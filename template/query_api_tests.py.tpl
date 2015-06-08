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

{% for method in reqMethodDict.itervalues() %}
{% if method['name'][3:6] == 'Qry' or method['name'][3:8] == 'Query' %}
{% set parameter = method['parameters'][0]  %}
@attr('QueryApi')
@attr('{{ method['name'][3:]}}')
def test_{{ method['name'][3:]}}():
    '''
    测试{{ method['name'][3:]}}
    '''
    global ch
    print ''
    print '----------------------------------------------------------------------'
    print u'test_{{ method['name'][3:]}}():开始'
    sleep(1)

    data = {{parameter['raw_type']}}()
    startTime = datetime.now()
    errorID,errorMsg,responeDataList =  ch.{{method['name'][3:]}}(data)
    endTime = datetime.now()
    timeDelta = endTime - startTime
    print u'test_{{ method['name'][3:]}}():请求共耗时%f秒' % timeDelta.total_seconds()

    if errorID == 0 :
        print u'共收到%d数据记录' % len(responeDataList)
        for i,responeData in enumerate(responeDataList):
            print '---------------------------------%d------------------------------------' % (i + 1)
            for k,v in responeData.toDict().iteritems():
                print k,'=',v,',',
            print ''
    else :
        print u'出错:','errorID=',errorID,'errorMsg=',errorMsg

    print u'test_{{ method['name'][3:]}}():请求完成'

    assert errorID == 0 or errorMsg== u'CTP:无此权限',u'请求失败'

    print u'test_{{ method['name'][3:]}}():执行结束'
    print '----------------------------------------------------------------------'
{% endif %}
{% endfor %}
