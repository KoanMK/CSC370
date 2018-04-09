# report_transcript.py
# CSC 370 - Spring 2018 - Starter code for Assignment 4
#
# The code below generates a mockup of the output of report_transcript.py
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

def print_header(student_id, student_name):
	print("Transcript for %s (%s)"%(str(student_id), str(student_name)) )
	
def print_row(course_term, course_code, course_name, grade):
	if grade is not None:
		print("%6s %10s %-35s   GRADE: %s"%(str(course_term), str(course_code), str(course_name), str(grade)) )
	else:
		print("%6s %10s %-35s   (NO GRADE ASSIGNED)"%(str(course_term), str(course_code), str(course_name)) )

if len(sys.argv) < 2:
	print('Usage: %s <student id>'%sys.argv[0], file=sys.stderr)
	sys.exit(0)
	
student_id = sys.argv[1]

conn = psycopg2.connect(dbname=psql_db,user=psql_user,password=psql_password,host=psql_server,port=psql_port)
cursor = conn.cursor()

# Mockup: Print a transcript for V00123456 (Rebecca Raspberry)
# student_id = 'V00123456'
# student_name = 'Rebecca Raspberry'
# print_header(student_id, student_name)

cursor.execute("select name from students where student_id = %s;", [student_id])
table = cursor.fetchall()
for row in table:
	for item in row:
		student_name = item
print_header(student_id, student_name)


# print_row(201709,'CSC 110','Fundamentals of Programming: I', 90)
# print_row(201709,'CSC 187','Recursive Algorithm Design', None) #The special value None is used to indicate that no grade is assigned.
# print_row(201801,'CSC 115','Fundamentals of Programming: II', 75)

cursor.close()
conn.close()