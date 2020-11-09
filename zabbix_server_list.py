#coding:utf-8
#获取zabbix上所有主机的IP和主机名
import requests
import json
import csv
import time


def get_token():
    data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": username,
            "password": password
        },
        "id": 0
    }
    r = requests.get(zaurl, headers=header, data=json.dumps(data))
    auth = json.loads(r.text)
    return auth["result"]

def getHosts(token):
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host"
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]
        },
        "id": 2,
        "auth": token,

    }

    request = requests.post(zaurl, headers=header, data=json.dumps(data))
    dict = json.loads(request.content)
#    print (dict['result'])
    return dict['result']


if __name__ == "__main__":
    zaurl="http://zabbix.chumanapp.com/api_jsonrpc.php"
    header = {"Content-Type": "application/json"}
    username = "admin"
    password = "UE12RoxeZPpx9Opj"

    token = get_token()
    hostlist = getHosts(token)
    datafile = "zabbix.txt"
    fdata = open(datafile,'w')
    for i in hostlist:
        hostid = i['host']
        inter = i['interfaces']
        for j in inter:
            hostip = j['ip']
            #dict[host] = ip        
            fdata.write(hostip + ' ' + hostid + '\n')
    fdata.close()