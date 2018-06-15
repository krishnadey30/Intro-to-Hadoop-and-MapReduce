#!/usr/bin/python

# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
import sys
for row in sys.stdin:
	data = row.strip().split(" ")
	if len(data)==10:
		ip, identity, username, date, tz, method, page, http_version, status, content_size = data
		print "{0}\t{1}".format(page,1)