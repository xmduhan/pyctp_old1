# -*- coding: utf-8 -*-


1、如何管理CTPConverter的通讯地址问题，如何保证多进程同时启动不会冲突(ok)
1、如何杀死defunct状态的进程(ok,使用wait())
1、如何防止子进程的stdout无线膨胀(ok)
1、CTPChannel中的ctp tarder转换器进程的创建与清除（ok）
1、查询类api的通用测试用例全部通过(ok)

#%%
1、增加MdChannel支持
(1)修改CTPChannel为TraderChannel,channel.py为CTPChannel.py
(2)增加初始化代码内容
1、请求延时机制响应机制(查询请求流量控制)
1、按照实际交易的需求编写一个测试用例集合
1、增加一个守护进程负责当主进程强行关闭的时候可以杀死通道进程
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
'--instrumentIDConfigFile',tempConfigFile
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

ch = MdChannel(frontAddress,brokerID,userID,password,['IF1506'],fileOutput='/tmp/md.log')
ch.readMarketData()

#%%
def test():
    raise Exception(u'测试')
test()

