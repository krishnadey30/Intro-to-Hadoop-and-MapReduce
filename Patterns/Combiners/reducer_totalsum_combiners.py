#!/usr/bin/python

import sys

TotalSales = 0
oldDay=None
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisDay, thisSale = data_mapped
    if oldDay and oldDay!=thisDay:
    	print "{0}\t{1}".format(oldDay,TotalSales)
    	oldDay=thisDay
    	TotalSales=0
    oldDay=thisDay
    TotalSales+=float(thisSale)
if oldDay!=None:
    print "{0}\t{1}".format(oldDay,TotalSales)
