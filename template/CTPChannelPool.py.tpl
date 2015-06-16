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


{% for method in reqMethodDict.itervalues() %}
    {% set parameter = method['parameters'][0]  %}
    def {{ method['name'][3:]}}(self,data):
        '''
        {{ method['remark'][3:] }}
        data 调用api需要填写参数表单,类型为{{parameter['raw_type']}},具体参见其定义文件
        返回信息格式[errorID,errorMsg,responseData=[...]]
        注意:同步调用没有metaData参数,因为没有意义
        '''
        channel = self.getMinWaitChannel()
        return channel.{{ method['name'][3:]}}(data)

{% endfor %}
