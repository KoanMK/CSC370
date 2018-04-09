# create_courses.py
# CSC 370 - Spring 2018 - Starter code for Assignment 4
# Nigel Decontie
# V00853112

import sys, csv, psycopg2

psql_user = 'nigeld' #Change this to your username
psql_db = 'nigeld' #Change this to your personal DB name
psql_password = 'admin' #Put your password (as a string) here
psql_server = 'studdb2.csc.uvic.ca'
psql_port = 5432
 
conn = psycopg2.connect(dbname=psql_db,user=psql_user,password=psql_password,host=psql_server,port=psql_port)

if len(sys.argv) < 2:
	print("Usage: %s <input file>",file=sys.stderr)
	sys.exit(0)
	
input_filename = sys.argv[1]

# Open your DB connection here

with open(input_filename) as f:
	for row in csv.reader(f):
		if len(row) == 0:
			continue #Ignore blank rows
		if len(row) < 4:
			print("Error: Invalid input line \"%s\""%(','.join(row)), file=sys.stderr)
			#Maybe abort the active transaction and roll back at this point?
			break
		code, name, term, instructor, capacity = row[0:5]
		prerequisites = row[5:] #List of zero or more items
		
		#Do something with the data here
		#Make sure to catch any exceptions that occur and roll back the transaction if a database error occurs.

		
		
