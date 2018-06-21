#!/usr/bin/python

import sys
import csv
import re
def mapper():
	reader=csv.reader(sys.stdin, delimiter='\t')
	for line in reader:
		nodeid=line[0]
		body = line[4]
		if nodeid.isdigit()==True:
			allwords = re.findall(r"[\w']+",body)
			allwords = map(lambda x: x.lower(),allwords)
			for word in allwords:
				print "{0}\t{1}".format(word,nodeid)

def main():
	mapper()


if __name__ =="__main__": main()
