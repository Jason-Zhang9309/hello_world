# coding=UTF-8
#使用多进程和不使用多进程的差别
"""
#不使用多进程
from random import randint
from time import time,sleep

def download_task(filename):
	print('开始下载%s...'%filename)
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s下载完成，耗时%d秒。'%(filename,time_to_download))

def main():
	start_time = time()
	download_task('python从入门到住院.pdf')
	download_task('Tokyo Hot.avi')
	end_time = time()
	print('总耗时%f秒'%( end_time - start_time))

if __name__ == '__main__':
	main()

#使用多进程
from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
	print('启动下载进程，进程号[%d].'%getpid())
	print('开始下载%s...'%filename)
	time_to_download = randint(5,10)
	sleep(time_to_download)
	print('%s下载完成，耗时%d秒。'%(filename,time_to_download))

def main():
	start_time = time()
	p1 = Process(target=download_task,args=('python从入门到住院.pdf',))
	p1.start()
	p2 = Process(target=download_task,args=('Tokyo Hot.avi',))
	p2.start()
	p1.join()
	p2.join()
	end_time = time()
	print('总耗时%f秒'%( end_time - start_time))

if __name__ == '__main__':
	main()


#两个进程一个人输出ping，一个输出pong，一共输出10个，Queue是一个共享队列
from multiprocessing import Process,Queue
from time import sleep

def sub_task(string,counts):
	
	while counts.qsize() < 10:
		print(string,end=' ',flush=True)
		counts.put(1)
		sleep(0.01)
def main():
	counts = Queue()
	Process(target=sub_task,args=('Ping',counts)).start()
	Process(target=sub_task,args=('pong',counts)).start()

if __name__ == '__main__':
	main()
"""
from time import sleep
from threading import Thread,Lock

class Account(object):
	"""docstring for ClassName"""
	def __init__(self):
		self._balance = 0
		self._lock = Lock()
	def deposit(self,money):
		#计算存款后的余额
		self._lock.acquire()
		try:
			new_balance = self._balance + money
			sleep(0.01)
			self._balance = new_balance
		finally:
			self._lock.release()

	@property
	def balance(self):
		return self._balance

class AddMoneyThread(Thread):
	"""docstring for AddMoneyThread"""
	def __init__(self, account,money):
		super().__init__()
		self._account = account
		self._money = money
	def run(self):
	 	self._account.deposit(self._money)

def main():
	account = Account()
	threads = []
	for _ in range(100):
		t = AddMoneyThread(account,1)
		threads.append(t)
		t.start()
	for t in threads:
		t.join()
	print('账户余额为￥%d元'%account.balance)

if __name__ == '__main__':
	main()
