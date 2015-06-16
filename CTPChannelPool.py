# -*- coding: utf-8 -*-

from CTPChannel import TraderChannel


class TraderChannelPool:
    '''
    用于解决ctp trader api查询流量控制(每秒1次)的问题,它将创建多个通道,将不同的请求分到不同
    的通道中去执行,突破ctp trader api的流量控制限制.
    目前还不清楚ctp正式环境账号多次登录是否可行,该方法是否可能需要进一步验证
    '''
    def __init__(self,frontAddress,brokerID,userID,password,nChannel=2,
        fileOutput='/dev/null',queryInterval=1):
        '''
        参数:
        frontAddress   ctp服务器地址
        brokerID   代理商编号
        userID   用户编号
        password   密码
        nChannel   要建立的通道数,默认情况下为2
        fileOutput   ctp trader通讯进程的日志信息的保存路径,默认抛弃('/dev/null')
        '''
        self.pool = []
        for i in range(nChannel):
            traderPool = TraderChannel(frontAddress,brokerID,userID,password,
                fileOutput=fileOutput,queryInterval=queryInterval)
            self.pool.append(traderPool)


    def getQueryWaitTime(self):
        '''
        获取查询需要等待的时间
        '''
        return min([ch.getQueryWaitTime() for ch in self.pool])

    def getMinWaitChannel(self):
        '''
        获取需要等待时间最短的通道
        '''
        waitTimeList = [ch.getQueryWaitTime() for ch in self.pool]
        i = waitTimeList.index(min(waitTimeList))
        return self.pool[i]



    
    def QryTradingAccount(self,data):
        '''
        请求查询资金账户
        data 调用api需要填写参数表单,类型为CThostFtdcQryTradingAccountField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryTradingAccount(data)


    
    def QryCFMMCTradingAccountKey(self,data):
        '''
        请求查询保证金监管系统经纪公司资金账户密钥
        data 调用api需要填写参数表单,类型为CThostFtdcQryCFMMCTradingAccountKeyField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryCFMMCTradingAccountKey(data)


    
    def UserPasswordUpdate(self,data):
        '''
        用户口令更新请求
        data 调用api需要填写参数表单,类型为CThostFtdcUserPasswordUpdateField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.UserPasswordUpdate(data)


    
    def QryTradingNotice(self,data):
        '''
        请求查询交易通知
        data 调用api需要填写参数表单,类型为CThostFtdcQryTradingNoticeField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryTradingNotice(data)


    
    def QryTrade(self,data):
        '''
        请求查询成交
        data 调用api需要填写参数表单,类型为CThostFtdcQryTradeField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryTrade(data)


    
    def QueryMaxOrderVolume(self,data):
        '''
        查询最大报单数量请求
        data 调用api需要填写参数表单,类型为CThostFtdcQueryMaxOrderVolumeField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QueryMaxOrderVolume(data)


    
    def SettlementInfoConfirm(self,data):
        '''
        投资者结算结果确认
        data 调用api需要填写参数表单,类型为CThostFtdcSettlementInfoConfirmField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.SettlementInfoConfirm(data)


    
    def QryInvestorPosition(self,data):
        '''
        请求查询投资者持仓
        data 调用api需要填写参数表单,类型为CThostFtdcQryInvestorPositionField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryInvestorPosition(data)


    
    def QryBrokerTradingAlgos(self,data):
        '''
        请求查询经纪公司交易算法
        data 调用api需要填写参数表单,类型为CThostFtdcQryBrokerTradingAlgosField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryBrokerTradingAlgos(data)


    
    def QryOrder(self,data):
        '''
        请求查询报单
        data 调用api需要填写参数表单,类型为CThostFtdcQryOrderField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryOrder(data)


    
    def QryExchange(self,data):
        '''
        请求查询交易所
        data 调用api需要填写参数表单,类型为CThostFtdcQryExchangeField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryExchange(data)


    
    def UserLogin(self,data):
        '''
        用户登录请求
        data 调用api需要填写参数表单,类型为CThostFtdcReqUserLoginField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.UserLogin(data)


    
    def FromFutureToBankByFuture(self,data):
        '''
        期货发起期货资金转银行请求
        data 调用api需要填写参数表单,类型为CThostFtdcReqTransferField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.FromFutureToBankByFuture(data)


    
    def QryExchangeRate(self,data):
        '''
        请求查询汇率
        data 调用api需要填写参数表单,类型为CThostFtdcQryExchangeRateField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryExchangeRate(data)


    
    def QryInvestorPositionDetail(self,data):
        '''
        请求查询投资者持仓明细
        data 调用api需要填写参数表单,类型为CThostFtdcQryInvestorPositionDetailField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryInvestorPositionDetail(data)


    
    def QrySettlementInfoConfirm(self,data):
        '''
        请求查询结算信息确认
        data 调用api需要填写参数表单,类型为CThostFtdcQrySettlementInfoConfirmField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QrySettlementInfoConfirm(data)


    
    def QryBrokerTradingParams(self,data):
        '''
        请求查询经纪公司交易参数
        data 调用api需要填写参数表单,类型为CThostFtdcQryBrokerTradingParamsField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryBrokerTradingParams(data)


    
    def QueryCFMMCTradingAccountToken(self,data):
        '''
        请求查询监控中心用户令牌
        data 调用api需要填写参数表单,类型为CThostFtdcQueryCFMMCTradingAccountTokenField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QueryCFMMCTradingAccountToken(data)


    
    def QryNotice(self,data):
        '''
        请求查询客户通知
        data 调用api需要填写参数表单,类型为CThostFtdcQryNoticeField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryNotice(data)


    
    def FromBankToFutureByFuture(self,data):
        '''
        期货发起银行资金转期货请求
        data 调用api需要填写参数表单,类型为CThostFtdcReqTransferField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.FromBankToFutureByFuture(data)


    
    def ParkedOrderInsert(self,data):
        '''
        预埋单录入请求
        data 调用api需要填写参数表单,类型为CThostFtdcParkedOrderField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.ParkedOrderInsert(data)


    
    def QryInvestorPositionCombineDetail(self,data):
        '''
        请求查询投资者持仓明细
        data 调用api需要填写参数表单,类型为CThostFtdcQryInvestorPositionCombineDetailField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryInvestorPositionCombineDetail(data)


    
    def OrderInsert(self,data):
        '''
        报单录入请求
        data 调用api需要填写参数表单,类型为CThostFtdcInputOrderField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.OrderInsert(data)


    
    def QrySecAgentACIDMap(self,data):
        '''
        请求查询二级代理操作员银期权限
        data 调用api需要填写参数表单,类型为CThostFtdcQrySecAgentACIDMapField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QrySecAgentACIDMap(data)


    
    def ParkedOrderAction(self,data):
        '''
        预埋撤单录入请求
        data 调用api需要填写参数表单,类型为CThostFtdcParkedOrderActionField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.ParkedOrderAction(data)


    
    def QueryBankAccountMoneyByFuture(self,data):
        '''
        期货发起查询银行余额请求
        data 调用api需要填写参数表单,类型为CThostFtdcReqQueryAccountField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QueryBankAccountMoneyByFuture(data)


    
    def QryParkedOrderAction(self,data):
        '''
        请求查询预埋撤单
        data 调用api需要填写参数表单,类型为CThostFtdcQryParkedOrderActionField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryParkedOrderAction(data)


    
    def Authenticate(self,data):
        '''
        客户端认证请求
        data 调用api需要填写参数表单,类型为CThostFtdcReqAuthenticateField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.Authenticate(data)


    
    def QryExchangeMarginRate(self,data):
        '''
        请求查询交易所保证金率
        data 调用api需要填写参数表单,类型为CThostFtdcQryExchangeMarginRateField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryExchangeMarginRate(data)


    
    def TradingAccountPasswordUpdate(self,data):
        '''
        资金账户口令更新请求
        data 调用api需要填写参数表单,类型为CThostFtdcTradingAccountPasswordUpdateField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.TradingAccountPasswordUpdate(data)


    
    def UserLogout(self,data):
        '''
        登出请求
        data 调用api需要填写参数表单,类型为CThostFtdcUserLogoutField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.UserLogout(data)


    
    def QryInstrument(self,data):
        '''
        请求查询合约
        data 调用api需要填写参数表单,类型为CThostFtdcQryInstrumentField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryInstrument(data)


    
    def OrderAction(self,data):
        '''
        报单操作请求
        data 调用api需要填写参数表单,类型为CThostFtdcInputOrderActionField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.OrderAction(data)


    
    def QryInstrumentCommissionRate(self,data):
        '''
        请求查询合约手续费率
        data 调用api需要填写参数表单,类型为CThostFtdcQryInstrumentCommissionRateField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryInstrumentCommissionRate(data)


    
    def QryInstrumentMarginRate(self,data):
        '''
        请求查询合约保证金率
        data 调用api需要填写参数表单,类型为CThostFtdcQryInstrumentMarginRateField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryInstrumentMarginRate(data)


    
    def QryInvestor(self,data):
        '''
        请求查询投资者
        data 调用api需要填写参数表单,类型为CThostFtdcQryInvestorField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryInvestor(data)


    
    def QryExchangeMarginRateAdjust(self,data):
        '''
        请求查询交易所调整保证金率
        data 调用api需要填写参数表单,类型为CThostFtdcQryExchangeMarginRateAdjustField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryExchangeMarginRateAdjust(data)


    
    def QryInvestorProductGroupMargin(self,data):
        '''
        请求查询投资者品种/跨品种保证金
        data 调用api需要填写参数表单,类型为CThostFtdcQryInvestorProductGroupMarginField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryInvestorProductGroupMargin(data)


    
    def QryEWarrantOffset(self,data):
        '''
        请求查询仓单折抵信息
        data 调用api需要填写参数表单,类型为CThostFtdcQryEWarrantOffsetField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryEWarrantOffset(data)


    
    def QryDepthMarketData(self,data):
        '''
        请求查询行情
        data 调用api需要填写参数表单,类型为CThostFtdcQryDepthMarketDataField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryDepthMarketData(data)


    
    def QryTransferBank(self,data):
        '''
        请求查询转帐银行
        data 调用api需要填写参数表单,类型为CThostFtdcQryTransferBankField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryTransferBank(data)


    
    def RemoveParkedOrderAction(self,data):
        '''
        请求删除预埋撤单
        data 调用api需要填写参数表单,类型为CThostFtdcRemoveParkedOrderActionField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.RemoveParkedOrderAction(data)


    
    def QryProduct(self,data):
        '''
        请求查询产品
        data 调用api需要填写参数表单,类型为CThostFtdcQryProductField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryProduct(data)


    
    def QryTradingCode(self,data):
        '''
        请求查询交易编码
        data 调用api需要填写参数表单,类型为CThostFtdcQryTradingCodeField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryTradingCode(data)


    
    def QrySettlementInfo(self,data):
        '''
        请求查询投资者结算结果
        data 调用api需要填写参数表单,类型为CThostFtdcQrySettlementInfoField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QrySettlementInfo(data)


    
    def QryAccountregister(self,data):
        '''
        请求查询银期签约关系
        data 调用api需要填写参数表单,类型为CThostFtdcQryAccountregisterField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryAccountregister(data)


    
    def QryParkedOrder(self,data):
        '''
        请求查询预埋单
        data 调用api需要填写参数表单,类型为CThostFtdcQryParkedOrderField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryParkedOrder(data)


    
    def QryTransferSerial(self,data):
        '''
        请求查询转帐流水
        data 调用api需要填写参数表单,类型为CThostFtdcQryTransferSerialField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryTransferSerial(data)


    
    def QryContractBank(self,data):
        '''
        请求查询签约银行
        data 调用api需要填写参数表单,类型为CThostFtdcQryContractBankField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.QryContractBank(data)


    
    def RemoveParkedOrder(self,data):
        '''
        请求删除预埋单
        data 调用api需要填写参数表单,类型为CThostFtdcRemoveParkedOrderField,具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.RemoveParkedOrder(data)

