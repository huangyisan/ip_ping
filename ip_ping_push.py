#!/usr/bin/env python
import etcd
import socket

def get_external_ip():
	localIP = socket.gethostbyname(socket.gethostname())
	ipList = socket.gethostbyname_ex(socket.gethostname())[-1]
	for ip in ipList:
		if ip != localIP:
			return ip

def get_hostname():
	hostname = socket.gethostname()
	return hostname

def create_etcd_client():
	global client
	client = etcd.Client(host='192.168.174.130',port=2379)
	
def add_etcd_data():
	client.write("/nodes/"+get_hostname(),get_external_ip(),ttl=90)	

def get_etcd_data():
	data=client.read('/nodes/'+get_hostname(),recursive=True, sorted=True)
	for i in data.children:
		print i.value

	
get_external_ip()
get_hostname()
create_etcd_client()
add_etcd_data()
get_etcd_data()
