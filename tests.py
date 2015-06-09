# -*- coding: utf-8 -*-
import os
from nose.plugins.attrib import attr

@attr('test01')
def test01():
    '''
    测试
    '''
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
    print ch.readMarketData(1000)
