#!/usr/bin/env python
import etcd



def create_etcd_client():
	global client
	client = etcd.Client(host='192.168.174.130',port=2379)

def get_etcd_data():
	data=client.read('/nodes/'+get_hostname(),recursive=True, sorted=True)
	for i in data.children:
		print i.value

create_etcd_client()	
get_etcd_data()
