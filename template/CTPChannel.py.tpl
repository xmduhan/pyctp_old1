# -*- coding: utf-8 -*-
import os
import zmq
import json
import uuid
import tempfile
import subprocess
from CTPStruct import *
from message import *
from time import sleep
from datetime import datetime,timedelta


def packageReqInfo(apiName,data):
	'''
	获取一个默认的调用结构
	'''
	reqInfo = {}
	reqInfo['RequestMethod'] = apiName
	parameters = {}
	reqInfo['Parameters'] = parameters
	parameters['Data'] = data
	return reqInfo

# 定义通用的出错返回数据
InvalidRequestFormat = [-2000,u'参数表单类型不正确',[]]
ResponseTimeOut = [-2001,u'请求超时未响应',[]]
InvalidMessageFormat = [-2002,u'接收到异常消息格式',[]]


#def mallocIpcAddress():
#	return 'ipc://%s/%s' % (tempfile.gettempdir(),uuid.uuid1())


def mallocIpcAddress():
	return 'ipc://%s' % tempfile.mktemp(suffix='.ipc',prefix='tmp_')




class MdChannel :
	'''
	Md通讯管道类,该类通过和CTPConverter的Md(行情)进程通讯,实线行情数据的传送
	'''



	def __testChannel(self):
		'''
		检查和ctp md 进程是否连通
		在md进程启动后会先发送一个空消息,提供测试通路使用
		'''
		# 由于zmq publisher需要等待客户端连接，这里等待相应时间才能接受到消息
		timeout = 2000
		reader = self.reader
		poller = zmq.Poller()
		poller.register(reader, zmq.POLLIN)
		sockets = dict(poller.poll(timeout))
		if reader in sockets :
			result = reader.recv_multipart()
			if len(result) == 1 and result[0] == "":
				return True
			else:
				self.__delTraderProcess()
				raise Exception(u'接收到不正确的消息格式')
		else:
			return False



	def __delTraderProcess(self):
		'''
		清除trader转换器进程
		'''
		self.mdProcess.kill()
		self.mdProcess.wait()



	def __init__(self,frontAddress,brokerID,userID,password,instrumentIdList,fileOutput='/dev/null'):
		'''
		1.创建ctp转换器进程
		2.创建和ctp通讯进程的通讯管道
		3.测试ctp连接是否正常
		参数:
		frontAddress   ctp服务器地址
		brokerID   代理商Id
		userID   用户Id
		password   密码
		instrumentIdList   需要订阅的品种的Id列表
		fileOutput   ctp trader通讯进程的日志信息的保存路径,默认抛弃('/dev/null')
		'''
		# 为ctp md转换器分配通讯管道地址
		self.pushbackPipe = mallocIpcAddress()
		self.publishPipe = mallocIpcAddress()

		# 生成md命令需要的临时配置文件(描述品种ID列表)
		self.tempConfigFile = tempfile.mktemp(suffix='.json')
		instrumentIdListJson = json.dumps(instrumentIdList)
		with open(self.tempConfigFile, 'w') as f:
			f.write(instrumentIdListJson.encode('utf-8'))

		# 创建接受行情数据的管道
		context = zmq.Context()
		self.context = context
		socket = context.socket(zmq.SUB)
		socket.connect(self.publishPipe)
		socket.setsockopt(zmq.SUBSCRIBE, '');
		self.reader = socket

		# 构造调用命令
		commandLine = ['md',
		'--FrontAddress',frontAddress,
		'--BrokerID',brokerID,
		'--UserID',userID,
		'--Password', password,
		'--PushbackPipe', self.pushbackPipe,
		'--PublishPipe', self.publishPipe,
		'--InstrumentIDConfigFile',self.tempConfigFile,
		'--loyalty'
		]

		# 创建转换器子进程
		traderStdout = open(fileOutput, 'w')
		self.mdProcess = subprocess.Popen(commandLine,stdout=traderStdout)

		# 检查ctp通道是否建立，如果失败抛出异常
		if not self.__testChannel():
			self.__delTraderProcess()
			raise Exception(u'无法建立ctp连接,具体错误请查看ctp转换器的日志信息')



	def __del__(self):
		'''
		对象移出过程
		1.结束ctp转换器进程
		'''
		self.__delTraderProcess()



	def readMarketData(self,timeout=1):
		'''
		读取行情数据
		参数
		timeout 如果当前没有消息的等待时间(毫秒)
		'''
		reader = self.reader
		poller = zmq.Poller()
		poller.register(reader, zmq.POLLIN)
		sockets = dict(poller.poll(timeout))
		if reader in sockets :
			result = reader.recv_multipart()
			# TODO 这里假设了result只有一个元素,最好是检查一下
			if len(result) == 1 and result[0] != "":
				resultDict = json.loads(result[0])
				marketData = CThostFtdcDepthMarketDataField(**resultDict)
				return marketData
			else:
				raise Exception(u'接收到不正确的消息格式')
		else:
			return None



