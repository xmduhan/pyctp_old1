# -*- coding: utf-8 -*-
import os
from nose.plugins.attrib import attr
from CTPChannel import TraderChannel,MdChannel
from CTPChannelPool import TraderChannelPool
from CTPStruct import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
from time import sleep
import psutil
import subprocess
import shlex

def setup():
    '''
    所有用例的公共初始化代码
    '''
    global frontAddress,mdFrontAddress,brokerID,userID,password
    # 读取环境变量中的信息
    frontAddress = os.environ.get('CTP_FRONT_ADDRESS')
    assert frontAddress,u'必须定义环境变量:CTP_FRONT_ADDRESS'
    mdFrontAddress = os.environ.get('CTP_MD_FRONT_ADDRESS')
    assert mdFrontAddress,u'必须定义环境变量:CTP_MD_FRONT_ADDRESS'
    brokerID = os.environ.get('CTP_BROKER_ID')
    assert brokerID,u'必须定义环境变量:CTP_BROKER_ID'
    userID = os.environ.get('CTP_USER_ID')
    assert userID,u'必须定义环境变量:CTP_USER_ID'
    password = os.environ.get('CTP_PASSWORD')
    assert password,u'必须定义环境变量:CTP_PASSWORD'
    # 创建通道
    #traderChannel = TraderChannel(frontAddress,brokerID,userID,password)


@attr('TraderChannel')
@attr('test_QueryApiDelayMechanism')
@attr('test_QueryApiDelayMechanismBasicTest')
def test_QueryApiDelayMechanismBasicTest():
    '''
    测试query api的延迟机制
    '''
    queryInterval = 1.1
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,queryInterval=queryInterval
    )
    data = CThostFtdcQryTradingAccountField()
    # 第1次调用api
    result = traderChannel.QryTradingAccount(data)
    assert result[0] == 0, u'调用api返回错误(result[0]=%d,result[1]=%s)' % (result[0],result[1])
    # 第2次调用api
    queryWaitTime = traderChannel.getQueryWaitTime()
    print 'queryWaitTime=',queryWaitTime
    beginTime = datetime.now()
    result = traderChannel.QryTradingAccount(data)
    endTime = datetime.now()
    executeTime = (endTime - beginTime).total_seconds()
    print 'executeTime=',executeTime
    assert executeTime > queryWaitTime
    #assert executeTime - queryWaitTime < .1
    # 确定第2次调用进行了延迟操作
    #assert executeTime > (queryInterval * 0.9) ,u'延迟调用没有生效'
    # 检查返回是否成功
    assert result[0] == 0, u'调用api返回错误(result[0]=%d,result[1]=%s)' % (result[0],result[1])



@attr('TraderChannel')
@attr('test_QueryApiDelayMechanism')
@attr('test_QueryApiDelayMechanismCounterExample')
def test_QueryApiDelayMechanismCounterExample():
    '''
    延迟机制的反向测试用例
    '''
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,queryInterval=0
    )
    data = CThostFtdcQryTradingAccountField()
    sleep(1)
    # 第1次调用api
    result = traderChannel.QryTradingAccount(data)
    assert result[0] == 0, u'调用api返回错误(result[0]=%d,result[1]=%s)' % (result[0],result[1])
    # 第1次调用api
    for i in range(10):
        result = traderChannel.QryTradingAccount(data)
        # 由于没有延迟设置所以调用不成功
        if result[0] == -3:
            break
    else :
        raise Exception(u'没有发生预期的流量控制错误')



