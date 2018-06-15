#!/usr/bin/python

# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
import sys
count = 0
oldIp = None
for row in sys.stdin:
	data=row.strip().split('\t')
	if len(data)!=2:
		continue
	thisIp,thisCount=data
	if oldIp and oldIp!=thisIp:
		print "{0}\t{1}".format(oldIp,count)
		oldIp=thisIp
		count=0
	oldIp=thisIp
	count+=1

if oldIp!=None:
	print "{0}\t{1}".format(oldIp,count)