class TraderChannel :
	'''
	Trader通讯管道类,该类通过和CTPConverter的Trader进程通讯,对外实现python语言封装的CTP接口,
	在设计上该类既支持同步接口也支持异步接口,但是目前暂时先实现同步接口.
	'''

	def __testChannel(self):
		'''
		检查ctp交易通道是否运行正常，该方法在构造函数内调用如果失败，构造函数会抛出异常
		成功返回True，失败返回False
		'''
		data = CThostFtdcQryTradingAccountField()
		result = self.QryTradingAccount(data)
		return result[0] == 0


	def __delTraderProcess(self):
		'''
		清除trader转换器进程
		'''
		self.traderProcess.kill()
		self.traderProcess.wait()


	def __init__(self,frontAddress,brokerID,userID,password,fileOutput='/dev/null'
		,queryInterval=1,timeout=1,useTraderQueryIntervalOption=True):
		'''
		初始化过程:
		1.创建ctp转换器进程
		2.创建和ctp通讯进程的通讯管道
		3.测试ctp连接是否正常
		如果ctp连接测试失败，将抛出异常阻止对象的创建
		参数:
		frontAddress   ctp服务器地址
		brokerID   代理商编号
		userID   用户编号
		password   密码
		fileOutput   ctp trader通讯进程的日志信息的保存路径,默认抛弃('/dev/null')
		queryInterval  查询间隔时间(单位:秒)
		timeout 等待响应时间(单位:秒)
		useTraderQueryIntervalOption 是否使用转换器级的流量控制,实际使用应该开启,增加此选项主要是方便测试
		'''
		# 设置上次查询时间
		self.queryInterval = queryInterval
		# NOTE:虽然这里之前没有ctp query请求,仍然要预留等待时间,是由于启动转化器进程是需要时
		# 间的,转化器此时还无法响应请求,而初始化过程马上就发出一个查询请,以测试通道是否通畅,
		# 该请求会在zmq队列中排队,排队时间也是计时的.而ctp流量控制计算的是发向服务器的时间,
		# 是不是送到zmq消息队列的时间.所以这里要考虑ctp trader转换器的时间这里暂定为1秒
		traderProcessStartupTime = 1.5
		self.lastQueryTime = datetime.now() - timedelta(seconds=queryInterval)
		self.lastQueryTime +=  timedelta(seconds=traderProcessStartupTime)
		self.queryIntervalMillisecond = queryInterval * 1000


		# 为ctp转换器分配通讯管道地址
		self.requestPipe = mallocIpcAddress()
		self.pushbackPipe = mallocIpcAddress()
		self.publishPipe = mallocIpcAddress()

		# 构造调用命令
		commandLine = ['trader',
		'--FrontAddress',frontAddress,
		'--BrokerID',brokerID,
		'--UserID',userID,
		'--Password', password,
		'--RequestPipe', self.requestPipe,
		'--PushbackPipe', self.pushbackPipe,
		'--PublishPipe', self.publishPipe,
		'--loyalty',
		#'--queryInterval',str(queryIntervalMillisecond)
		]
		if useTraderQueryIntervalOption:
			commandLine.append('--queryInterval')
			commandLine.append(str(self.queryIntervalMillisecond))

		# 创建转换器子进程
		traderStdout = open(fileOutput, 'w')
		self.traderProcess = subprocess.Popen(commandLine,stdout=traderStdout)

		# 创建请求通讯通道
		context = zmq.Context()
		self.context = context
		socket = context.socket(zmq.DEALER)
		socket.connect(self.requestPipe)
		socket.setsockopt(zmq.LINGER,0)
		self.request = socket
		self.timeoutMillisecond = 1000 * timeout

		# 检查ctp通道是否建立，如果失败抛出异常
		if not self.__testChannel():
			self.__delTraderProcess()
			raise Exception('无法建立ctp连接,具体错误请查看ctp转换器的日志信息')
			#raise Exception('''can't not connect to ctp server.''')


	def __del__(self):
		'''
		对象移出过程
		1.结束ctp转换器进程
		'''
		self.__delTraderProcess()



	def getQueryWaitTime(self):
		'''
		获取查询需要等待的时间
		'''
		needWait = self.queryInterval - (datetime.now() - self.lastQueryTime).total_seconds()
		if needWait > 0 :
			return needWait
		else:
			return 0


	def queryWait(self):
		'''
		查询前的等待,如果需要的话
		'''
		sleep(self.getQueryWaitTime())



