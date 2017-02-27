#!/usr/bin/env python
import etcd
import json



def create_etcd_client():
	global client
	client = etcd.Client(host='192.168.174.130',port=2379)

def get_etcd_ip_data():
	data=client.read('/nodes',recursive=True, sorted=True)
	for i in data.children:
		dic = i.__dict__
		global hostname ip
		hostname=dic.get('key').split('/')[-1]
		ip=dic.get('value')

def ping_info_push():

create_etcd_client()	
get_etcd_ip_data()
