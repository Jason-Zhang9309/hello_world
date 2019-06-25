# coding=UTF-8
#排序算法-冒泡排序、选择排序、归并排序、快速排序

"""
冒泡排序-O(n**2)：两两比较，大的下沉

35,97,48,55,23,68,74,80
35,48,55,23,68,74,80,[97]
35,48,55,23,68,74,[80]
35,48,55,23,68,[74]
35,48,55,23,[68]
35,48,23,[55]
35,23,[48]
...
"""
# 函数设计要尽量做到无副作用（不影响使用者）
# *前面的叫位置参数，传递参数时只需要对号入座即可
# *后面的叫命名关键字参数，传递参数时必须给出参数名和参数值
# *args-可变参数-元组
# **kwargs-关键字参数-字典
#优化一（判断对象有序，提前结束循环）
#优化二（解'>'的耦合，扩大函数使用范围）
#优化三（创建函数对象，避免对调用函数对象的修改）
#优化四（搅拌排序）
def bubble_sort(origin_items,*,comp=lambda x,y:x>y):
	#将原始的数据列表复制到items，排序后不影响原数据
	items = origin_items[:]
	for i in range(1,len(items)):
		swapped = False
		for j in range(i-1,len(items)-i):
			if comp(items[j],items[j+1]):
				items[j],items[j+1] = items[j+1],items[j]
				swapped = True
		if swapped:
			swapped = False
			for j in range(len(items)-i-1,i-1,-1):
				if comp(items[j-1],items[j]):
					items[j],items[j-1] = items[j-1],items[j]
					swapped = True
		if not swapped:
			break
	return items
				
	
# 选择排序-O(n**2)每次从剩下的元素中选最小的
def select_sort(origin_items,comp=lambda x,y:x<y):
	items = origin_items[:]
	for i in range(len(items)-1):
		min_index = i
		for j in range(i+1,len(items)):
			if comp(items[j],items[min_index]):
				min_index = j
		items[i],items[min_index] = items[min_index],items[i]
	return items

#归并排序-O(n*log_2 n)-高级排序算法
def merge_sort(items,comp=lambda x,y:x<=y):
	"""拆分"""
	if len(items)<2:
		return items[:]
	mid = len(items)//2
	left = merge_sort(items[:mid],comp)
	right = merge_sort(items[mid:],comp)
	return merge(left,right,comp)

def merge(items1,items2,comp):
	"""合并（将两个有序的列表合成一个有序的列表"""
	items = []
	index1,index2 = 0,0
	while index1 < len(items1) and index2 < len(items2):
		if comp(items1[index1],items2[index2]):
			items.append(items1[index1])
			index1 += 1
		else:
			items.append(items2[index2])
			index2 += 1
	items += items1[index1:]
	items += items2[index2:]
	return items

#快速排序-以枢轴为界讲列表中的元素分为两部分，左边的都比枢轴小，右边的都比枢轴大

def quick_sort(origin_items,comp=lambda x,y:x<=y):
	items = origin_items
	_quick_sort(items,0,len(items)-1,comp)
	return items

def _quick_sort(items,start,end,comp):
	"""递归调用划分和排序"""
	if start < end:
		pos = _partition(items,start,end,comp)
		_quick_sort(items,start,pos-1,comp)
		_quick_sort(items,pos+1,end,comp)

def _partition(items,start,end,comp):
	"""划分"""
	pivot = items[end]
	i = start -1
	for j in range(start,end):
		if comp(items[j],pivot):
			i += 1
			items[i],items[j] = items[j],items[i]
	items[i+1],items[end] = items[end],items[i+1]
	return(i+1)
"""
class Person(object):
	
	def __init__(self,name, age):
		self.name = name
		self.age = age
	def __str__(self):

		return(f'{self.name}:{self.age}')

	def __repr__(self):
		return self.__str__
"""
def main():
	items = [35,97,48,55,23,68,74,80]
	#冒泡排序
	print(bubble_sort(items))
	#选择排序
	print(select_sort(items))
	#归并排序
	print(merge_sort(items))
	#快速排序
	print(quick_sort(items))
"""
	items2 = [Person('Wang',25),Person('Zhang',27),Person('Luo',30),Person('He',50)]
	print(bubble_sort(items2))
	print(select_sort(items2))
	print(merge_sort(items2))
	print(quick_sort(items2))

	print(quick_sort(items2,comp=lambda p1,p2 p1.age<=p2.age))

	items3 = ['apple','orange','watermelon','durian','pear']
	print(bubble_sort(items3))
	print(select_sort(items3))
	print(merge_sort(items3))
	print(quick_sort(items3))
"""
if __name__ == '__main__':
	main()
