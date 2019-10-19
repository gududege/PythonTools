#!/usr/bin/env python
#coding=utf-8
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkalidns.request.v20150109.DescribeDomainRecordsRequest import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109.UpdateDomainRecordRequest import UpdateDomainRecordRequest
import json
import requests
import re

client = AcsClient(' ', ' ', 'cn-hangzhou')
domainname = 'insert your ddns domain name'
tagetrecord = 'insert you A record'

def getCurrentIp() -> str:
    try:
        taobaoInterface = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=myip', timeout = 1)
        ip = taobaoInterface.json()['data']['ip'] if taobaoInterface.status_code == 200 else ''
    except Exception as e:
        souhuInterface = requests.get('http://pv.sohu.com/cityjson?ie=utf-8',  timeout = 1)
        if souhuInterface.status_code == 200:
            ip = re.search(r'(((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3})', souhuInterface.text)
            ip = ip.group()      
    return ip

def getRecordList(Domain : str) -> list:
    request = DescribeDomainRecordsRequest()
    request.set_accept_format('json')
    request.set_DomainName(Domain)
    response = client.do_action_with_exception(request)
    recordList = json.loads(str(response, encoding='utf-8'))["DomainRecords"]["Record"]
    # python2:  print(response) 
    return recordList

def getTargetRecordInfoFromList(TargetName : str, RecordList : list):
    for record in RecordList:
        if record['RR'] == TargetName:
            return (record['RecordId'], record['Value'])
    return ''

def updateRecord(RecordId : str, RR : str, Type : str, Value : str) -> str:
    request = UpdateDomainRecordRequest()
    request.set_accept_format('json')
    request.set_Value(Value)
    request.set_Type(Type)
    request.set_RR(RR)
    request.set_RecordId(RecordId)
    response = client.do_action_with_exception(request)
    return str(response, encoding='utf-8')

if __name__ == "__main__":
    #  print(getTargetRecordInfoFromList(tagetrecord,  getRecordList(domainname))) 
    recordInfo = getTargetRecordInfoFromList(tagetrecord,  getRecordList(domainname))
    currentRecordIP = recordInfo[1]
    currentNASIP = getCurrentIp()
    if currentNASIP != currentRecordIP:
        recordID = recordInfo[0]
        resp = updateRecord(recordID, tagetrecord, 'A', currentNASIP)
        print(resp)
    else:
        print('No need to update')
    
