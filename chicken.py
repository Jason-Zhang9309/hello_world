# coding=UTF-8
"""
#百钱白鸡问题
#公鸡5元一只，母鸡3元1只，小鸡一元三只，100元买100只鸡，公鸡、母鸡、小鸡各买几只？
for x in range(0,20):
	for y in range(0,33):
		z = 100 -x - y
		if 5*x + 3*y + z/3 == 100 and z%3 == 0:
			print('公鸡：%d，母鸡：%d，小鸡：%d' %(x,y,z))

a = 0
b = 1
for _ in range(20):
	a,b = b,a+b
	print(a,end=' ')


import re

def main():
	username = input('请输入用户名： ')
	qq = input('请输入QQ号码： ')
	m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
	if not m1:
		print('请输入有效的用户名。')
	m2 = re.match(r'^[1-9]\d{4,11}$',qq)
	if not m2:
		print('请输入有效的QQ号。')
	if m1 and m2:
		print('你输入的信息有效！')

import re
def main():
	pattern = re.compile(r'(?<=\D)1[35789]\d{9}(?=\D)')
	sentence = '"我的身份证号码是1234567890123，手机号码是18210059762这个号码你记住了吗? 还有王大锤的手机号码是13411348076。"'
	mylist = re.findall(pattern,sentence)
	print(mylist)

	for temp in pattern.finditer(sentence):
		print(temp.group())

	m = pattern.search(sentence)
	while m:
		print(m.group())
		m = pattern.search(sentence,m.end())



#替换字符串中的不良内容

import re
def main():
	sentence = '你丫是傻逼吗？我操你大爷的。Fuck you！'
	purified = re.sub('[操逼艹]|fuck|shit|傻[逼比屄]|煞笔','*',sentence,flags=re.IGNORECASE)
	print(purified)
"""
import re
def main():
	poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
	sentence_list = re.split(r'[,.，。]',poem)
	while '' in sentence_list:
		sentence_list.remove('')
	print(sentence_list)

	for i in range(len(sentence_list)):
		print(sentence_list[i])
if __name__ == '__main__':
	main()
