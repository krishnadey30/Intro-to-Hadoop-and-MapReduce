#!/usr/bin/python

import sys

oldCategory= None
totalSales = 0

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
    thisCategory, thisSale = data_mapped

    if oldCategory and oldCategory!=thisCategory:
    	print "{0}\t{1}".format(oldCategory,totalSales)
    	totalSales = 0
    	oldCategory = thisCategory

    oldCategory = thisCategory
    totalSales+=float(thisSale)

if oldCategory!=None:
	print "{0}\t{1}".format(oldCategory,totalSales)
