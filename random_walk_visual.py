# coding=UTF-8

import matplotlib.pyplot as plt
from randomwalk import Randomwalk


while True:
	
	#创建一个Randomwalk实例，并将其包含的点绘制出来
	rw = Randomwalk()
	rw.fill_walk()

	#设置绘制窗口的尺寸
	plt.figure(figsize=(10,6))

	point_number = list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,edgecolor='none',s=1)

	#突出起点和终点
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)
	plt.show()

	keep_running = raw_input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
		
