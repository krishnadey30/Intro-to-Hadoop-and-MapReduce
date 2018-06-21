#!/usr/bin/python

"""
Your goal for this task is to write mapper and reducer code 
that will combine some of the forum and user data. 
In relational algebra, this is known as a join operation. 
At the moment, this is not an auto-gradable exercise, but instructions below are given on how to test your code on your machine. 

The goal is to have the output from the reducer with the following fields for each forum post: 
"id"(1) "title"(2)  "tagnames"(3)  "author_id"(4)  "node_type" (6) "parent_id" (7) "abs_parent_id" (8) "added_at"(9) 
"score" (10) "reputation" (2) "gold"(3)  "silver" (4) "bronze"(5)
 
Note that for each post we have taken some of the information describing the post, 
and joined it with user information. The body of the post is not included in the final output. 
The reason is that it is difficult to handle a multiline body, as it might be split on separate 
lines during the intermediate steps Hadoop performs - shuffle and sort.   

$head -2 forum_users.tsv
"user_ptr_id"   "reputation"    "gold"  "silver"        "bronze"

$head -2 forum_node.tsv
"id"    "title" "tagnames"      "author_id"     "body"  "node_type"     "parent_id"     "abs_parent_id" "added_at"      "score" "state_string"  "last_edited_id"       "last_activity_by_id"    "last_activity_at"      "active_revision_id"    "extra" "extra_ref_id"  "extra_count"   "marked"

Your mapper code should take in records from both forum_node and forum_users. 
It needs to keep, for each record, those fields that are needed for the final output given above. 
In addition, mapper needs to add some text (e.g. "A" and "B") to mark where each output comes from 
(user information vs forum post information). Example output from mapper is:

"12345"  "A"  "11"  "3"  "4"  "1"
"12345"  "B"   "6336" "Unit 1: Same Value Q"  "cs101 value same"  "question"  "\N"  "\N"  "2012-02-25 08:09:06.787181+00"  "1" 
  
The first line originally comes from the forum_users input. It is from a student with user id: 12345 - the mapper key. 
The next field is the marker A specifying that the record comes from forum_users. 
What follows is the remaining information user information. 

The second line originally comes from the forum_node input. 
It also starts with the student id (mapper key) followed by a marker B and the information about the forum post.  
   
The mapper key for both types of records is the student ID: 
"user_ptr_id" from "forum_users" or  "author_id" from "forum_nodes" file. 
Remember that during the sort and shuffle phases records will be grouped based on the student ID (12345 in our example). 
You can use that to process and join the records appropriately in the reduce phase. 
"""

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line)==19 and line[3].isdigit():
            print line[3],"\t","B\t",line[0],"\t",line[1],"\t",line[2],"\t",line[5],"\t",line[6],"\t",line[7],"\t",line[8],"\t",line[9]
        elif len(line)==5 and line[0].isdigit():
            print line[0],"\t","A\t",line[1],"\t",line[2],"\t",line[3],"\t",line[4]

def main():
    mapper()

if __name__=="__main__":main()
        