@attr('TraderChannel')
@attr('test_QueryApiDelayMechanism')
@attr('test_ConverterQueryApiDelayMechanism')
def test_ConverterQueryApiDelayMechanism():
    '''

    '''
    # 模拟两个查询请求同时到达队列,但没有启用转换器的流量控制功能
    # NOTE 默认情况下转换器流量控制延迟和queryInterval一致
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,queryInterval = 0)
    data = CThostFtdcQryTradingAccountField()
    # 由于将queryInterval设为0,破坏查询等待机制,需要等待一下,否则连第1个查询都会出错
    sleep(1)
    # 连续调用2次查询api
    result = traderChannel.QryTradingAccount(data)
    assert result[0] == 0
    for i in range(10):
        result = traderChannel.QryTradingAccount(data)
        # 由于没有延迟设置所以调用不成功
        if result[0] == -3:
            break
    else :
        raise Exception(u'没有发生预期的流量控制错误')

    # 启动转换器的流量控制功能调用就能成功
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,queryInterval = 0,
        timeout=5,converterQueryInterval = 1
    )
    data = CThostFtdcQryTradingAccountField()
    # 连续调用2次查询api
    result = traderChannel.QryTradingAccount(data)
    if result[0] != 0:
        print result[1]
    assert result[0] == 0
    result = traderChannel.QryTradingAccount(data)
    if result[0] != 0:
        print result[1]
    assert result[0] == 0


@attr('TraderChannel')
@attr('test_QueryApiDelayMechanism')
@attr('test_SystemHighLoadWithoutTraderQueryIntervalOption')
def test_SystemHighLoadWithoutTraderQueryIntervalOption():
    '''
    测试在系统高负荷情况下不使用转换器的流量控制选项,可能间歇性的出现错误
    '''
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,timeout = 10
    )
    data = CThostFtdcQryTradingAccountField()

    # 模拟系统过载的情况
    commandLine = shlex.split('stress --cpu 3 --io 3 --vm 10 --timeout 10')
    subprocess.Popen(commandLine,stdout=open('/dev/null'))

    # 连续调用10次查询api
    for i in range(10):
        result = traderChannel.QryTradingAccount(data)
        if result[0] != 0 :
            print result[1]
        assert result[0] == 0


@attr('TraderChannel')
@attr('test_TraderChannelCleanCTPProcess')
def test_TraderChannelCleanCTPProcess():
    '''
    测试TraderChannel是否能正常清理进程
    '''
    process = psutil.Process()
    # 没有创建TraderChannel对象前应该没有trader进程
    #assert 'trader' not in [child.name() for child in process.children() ]

    # 创建后可以找到一个trader进程
    traderChannel = TraderChannel(frontAddress,brokerID,userID,password)
    pid = traderChannel.traderProcess.pid
    assert pid and pid != 0
    assert pid in [child.pid for child in process.children()]

    # 将变量指向None迫使垃圾回收,确认进程被清理了
    traderChannel = None
    sleep(1)
    assert pid not in [child.pid for child in process.children() ]


@attr('TraderChannel')
@attr('test_TraderChannelStartupStressTest')
def test_TraderChannelStartupStressTest():
    '''
    TraderChannel的启动压力测试
    1.测试反复重新创建TraderChannel对象是否能正常运行
    2.反复创建TraderChannel对象是否能够正常回收进程
    '''

    pidList = []

    # 启动调用测试
    for i in range(10):
        traderChannel = TraderChannel(frontAddress,brokerID,userID,password)
        data = CThostFtdcQryTradingAccountField()
        result = traderChannel.QryTradingAccount(data)
        assert result[0] == 0
        pid = traderChannel.traderProcess.pid
        assert pid and pid != 0
        pidList.append(pid)

    # 进程清理测试
    traderChannel = None
    process = psutil.Process()
    sleep(1)
    for pid in pidList:
        assert pid not in [child.pid for child in process.children()]



@attr('TraderChannelPool')
@attr('test_TraderChannelPoolForFaster')
def test_TraderChannelPoolForFaster():
    '''
    测试使用TraderChannelPool为查询api加速
    '''
    queryInterval = 1.1

    # 使用TraderChannel
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,queryInterval=queryInterval
    )
    data = CThostFtdcQryTradingAccountField()
    beginTime = datetime.now()
    for i in range(5):
        result = traderChannel.QryTradingAccount(data)
        assert result[0] == 0
    endTime = datetime.now()
    executeTime = (endTime - beginTime).total_seconds()
    print 'TraderChannel:executeTime=',executeTime
    assert executeTime > 5

    # 使用TraderChannelPool
    traderChannelPool = TraderChannelPool(
        frontAddress,brokerID,userID,password,nChannel=5,queryInterval=queryInterval
    )
    data = CThostFtdcQryTradingAccountField()
    beginTime = datetime.now()
    for i in range(5):
        result = traderChannelPool.QryTradingAccount(data)
        assert result[0] == 0
    endTime = datetime.now()
    executeTime = (endTime - beginTime).total_seconds()
    print 'TraderChannelPool:executeTime=',executeTime
    assert executeTime < 1.5


