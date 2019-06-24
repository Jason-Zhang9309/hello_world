# coding=UTF-8
import requests
import pygal
import math
import io

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
with open('btc_close_2017_requests.json','w') as f:
	f.write(req.text)
file_requests = req.json()
dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in file_requests:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))
	#print(dates[-1])
	#print("{} is month {} week {}, {}, the close price is {} RMB".format(date,month,week,weekday,close))

line_chart = pygal.Line(x_lable_rotation=20,show_minor_x_lables=False)
line_chart.title = u'收盘价（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
line_chart.add(u'收盘价',close)
line_chart.render_to_file('close_price.svg')

line_chart = pygal.Line(x_lable_rotation=20,show_minor_x_lables=False)
line_chart.title = u'收盘价对数变换（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add(u'log收盘价',close_log)
line_chart.render_to_file('close_log_price.svg')

with io.open('close_price_Dashboard.html','w',encoding='utf8') as html_file:
	html_file.write(u'<html><head><title>Dashboard</title><metacharset="utf-8"></head><body>\n')
	for svg in ['close_price.svg','close_log_price.svg']:
		html_file.write(u'<object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))
	html_file.write(u'</body></html>')
