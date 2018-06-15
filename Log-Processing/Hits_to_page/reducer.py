#!/usr/bin/python

# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
import sys
count = 0
oldPage = None
for row in sys.stdin:
	data=row.strip().split('\t')
	if len(data)!=2:
		continue
	thisPage,thisCount=data
	if oldPage and oldPage!=thisPage:
		print "{0}\t{1}".format(oldPage,count)
		oldPage=thisPage
		count=0
	oldPage=thisPage
	count+=1

if oldPage!=None:
	print "{0}\t{1}".format(oldPage,count)