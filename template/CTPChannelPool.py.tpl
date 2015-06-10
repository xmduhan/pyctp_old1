# -*- coding: utf-8 -*-

class TraderChannelPool:
    '''
    用于解决ctp trader api查询流量控制(每秒1次)的问题,它将创建多个通道,将不同的请求分到不同
    的通道中去执行,突破ctp trader api的流量控制限制.
    目前还不清楚ctp正式环境账号多次登录是否可行,该方法是否可能需要进一步验证
    '''
    def __init__(self,frontAddress,brokerID,userID,password,nChannel=2,fileOutput='/dev/null'):
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
            traderPool = TraderChannel(frontAddress,brokerID,userID,password,fileOutput=fileOutput)
            pool.append(traderPool)

    
