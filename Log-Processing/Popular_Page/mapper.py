#!/usr/bin/python

import sys
for row in sys.stdin:
	data = row.strip().split(" ")
	if len(data)==10:
		ip, identity, username, date, tz, method, page, http_version, status, content_size = data
		page=page.replace("http://www.the-associates.co.uk","")
		print "{0}\t{1}".format(page,1)