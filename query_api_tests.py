# -*- coding: utf-8 -*-
import os
from channel import CTPChannel
from CTPStruct import *
from time import sleep
from nose.plugins.attrib import attr
from datetime import datetime

ch = None

def setup():
    '''
    所有用例的公共初始化代码
    '''
    global ch
    # 读取环境变量中的信息
    frontAddress = os.environ.get('CTP_FRONT_ADDRESS')
    brokerID = os.environ.get('CTP_BROKER_ID')
    userID = os.environ.get('CTP_USER_ID')
    password = os.environ.get('CTP_PASSWORD')
    # 创建通道
    ch = CTPChannel(frontAddress,brokerID,userID,password)
    sleep(1)




@attr('QueryApi')
@attr('QryTradingAccount')
def test_QryTradingAccount():
    '''
    测试QryTradingAccount
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryTradingAccount():开始'
    sleep(1)

    data = CThostFtdcQryTradingAccountField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryTradingAccount(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryTradingAccount():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryTradingAccount():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryTradingAccount():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryCFMMCTradingAccountKey')
def test_QryCFMMCTradingAccountKey():
    '''
    测试QryCFMMCTradingAccountKey
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryCFMMCTradingAccountKey():开始'
    sleep(1)

    data = CThostFtdcQryCFMMCTradingAccountKeyField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryCFMMCTradingAccountKey(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryCFMMCTradingAccountKey():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryCFMMCTradingAccountKey():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryCFMMCTradingAccountKey():执行结束'
    print '----------------------------------------------------------------------'






@attr('QueryApi')
@attr('QryTradingNotice')
def test_QryTradingNotice():
    '''
    测试QryTradingNotice
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryTradingNotice():开始'
    sleep(1)

    data = CThostFtdcQryTradingNoticeField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryTradingNotice(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryTradingNotice():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryTradingNotice():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryTradingNotice():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryTrade')
def test_QryTrade():
    '''
    测试QryTrade
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryTrade():开始'
    sleep(1)

    data = CThostFtdcQryTradeField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryTrade(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryTrade():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryTrade():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryTrade():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QueryMaxOrderVolume')
def test_QueryMaxOrderVolume():
    '''
    测试QueryMaxOrderVolume
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QueryMaxOrderVolume():开始'
    sleep(1)

    data = CThostFtdcQueryMaxOrderVolumeField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QueryMaxOrderVolume(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QueryMaxOrderVolume():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QueryMaxOrderVolume():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QueryMaxOrderVolume():执行结束'
    print '----------------------------------------------------------------------'






@attr('QueryApi')
@attr('QryInvestorPosition')
def test_QryInvestorPosition():
    '''
    测试QryInvestorPosition
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryInvestorPosition():开始'
    sleep(1)

    data = CThostFtdcQryInvestorPositionField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryInvestorPosition(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryInvestorPosition():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryInvestorPosition():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryInvestorPosition():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryBrokerTradingAlgos')
def test_QryBrokerTradingAlgos():
    '''
    测试QryBrokerTradingAlgos
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryBrokerTradingAlgos():开始'
    sleep(1)

    data = CThostFtdcQryBrokerTradingAlgosField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryBrokerTradingAlgos(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryBrokerTradingAlgos():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryBrokerTradingAlgos():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryBrokerTradingAlgos():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryOrder')
def test_QryOrder():
    '''
    测试QryOrder
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryOrder():开始'
    sleep(1)

    data = CThostFtdcQryOrderField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryOrder(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryOrder():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryOrder():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryOrder():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryExchange')
def test_QryExchange():
    '''
    测试QryExchange
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryExchange():开始'
    sleep(1)

    data = CThostFtdcQryExchangeField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryExchange(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryExchange():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryExchange():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryExchange():执行结束'
    print '----------------------------------------------------------------------'








@attr('QueryApi')
@attr('QryExchangeRate')
def test_QryExchangeRate():
    '''
    测试QryExchangeRate
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryExchangeRate():开始'
    sleep(1)

    data = CThostFtdcQryExchangeRateField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryExchangeRate(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryExchangeRate():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryExchangeRate():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryExchangeRate():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryInvestorPositionDetail')
def test_QryInvestorPositionDetail():
    '''
    测试QryInvestorPositionDetail
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryInvestorPositionDetail():开始'
    sleep(1)

    data = CThostFtdcQryInvestorPositionDetailField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryInvestorPositionDetail(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryInvestorPositionDetail():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryInvestorPositionDetail():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryInvestorPositionDetail():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QrySettlementInfoConfirm')
def test_QrySettlementInfoConfirm():
    '''
    测试QrySettlementInfoConfirm
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QrySettlementInfoConfirm():开始'
    sleep(1)

    data = CThostFtdcQrySettlementInfoConfirmField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QrySettlementInfoConfirm(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QrySettlementInfoConfirm():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QrySettlementInfoConfirm():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QrySettlementInfoConfirm():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryBrokerTradingParams')
def test_QryBrokerTradingParams():
    '''
    测试QryBrokerTradingParams
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryBrokerTradingParams():开始'
    sleep(1)

    data = CThostFtdcQryBrokerTradingParamsField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryBrokerTradingParams(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryBrokerTradingParams():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryBrokerTradingParams():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryBrokerTradingParams():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QueryCFMMCTradingAccountToken')
def test_QueryCFMMCTradingAccountToken():
    '''
    测试QueryCFMMCTradingAccountToken
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QueryCFMMCTradingAccountToken():开始'
    sleep(1)

    data = CThostFtdcQueryCFMMCTradingAccountTokenField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QueryCFMMCTradingAccountToken(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QueryCFMMCTradingAccountToken():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QueryCFMMCTradingAccountToken():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QueryCFMMCTradingAccountToken():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryNotice')
def test_QryNotice():
    '''
    测试QryNotice
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryNotice():开始'
    sleep(1)

    data = CThostFtdcQryNoticeField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryNotice(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryNotice():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryNotice():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryNotice():执行结束'
    print '----------------------------------------------------------------------'








@attr('QueryApi')
@attr('QryInvestorPositionCombineDetail')
def test_QryInvestorPositionCombineDetail():
    '''
    测试QryInvestorPositionCombineDetail
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryInvestorPositionCombineDetail():开始'
    sleep(1)

    data = CThostFtdcQryInvestorPositionCombineDetailField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryInvestorPositionCombineDetail(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryInvestorPositionCombineDetail():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryInvestorPositionCombineDetail():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryInvestorPositionCombineDetail():执行结束'
    print '----------------------------------------------------------------------'






@attr('QueryApi')
@attr('QrySecAgentACIDMap')
def test_QrySecAgentACIDMap():
    '''
    测试QrySecAgentACIDMap
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QrySecAgentACIDMap():开始'
    sleep(1)

    data = CThostFtdcQrySecAgentACIDMapField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QrySecAgentACIDMap(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QrySecAgentACIDMap():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QrySecAgentACIDMap():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QrySecAgentACIDMap():执行结束'
    print '----------------------------------------------------------------------'






@attr('QueryApi')
@attr('QueryBankAccountMoneyByFuture')
def test_QueryBankAccountMoneyByFuture():
    '''
    测试QueryBankAccountMoneyByFuture
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QueryBankAccountMoneyByFuture():开始'
    sleep(1)

    data = CThostFtdcReqQueryAccountField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QueryBankAccountMoneyByFuture(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QueryBankAccountMoneyByFuture():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QueryBankAccountMoneyByFuture():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QueryBankAccountMoneyByFuture():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryParkedOrderAction')
def test_QryParkedOrderAction():
    '''
    测试QryParkedOrderAction
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryParkedOrderAction():开始'
    sleep(1)

    data = CThostFtdcQryParkedOrderActionField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryParkedOrderAction(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryParkedOrderAction():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryParkedOrderAction():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryParkedOrderAction():执行结束'
    print '----------------------------------------------------------------------'






@attr('QueryApi')
@attr('QryExchangeMarginRate')
def test_QryExchangeMarginRate():
    '''
    测试QryExchangeMarginRate
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryExchangeMarginRate():开始'
    sleep(1)

    data = CThostFtdcQryExchangeMarginRateField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryExchangeMarginRate(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryExchangeMarginRate():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryExchangeMarginRate():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryExchangeMarginRate():执行结束'
    print '----------------------------------------------------------------------'








@attr('QueryApi')
@attr('QryInstrument')
def test_QryInstrument():
    '''
    测试QryInstrument
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryInstrument():开始'
    sleep(1)

    data = CThostFtdcQryInstrumentField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryInstrument(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryInstrument():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryInstrument():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryInstrument():执行结束'
    print '----------------------------------------------------------------------'






@attr('QueryApi')
@attr('QryInstrumentCommissionRate')
def test_QryInstrumentCommissionRate():
    '''
    测试QryInstrumentCommissionRate
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryInstrumentCommissionRate():开始'
    sleep(1)

    data = CThostFtdcQryInstrumentCommissionRateField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryInstrumentCommissionRate(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryInstrumentCommissionRate():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryInstrumentCommissionRate():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryInstrumentCommissionRate():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryInstrumentMarginRate')
def test_QryInstrumentMarginRate():
    '''
    测试QryInstrumentMarginRate
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryInstrumentMarginRate():开始'
    sleep(1)

    data = CThostFtdcQryInstrumentMarginRateField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryInstrumentMarginRate(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryInstrumentMarginRate():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryInstrumentMarginRate():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryInstrumentMarginRate():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryInvestor')
def test_QryInvestor():
    '''
    测试QryInvestor
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryInvestor():开始'
    sleep(1)

    data = CThostFtdcQryInvestorField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryInvestor(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryInvestor():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryInvestor():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryInvestor():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryExchangeMarginRateAdjust')
def test_QryExchangeMarginRateAdjust():
    '''
    测试QryExchangeMarginRateAdjust
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryExchangeMarginRateAdjust():开始'
    sleep(1)

    data = CThostFtdcQryExchangeMarginRateAdjustField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryExchangeMarginRateAdjust(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryExchangeMarginRateAdjust():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryExchangeMarginRateAdjust():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryExchangeMarginRateAdjust():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryInvestorProductGroupMargin')
def test_QryInvestorProductGroupMargin():
    '''
    测试QryInvestorProductGroupMargin
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryInvestorProductGroupMargin():开始'
    sleep(1)

    data = CThostFtdcQryInvestorProductGroupMarginField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryInvestorProductGroupMargin(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryInvestorProductGroupMargin():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryInvestorProductGroupMargin():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryInvestorProductGroupMargin():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryEWarrantOffset')
def test_QryEWarrantOffset():
    '''
    测试QryEWarrantOffset
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryEWarrantOffset():开始'
    sleep(1)

    data = CThostFtdcQryEWarrantOffsetField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryEWarrantOffset(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryEWarrantOffset():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryEWarrantOffset():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryEWarrantOffset():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryDepthMarketData')
def test_QryDepthMarketData():
    '''
    测试QryDepthMarketData
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryDepthMarketData():开始'
    sleep(1)

    data = CThostFtdcQryDepthMarketDataField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryDepthMarketData(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryDepthMarketData():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryDepthMarketData():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryDepthMarketData():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryTransferBank')
def test_QryTransferBank():
    '''
    测试QryTransferBank
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryTransferBank():开始'
    sleep(1)

    data = CThostFtdcQryTransferBankField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryTransferBank(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryTransferBank():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryTransferBank():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryTransferBank():执行结束'
    print '----------------------------------------------------------------------'






@attr('QueryApi')
@attr('QryProduct')
def test_QryProduct():
    '''
    测试QryProduct
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryProduct():开始'
    sleep(1)

    data = CThostFtdcQryProductField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryProduct(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryProduct():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryProduct():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryProduct():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryTradingCode')
def test_QryTradingCode():
    '''
    测试QryTradingCode
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryTradingCode():开始'
    sleep(1)

    data = CThostFtdcQryTradingCodeField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryTradingCode(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryTradingCode():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryTradingCode():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryTradingCode():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QrySettlementInfo')
def test_QrySettlementInfo():
    '''
    测试QrySettlementInfo
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QrySettlementInfo():开始'
    sleep(1)

    data = CThostFtdcQrySettlementInfoField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QrySettlementInfo(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QrySettlementInfo():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QrySettlementInfo():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QrySettlementInfo():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryAccountregister')
def test_QryAccountregister():
    '''
    测试QryAccountregister
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryAccountregister():开始'
    sleep(1)

    data = CThostFtdcQryAccountregisterField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryAccountregister(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryAccountregister():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryAccountregister():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryAccountregister():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryParkedOrder')
def test_QryParkedOrder():
    '''
    测试QryParkedOrder
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryParkedOrder():开始'
    sleep(1)

    data = CThostFtdcQryParkedOrderField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryParkedOrder(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryParkedOrder():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryParkedOrder():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryParkedOrder():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryTransferSerial')
def test_QryTransferSerial():
    '''
    测试QryTransferSerial
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryTransferSerial():开始'
    sleep(1)

    data = CThostFtdcQryTransferSerialField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryTransferSerial(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryTransferSerial():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryTransferSerial():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryTransferSerial():执行结束'
    print '----------------------------------------------------------------------'




@attr('QueryApi')
@attr('QryContractBank')
def test_QryContractBank():
    '''
    测试QryContractBank
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_QryContractBank():开始'
    sleep(1)

    data = CThostFtdcQryContractBankField()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.QryContractBank(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_QryContractBank():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_QryContractBank():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_QryContractBank():执行结束'
    print '----------------------------------------------------------------------'



