# report_classlist.py
# CSC 370 - Spring 2018 - Starter code for Assignment 4
#
# Nigel Decontie
# V00853112
#
# The code below generates a mockup of the output of report_classlist.py
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

def print_header(course_code, course_name, term, instructor_name):
	print("Class list for %s (%s)"%(str(course_code), str(course_name)) )
	print("  Term %s"%(str(term), ) )
	print("  Instructor: %s"%(str(instructor_name), ) )
	
def print_row(student_id, student_name, grade):
	if grade is not None:
		print("%10s %-25s   GRADE: %s"%(str(student_id), str(student_name), str(grade)) )
	else:
		print("%10s %-25s"%(str(student_id), str(student_name),) )

def print_footer(total_enrolled, max_capacity):
	print("%s/%s students enrolled"%(str(total_enrolled),str(max_capacity)) )

if len(sys.argv) < 3:
	print('Usage: %s <course code> <term>'%sys.argv[0], file=sys.stderr)
	sys.exit(0)
	
course_code, term = sys.argv[1:3]

conn = psycopg2.connect(dbname=psql_db,user=psql_user,password=psql_password,host=psql_server,port=psql_port)
cursor = conn.cursor()

# Queries
cursor.execute("select name, instructor_name from course_offerings where code = %s and term_code = %s;", [course_code, term])
table = cursor.fetchall()
args = []
for row in table:
	for item in row:
		args.append(item)
print_header(course_code, args[0], term, args[1])

cursor.execute("select student_id, name, grade from enrollment natural join students where code = %s and term_code = %s;", [course_code, term])
table = cursor.fetchall()
for row in table:
	print_row(*row)

#Print the last line (enrollment/max_capacity)
args = []
cursor.execute("select count(*) from enrollment where code = %s and term_code = %s;", [course_code, term])
table = cursor.fetchall()
for row in table:
	for item in row:
		args.append(item)

cursor.execute("select capacity from course_offerings where code = %s and term_code = %s;", [course_code, term])
table = cursor.fetchall()
for row in table:
	for item in row:
		args.append(item)

print_footer(*args)

cursor.close()
conn.close()