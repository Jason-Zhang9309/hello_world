from socket import socket,SOCK_STREAM,AF_INET
from base64 import b64encode 
from json import dumps
from threading import Thread


class FileTranserHandler(Thread):
	def __init__(self,cclient,filename,data):
		super().__init__()
		self.cclient = cclient
		self.data = data
		self.filename = filename

	def run(self):
		my_dict = {}
		my_dict['filename'] = self.filename
		my_dict['filedata'] = self.data
		json_str = dumps(my_dict)
		self.cclient.send(json_str.encode('utf-8'))
		self.cclient.close()

def main():


	server = socket()
	server.bind(('127.0.0.1',5566))
	server.listen(512)
	filename = 'l30l2enx35w.jpg'
	print('服务器启动开始监听...')

	with open(filename,'rb') as f:
		data = b64encode(f.read()).decode('utf-8')

	while True:
		client,addr = server.accept()
		FileTranserHandler(client,filename,data).start()

if __name__ == '__main__':
	main()
  
from socket import socket
from json import loads
from base64 import b64decode

def main():
	client = socket()
	client.connect(('127.0.0.1',5566))
	in_data = bytes()
	data = client.recv(1024)
	while data:
		in_data += data
		data = client.recv(1024)
	my_dict = loads(in_data.decode('utf-8'))
	filename = my_dict['filename']
	filedata = my_dict['filedata']
	print(filedata)
	with open('/usr/zhangjishu/pic_recv/' + filename,'wb') as f:
		f.write(b64decode(filedata))

	print('图片已保存.')

if __name__ == '__main__':
	main()
