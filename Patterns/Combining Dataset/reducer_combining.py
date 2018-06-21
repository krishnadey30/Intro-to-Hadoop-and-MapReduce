#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
user_detail={}
post_detail=[]
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if data_mapped[1]=="B":
        post_detail.append(data_mapped)
    if data_mapped[1]=="A":
        user_detail[data_mapped[0]]=data_mapped
    
for x in post_detail:
    for a in x:
        if a!="B":
            print a,"\t",
    for i,a in enumerate(user_detail[x[0]]):
        if i > 1:
            print a,"\t",
    print