{% for method in reqMethodDict.itervalues() %}
	{% set parameter = method['parameters'][0]  %}
	def {{ method['name'][3:]}}(self,data):
		'''
		{{ method['remark'][3:] }}
		data 调用api需要填写参数表单,类型为{{parameter['raw_type']}},具体参见其定义文件
		返回信息格式[errorID,errorMsg,responseData=[...]]
		注意:同步调用没有metaData参数,因为没有意义
		'''
		if not isinstance(data,{{parameter['raw_type']}}):
			return InvalidRequestFormat


		requestApiName = 'Req{{method['name'][3:]}}'
		responseApiName = 'OnRsp{{method['name'][3:]}}'

		# 打包消息格式
		reqInfo = packageReqInfo(requestApiName,data.toDict())
		metaData={}
		requestMessage = RequestMessage()
		requestMessage.header = 'REQUEST'
		requestMessage.apiName = requestApiName
		requestMessage.reqInfo = json.dumps(reqInfo)
		requestMessage.metaData = json.dumps(metaData)

		{% if method['name'][3:6] == 'Qry' or method['name'][3:8] == 'Query' %}
		# 查询前的等待,避免超过ctp查询api的流量控制
		self.queryWait()
		# NOTE:更新lastQueryTime不能放在同步调用的返回处,因为有的调用返回时间非常长,这样再
		# 等待就没有必要
		self.lastQueryTime = datetime.now()
		{% endif %}

		# 发送到服务器
		requestMessage.send(self.request)
		################### 等待服务器的REQUESTID响应 ###################
		# 读取服务
		poller = zmq.Poller()
		poller.register(self.request, zmq.POLLIN)
		sockets = dict(poller.poll(self.timeoutMillisecond))
		if not (self.request in sockets) :
			return ResponseTimeOut

		# 从request通讯管道读取返回信息
		requestIDMessage = RequestIDMessage()
		requestIDMessage.recv(self.request)

		# 检查接收的消息格式
		c1 = requestIDMessage.header == 'REQUESTID'
		c2 = requestIDMessage.apiName == requestApiName
		if not ( c1 and c2 ):
			return InvalidMessageFormat

		# 如果没有收到RequestID,返回转换器的出错信息
		if not (int(requestIDMessage.requestID) > 0):
			errorInfo = json.loads(requestIDMessage.errorInfo)
			return errorInfo['ErrorID'],errorInfo['ErrorMsg'],[]


		################### 等待服务器的返回的数据信息 ###################
		poller = zmq.Poller()
		poller.register(self.request, zmq.POLLIN)

		# 循环读取所有数据
		respnoseDataList = []
		while(True):
			sockets = dict(poller.poll(self.timeoutMillisecond))
			if not (self.request in sockets) :
				return ResponseTimeOut

			# 从request通讯管道读取返回信息
			responseMessage = ResponseMessage()
			responseMessage.recv(self.request)

			# 返回数据信息格式符合要求
			c1 = responseMessage.header == 'RESPONSE'
			c2 = responseMessage.requestID == requestIDMessage.requestID
			c3 = responseMessage.apiName in (responseApiName,requestApiName)
			if not (c1 and c2 and c3) :
				return InvalidMessageFormat

			# 提取消息中的出错信息
			respInfo = json.loads(responseMessage.respInfo)
			errorID = respInfo['Parameters']['RspInfo']['ErrorID']
			errorMsg = respInfo['Parameters']['RspInfo']['ErrorMsg']
			if errorID != 0 :
				return errorID,errorMsg,[]

			# 提取消息中的数据
			{% set responseDataType = onRspMethodDict['OnRsp' + method['name'][3:]]['parameters'][0]['raw_type']%}
			respnoseDataDict = respInfo['Parameters']['Data']
			if respnoseDataDict:
				respnoseData = {{responseDataType}}(**respnoseDataDict)
				respnoseDataList.append(respnoseData)

			# 判断是否已是最后一条消息
			if int(responseMessage.isLast) == 1:
				break;

		# 返回成功
		return 0,'',respnoseDataList



{% endfor %}
