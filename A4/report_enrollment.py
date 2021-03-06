# report_enrollment.py
# CSC 370 - Spring 2018 - Starter code for Assignment 4
#
# Nigel Decontie
# V00853112
#
# The code below generates a mockup of the output of report_enrollment.py
# as specified in the assignment. You can copy and paste the functions in this
# program into your solution to ensure the correct formatting.
#
# B. Bird - 02/26/2018

import psycopg2, sys

psql_user = 'nigeld' #Change this to your username
psql_db = 'nigeld' #Change this to your personal DB name
psql_password = 'admin' #Put your password (as a string) here
psql_server = 'studdb2.csc.uvic.ca'
psql_port = 5432

def print_row(term, course_code, course_name, instructor_name, total_enrollment, maximum_capacity):
	print("%6s %10s %-35s %-25s %s/%s"%(str(term), str(course_code), str(course_name), str(instructor_name), str(total_enrollment), str(maximum_capacity) ) )

conn = psycopg2.connect(dbname=psql_db,user=psql_user,password=psql_password,host=psql_server,port=psql_port)
cursor = conn.cursor()

cursor.execute("with T1 as (select count(*) as num, code, term_code from enrollment group by code, term_code order by term_code) select course_offerings.term_code, course_offerings.code, name, instructor_name, num, capacity from course_offerings left join T1 on course_offerings.term_code = T1.term_code and course_offerings.code = T1.code order by term_code;")
table = cursor.fetchall()
for row in table:
	argslist = []
	for item in row:
		if item == None:
			argslist.append(0)
		else:
			argslist.append(item)
	print_row(*argslist)

cursor.close()
conn.close()
