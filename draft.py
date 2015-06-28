# -*- coding: utf-8 -*-
#%% 已完成
1、如何管理CTPConverter的通讯地址问题，如何保证多进程同时启动不会冲突(ok)
1、如何杀死defunct状态的进程(ok,使用wait())
1、如何防止子进程的stdout无线膨胀(ok)
1、CTPChannel中的ctp tarder转换器进程的创建与清除（ok）
1、查询类api的通用测试用例全部通过(ok)
1、增加MdChannel支持(ok)
(1)修改CTPChannel为TraderChannel,channel.py为CTPChannel.py
(2)增加初始化代码内容
1、增加一个守护进程负责当主进程强行关闭的时候可以杀死通道进程(ok)
1、思考是否删除example.py.tpl(ok,已删除)
1、请求延时机制响应机制(查询请求流量控制)(ok)
1、实现一个实验性的TraderChannelPool(ok)
1、延迟响应机制和TraderChannelPool的测试用例(ok)
1、TraderChannel进程清理的测试用例(ok)
1、行情api的测试用例(ok)
1、不同的convert进程如果同时启动会产生.con文件会不会出现冲突的问题?(ok)
1、TraderChannelPool多个Channel写同一个文件会不会有问题(ok)
1、为MdChannel，TraderChannel增加__exit__和__enter__(ok)

#%% 待处理（问题列表）

1、通用请求流程只能现实查询api其他api在没有找到规律前需要手工编写,先实线OrderInsert
之后再考虑如何转化为通用调用方法.




1、打开的文件没有关闭会不会有问题
1、按照实际交易的需求编写一个测试用例集合
1、增加异步功能api,同时增加同步api的容错能力
1、convert启动是否完成需要通过检查日志，而不是设定延时

#%% 暂缓
1、去掉TraderChannel流量控制机制，仅保留最后查询时间(看来还不能去掉)

#%% 启动trader进程的测试代码
import uuid
import os
import tempfile
import subprocess

def mallocIpcAddress():
    return 'ipc://%s/%s' % (tempfile.gettempdir(),uuid.uuid1())
    
frontAddress = os.environ.get('CTP_FRONT_ADDRESS') 
assert frontAddress
brokerID = os.environ.get('CTP_BROKER_ID') 
assert brokerID
userID = os.environ.get('CTP_USER_ID') 
assert userID
password = os.environ.get('CTP_PASSWORD') 
assert password    
requestPipe = mallocIpcAddress()
pushbackPipe = mallocIpcAddress()
publishPipe = mallocIpcAddress()

option = [
'--FrontAddress',frontAddress,
'--BrokerID',brokerID,
'--UserID',userID,
'--Password', password,
'--RequestPipe', requestPipe,
'--PushbackPipe', pushbackPipe,
'--PublishPipe', publishPipe,
]

command = ['trader']
command.extend(option)
command


#%%  测试TraderChannel
import os
from datetime import datetime
os.chdir(u'/home/duhan/github/pyctp')
from CTPChannel import TraderChannel
from CTPStruct import *
from time import sleep

frontAddress = os.environ.get('CTP_FRONT_ADDRESS')
assert frontAddress
brokerID = os.environ.get('CTP_BROKER_ID')
assert brokerID
userID = os.environ.get('CTP_USER_ID')
assert userID
password = os.environ.get('CTP_PASSWORD')
assert password

ch = TraderChannel(frontAddress,brokerID,userID,password,'/tmp/trader.log',1.1)
data = CThostFtdcQryTradingAccountField()
print ch.getQueryWaitTime()
print ch.QryTradingAccount(data)
#sleep(1)
#print ch.QryTradingAccount(data)
#print ch.QryTradingAccount(data)
#print ch.QryTradingAccount(data)
#print ch.QryTradingAccount(data)
#print ch.QryTradingAccount(data)
#(datetime.now() - ch.lastQueryTime).total_seconds()
#for i in range(10):
#    print ch.QryTradingAccount(data)

#%% 测试TraderChannelPool
import os
from datetime import datetime
os.chdir(u'/home/duhan/github/pyctp')
from CTPChannelPool import TraderChannelPool
from CTPStruct import *
from time import sleep

frontAddress = os.environ.get('CTP_FRONT_ADDRESS')
assert frontAddress
brokerID = os.environ.get('CTP_BROKER_ID')
assert brokerID
userID = os.environ.get('CTP_USER_ID')
assert userID
password = os.environ.get('CTP_PASSWORD')
assert password
channelPool = \
TraderChannelPool(frontAddress,brokerID,userID,password,nChannel=5,ctpQueryInterval=1.1)

#%%
data = CThostFtdcQryTradingAccountField()
for i in range(10):
    print channelPool.QryTradingAccount(data),channelPool.getMinWaitChannel()


#%%  启动md进程代码
import uuid
import os
import tempfile
import subprocess
def mallocIpcAddress():
    return 'ipc://%s/%s' % (tempfile.gettempdir(),uuid.uuid1())
    
frontAddress = os.environ.get('CTP_MD_FRONT_ADDRESS') 
assert frontAddress
brokerID = os.environ.get('CTP_BROKER_ID') 
assert brokerID
userID = os.environ.get('CTP_USER_ID') 
assert userID
password = os.environ.get('CTP_PASSWORD') 
assert password    
pushbackPipe = mallocIpcAddress()
publishPipe = mallocIpcAddress()
tempConfigFile = '/etc/ctp/config.json'
fileOutput = '/tmp/md.log'

# 构造调用命令
commandLine = ['md',
'--FrontAddress',frontAddress,
'--BrokerID',brokerID,
'--UserID',userID,
'--Password', password,
'--PushbackPipe', pushbackPipe,
'--PublishPipe', publishPipe,
'--InstrumentIDConfigFile',tempConfigFile
]
traderStdout = open(fileOutput, 'w')
mdProcess = subprocess.Popen(commandLine,stdout=traderStdout)

#%% 测试MdChannel
import os
os.chdir(u'/home/duhan/github/pyctp')
from CTPChannel import MdChannel
from CTPStruct import *

frontAddress = os.environ.get('CTP_MD_FRONT_ADDRESS')
assert frontAddress
brokerID = os.environ.get('CTP_BROKER_ID')
assert brokerID
userID = os.environ.get('CTP_USER_ID')
assert userID
password = os.environ.get('CTP_PASSWORD')
assert password

ch = MdChannel(frontAddress,brokerID,userID,password,['IF1506','IF1507'],fileOutput='/tmp/md.log')
ch.readMarketData()


#%% 测试计算时间间隔并等待
from datetime import datetime 
from time import sleep
from datetime import timedelta
beginTime = datetime.now()
sleep(.1)
endTime = datetime.now()
timeDelta = endTime-beginTime
needWait = 1-timeDelta.total_seconds()
sleep(needWait)

#%% 计算间隔时间 
beginTime = datetime.now()
endTime = beginTime - timedelta(seconds=1)
(endTime-beginTime).total_seconds()


#%% 子进程信息查询
import psutil
process = psutil.Process()
childrenNameList = [child.name() for child in process.children() ]
'trader' in childrenNameList

#%%
from datetime import datetime
from dateutil.relativedelta import relativedelta
datetime.strftime(datetime.now() + relativedelta(months=1),"%y%m")  


#%% 格式化毫秒
from datetime import datetime
print datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

#%% 生成一个
import uuid
'ipc///tmp/%s' % uuid.uuid1()

