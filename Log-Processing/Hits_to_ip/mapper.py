#!/usr/bin/python

import sys
for row in sys.stdin:
	data = row.strip().split(" ")
	if len(data)==10:
		ip, identity, username, date, tz, method, page, http_version, status, content_size = data
		print "{0}\t{1}".format(ip,1)