@attr('MdChannel')
@attr('test_MdChannelCreate')
def test_MdChannelCreate():
    '''
    测试MdChannel的创建和使用
    '''
    instrumentID = datetime.strftime(datetime.now() + relativedelta(months=1),"IF%y%m")
    mdChannel = MdChannel(mdFrontAddress,brokerID,userID,password,[instrumentID])
    result = mdChannel.readMarketData(1000)
    assert isinstance(result,CThostFtdcDepthMarketDataField)
    data = result.toDict()
    assert data['InstrumentID'] == instrumentID


@attr('MdChannel')
@attr('TraderChannel')
@attr('TraderChannelPool')
@attr('test_ChannelClassUseWithStatment')
def test_ChannelClassUseWithStatment():
    '''
    确认Channel相关对象可以使用with语句
    '''
    with TraderChannel(frontAddress,brokerID,userID,password) as traderChannel:
        assert traderChannel

    with TraderChannelPool(frontAddress,brokerID,userID,password) as traderChannelPool:
        assert traderChannelPool

    instrumentID = datetime.strftime(datetime.now() + relativedelta(months=1),"IF%y%m")
    with MdChannel(mdFrontAddress,brokerID,userID,password,[instrumentID]) as mdChannel:
        assert mdChannel


@attr('MdChannel')
@attr('TraderChannel')
@attr('test_OutputFileDirectoryIsolation')
def test_OutputFileDirectoryIsolation():
    '''
    测试通道目录的隔离
    '''
    # 测试交易通道
    with TraderChannel(frontAddress,brokerID,userID,password) as traderChannel:
        assert traderChannel
        assert os.path.exists(traderChannel.workdir)
        filenameList =  os.listdir(traderChannel.workdir)
        print filenameList
        assert 'QueryRsp.con' in filenameList
        assert 'DialogRsp.con' in filenameList
        assert 'TradingDay.con' in filenameList
        assert 'Private.con' in filenameList
        assert 'Public.con' in filenameList
        assert 'trader.log' in filenameList

    # 测试行情通道
    instrumentID = datetime.strftime(datetime.now() + relativedelta(months=1),"IF%y%m")
    with MdChannel(mdFrontAddress,brokerID,userID,password,[instrumentID]) as mdChannel:
        assert mdChannel
        assert os.path.exists(mdChannel.workdir)
        filenameList =  os.listdir(mdChannel.workdir)
        print filenameList
        assert 'QueryRsp.con' in filenameList
        assert 'DialogRsp.con' in filenameList
        assert 'TradingDay.con' in filenameList
        assert 'md.log' in filenameList


@attr('TraderChannel')
@attr('test_SettlementInfoConfirm')
def test_SettlementInfoConfirm():
    '''
    测试结算确认
    '''
    traderChannel = TraderChannel(frontAddress,brokerID,userID,password)
    requestData = CThostFtdcSettlementInfoConfirmField()
    requestData.BrokerID = brokerID
    requestData.InvestorID = userID
    requestData.ConfirmDate = ''
    requestData.ConfirmTime = ''
    result = traderChannel.SettlementInfoConfirm(requestData)
    assert result[0] == 0
    responseData = result[2][0]
    assert responseData.BrokerID == brokerID
    assert responseData.InvestorID == userID



orderRefSeq = 0
def getOrderRef():
    '''
    获取OrderRef序列值
    '''
    global orderRefSeq
    orderRefSeq += 1
    return ('%12d' % orderRefSeq).replace(' ','0') # '000000000001'


def getDefaultInstrumentID():
    '''
    获得一个保证可以使用的合同代码
    '''
    return datetime.strftime(datetime.now() + relativedelta(months=1),"IF%y%m")



