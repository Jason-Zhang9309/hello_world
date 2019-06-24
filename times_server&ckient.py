# coding=UTF-8
from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime

def main():
	server = socket(family=AF_INET,type=SOCK_STREAM)
	server.bind(('127.0.0.1',6789))
	server.listen(512)
	print('服务器启动开始监听...')
	while True:
		client,addr = server.accept()
		print(str(addr)+'连接到了服务器.')
		client.send(str(datetime.now()).encode('utf-8'))
		client.close()

if __name__ == '__main__':
	main()
  
  
 from socket import socket

def main():
	client = socket()

	client.connect(('127.0.0.1',6789))
	print(client.recv(1024).decode('utf-8'))
	client.close()

if __name__ == '__main__':
	main()
