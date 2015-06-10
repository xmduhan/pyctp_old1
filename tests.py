# -*- coding: utf-8 -*-
import os
from nose.plugins.attrib import attr
from CTPChannel import TraderChannel
from CTPChannelPool import TraderChannelPool
from CTPStruct import *
from datetime import datetime
from time import sleep

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
def test_QueryApiDelayMechanism():
    '''
    测试query api的延迟机制
    '''
    ctpQueryInterval = 1.1
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,ctpQueryInterval=ctpQueryInterval
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
    assert executeTime - queryWaitTime < .1
    # 确定第2次调用进行了延迟操作
    assert executeTime > (ctpQueryInterval * 0.9) ,u'延迟调用没有生效'
    # 检查返回是否成功
    assert result[0] == 0, u'调用api返回错误(result[0]=%d,result[1]=%s)' % (result[0],result[1])



@attr('TraderChannel')
@attr('test_QueryApiDelayMechanism')
@attr('test_QueryApiDelayMechanismCounterexample')
def test_QueryApiDelayMechanismCounterexample():
    '''
    延迟机制的反向测试用例
    '''
    ctpQueryInterval = 0
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,ctpQueryInterval=ctpQueryInterval
    )
    data = CThostFtdcQryTradingAccountField()
    sleep(1)
    # 第1次调用api
    result = traderChannel.QryTradingAccount(data)
    assert result[0] == 0, u'调用api返回错误(result[0]=%d,result[1]=%s)' % (result[0],result[1])
    # 第1次调用api
    result = traderChannel.QryTradingAccount(data)
    # 由于没有延迟设置所以调用不成功
    assert result[0] == -3,u'调用api返回错误(result[0]=%d,result[1]=%s)' % (result[0],result[1])



@attr('TraderChannelPool')
def test_TraderChannelPoolForFaster():
    '''
    测试使用TraderChannelPool为查询api加速
    '''
    ctpQueryInterval = 1.1

    # 使用TraderChannel
    traderChannel = TraderChannel(
        frontAddress,brokerID,userID,password,ctpQueryInterval=ctpQueryInterval
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
        frontAddress,brokerID,userID,password,nChannel=5,ctpQueryInterval=ctpQueryInterval
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