def getDefaultInputOrderField():
    '''
    获得一个默认的参数合法的,提交请求结构
    '''
    inputOrderField = CThostFtdcInputOrderField()
    inputOrderField.BrokerID = brokerID
    inputOrderField.InvestorID = userID
    inputOrderField.InstrumentID = getDefaultInstrumentID()
    inputOrderField.OrderRef =  getOrderRef() #
    inputOrderField.UserID = userID
    inputOrderField.OrderPriceType = '1'     # 任意价
    #inputOrderField.Direction = '0'          # 买
    #inputOrderField.CombOffsetFlag = '0'     # 开仓
    inputOrderField.CombHedgeFlag = '1'      # 投机
    inputOrderField.LimitPrice = 0           # 限价 0表不限制
    inputOrderField.VolumeTotalOriginal = 1  # 手数
    inputOrderField.TimeCondition = '1'      # 立即完成否则撤消
    inputOrderField.GTDDate = ''
    inputOrderField.VolumeCondition = '1'    # 成交类型  '1' 任何数量  '2' 最小数量 '3'全部数量
    inputOrderField.MinVolume = 1            # 最小数量
    inputOrderField.ContingentCondition = '1' # 触发类型 '1' 立即否则撤消
    inputOrderField.StopPrice = 0             # 止损价
    inputOrderField.ForceCloseReason = '0'    # 强平标识 '0'非强平
    inputOrderField.IsAutoSuspend = 0         # 自动挂起标识
    inputOrderField.BusinessUnit = ''         # 业务单元
    inputOrderField.RequestID = 1
    inputOrderField.UserForceClose = 0        # 用户强平标识
    inputOrderField.IsSwapOrder = 0           # 互换单标识
    return inputOrderField


def getDefaultInputOrderField_buyOpen():
    '''
    获得一个默认的多头开仓报单数据
    '''
    inputOrderField = getDefaultInputOrderField()
    inputOrderField.Direction = '0'          # 买
    inputOrderField.CombOffsetFlag = '0'     # 开仓
    return inputOrderField

def getDefaultInputOrderField_buySell():
    '''
    获得一个默认的多头平仓报单数据
    '''
    inputOrderField = getDefaultInputOrderField()
    inputOrderField.Direction = '1'          # 卖
    inputOrderField.CombOffsetFlag = '1'     # 平仓
    return inputOrderField

def getDefaultInputOrderField_sellOpen():
    '''
    获得一个默认的空头开仓报单数据
    '''
    inputOrderField = getDefaultInputOrderField()
    inputOrderField.Direction = '1'          # 卖
    inputOrderField.CombOffsetFlag = '0'     # 开仓
    return inputOrderField


def getDefaultInputOrderField_sellClose():
    '''
    获得一个默认的空头平仓报单数据
    '''
    inputOrderField = getDefaultInputOrderField()
    inputOrderField.Direction = '0'          # 买
    inputOrderField.CombOffsetFlag = '1'     # 平仓
    return inputOrderField


@attr('TraderChannel')
@attr('test_OrderInsert')
@attr('test_OrderInsert_OpenAndClose')
def test_OrderInsert_OpenAndClose():
    '''
    测试报单
    '''
    traderChannel = TraderChannel(frontAddress,brokerID,userID,password,timeout = 1)
    print 'tail -f %s/trader.log' % traderChannel.workdir
    requestData = getDefaultInputOrderField_buyOpen()
    result = traderChannel.OrderInsert(requestData)
    assert result[0] == -2003


@attr('TraderChannel')
@attr('test_OrderInsert')
@attr('test_OrderInsert_WithInvalidValue')
def test_OrderInsert_WithInvalidValue():
    '''
    测试报单
    '''
    traderChannel = TraderChannel(frontAddress,brokerID,userID,password,timeout = 1)
    print 'tail -f %s/trader.log' % traderChannel.workdir
    requestData = getDefaultInputOrderField_buyOpen()
    requestData.VolumeTotalOriginal = 0         # 手数=0 使表单无效
    result = traderChannel.OrderInsert(requestData)
    print result
    assert result[0] == 15
    assert result[1] == u'CTP:报单字段有误'
