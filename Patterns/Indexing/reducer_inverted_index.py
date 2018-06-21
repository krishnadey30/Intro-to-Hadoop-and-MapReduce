#!/usr/bin/python

import sys
l=[]
oldword = None
count = 0
for row in sys.stdin:
	data=row.strip().split('\t')
	if len(data)!=2:
		continue
	thisword,thisnode=data
	if oldword and oldword!=thisword:
		l=sorted(l,key=lambda x:int(x))
		print "{0}\t{1}\t{2}".format(oldword,count,','.join(l))
		oldword=thisword
		count=0
		l=[]
	oldword=thisword
	count+=1
	l.append(thisnode)

if oldword!=None:
	l=sorted(l,key=lambda x:int(x))
	print "{0}\t{1}\t{2}".format(oldword,count,','.join(l))
