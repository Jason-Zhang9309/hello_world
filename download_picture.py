# coding=UTF-8

from time import time
from threading import Thread
import requests

#继承Threa类自定义线程类
class DownloadHandler(Thread):
	
	def __init__(self, url):
		super().__init__()
		self.url = url

	def run(self):
		#rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
		filename = self.url[self.url.rfind('/')+1:]
		req = requests.get(self.url)
		with open('/usr/zhangjishu/meinvpicture/' + filename, 'wb') as f:
			f.write(req.content)

def main():
	req = requests.get('http://api.tianapi.com/meinv/?&&key=02a5a353598649e14bed0a8ff7f57b50&num=10')
	data_model = req.json()
	
	for mm_dict in data_model['newslist']:
		url = mm_dict['picUrl']
		print(url)
		DownloadHandler(url).start()
	
if __name__ == '__main__':
	main()


