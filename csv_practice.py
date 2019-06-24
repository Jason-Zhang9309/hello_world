import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	#print(header_row)
	"""
	for index,column_header in enumerate(header_row):
		print(index,column_header)
	"""

	dates,hights,lows = [],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],"%Y-%m-%d")
			
			high = int(row[1])
			low = int(row[3])
			
		except ValueError:
			print current_date,'miss'
		else:
			dates.append(current_date)
			hights.append(high)
			lows.append(low)
	

	
	

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates,hights,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,hights,lows,facecolor='green',alpha=0.1)
plt.title("Daily high and low temperatures- 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
