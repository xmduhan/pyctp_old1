# -*- coding: utf-8 -*-


1、如何管理CTPConverter的通讯地址问题，如何保证多进程同时启动不会冲突(ok)
1、如何杀死defunct状态的进程(ok,使用wait())
1、如何防止子进程的stdout无线膨胀(ok)
1、CTPChannel中的ctp tarder转换器进程的创建与清除（ok）
1、查询类api的通用测试用例全部通过(ok)
1、增加MdChannel支持(ok)
(1)修改CTPChannel为TraderChannel,channel.py为CTPChannel.py
(2)增加初始化代码内容

#%%
1、增加一个守护进程负责当主进程强行关闭的时候可以杀死通道进程
1、请求延时机制响应机制(查询请求流量控制)
1、按照实际交易的需求编写一个测试用例集合
1、思考是否删除example.py.tpl
1、打开的文件没有关闭会不会有问题

#%%
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
#%%
devnull = open('/dev/null', 'w')
sp = subprocess.Popen(command,stdout=devnull)

#%%
sp.kill()
sp.wait()
#%%
import os
os.chdir(u'/home/duhan/github/pyctp')
from CTPChannel import TraderChannel
from CTPStruct import *

frontAddress = os.environ.get('CTP_FRONT_ADDRESS')
assert frontAddress
brokerID = os.environ.get('CTP_BROKER_ID')
assert brokerID
userID = os.environ.get('CTP_USER_ID')
assert userID
password = os.environ.get('CTP_PASSWORD')
assert password

ch = TraderChannel(frontAddress,brokerID,userID,password,'/tmp/trader.log')
data = CThostFtdcQryTradingAccountField()
ch.QryTradingAccount(data)


#%%

#%%
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

#%%
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


#%%
a = ['{\n   "ActionDay" : "20150609",\n   "AskPrice1" : 5250.8000000000002,\n   "AskPrice2" : 1.7976931348623157e+308,\n   "AskPrice3" : 1.7976931348623157e+308,\n   "AskPrice4" : 1.7976931348623157e+308,\n   "AskPrice5" : 1.7976931348623157e+308,\n   "AskVolume1" : 3,\n   "AskVolume2" : 0,\n   "AskVolume3" : 0,\n   "AskVolume4" : 0,\n   "AskVolume5" : 0,\n   "AveragePrice" : 1583048.7369148347,\n   "BidPrice1" : 5250.2000000000007,\n   "BidPrice2" : 1.7976931348623157e+308,\n   "BidPrice3" : 1.7976931348623157e+308,\n   "BidPrice4" : 1.7976931348623157e+308,\n   "BidPrice5" : 1.7976931348623157e+308,\n   "BidVolume1" : 4,\n   "BidVolume2" : 0,\n   "BidVolume3" : 0,\n   "BidVolume4" : 0,\n   "BidVolume5" : 0,\n   "ClosePrice" : 5250.3999999999996,\n   "CurrDelta" : 1.7976931348623157e+308,\n   "ExchangeID" : "",\n   "ExchangeInstID" : "",\n   "HighestPrice" : 5364.3999999999996,\n   "InstrumentID" : "IF1506",\n   "LastPrice" : 5250.4000000000005,\n   "LowerLimitPrice" : 4811.3999999999996,\n   "LowestPrice" : 5186.1999999999998,\n   "OpenInterest" : 59736,\n   "OpenPrice" : 5343,\n   "PreClosePrice" : 5336.3999999999996,\n   "PreDelta" : 1.7976931348623157e+308,\n   "PreOpenInterest" : 55534,\n   "PreSettlementPrice" : 5346,\n   "SettlementPrice" : 5272.6000000000004,\n   "TradingDay" : "20150609",\n   "Turnover" : 1610703015300,\n   "UpdateMillisec" : 800,\n   "UpdateTime" : "16:05:00",\n   "UpperLimitPrice" : 5880.6000000000004,\n   "Volume" : 1017469\n}\n']



#%%
def test():
    raise Exception(u'测试')
test()

