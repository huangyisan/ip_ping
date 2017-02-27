#!/usr/bin/env python
import etcd
import socket

def get_external_ip():
	localIP = socket.gethostbyname(socket.gethostname())
	ipList = socket.gethostbyname_ex(socket.gethostname())[-1]
	for ip in ipList:
		if ip != localIP:
			return ip

get_external_ip()
