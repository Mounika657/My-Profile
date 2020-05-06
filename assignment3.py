iBHubs

Home
AssignmentID - DB003
Submission Guidelines
Coding Guidelines
assignment_003.md

# Submission Guidelines
Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_003. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_003/
#Coding Guidelines
Write your queries query.py
Query for each question is to be assigned to a variable in the above python file. Variables for each question are specific individually.
Schema for the tables that are to be used for following queries

 Actor (  
	 id integer PRIMARY KEY,
	 fname varchar(250),  
	 lname varchar(250), 
	 gender varchar(10) 
 );

 Movie(  
	 id integer PRIMARY KEY, 
	 name varchar(250), 
	 year integer, 
	 rank integer
 );
	
 Director(  
	 id integer PRIMARY KEY, 
	 fname varchar(250), 
	 lname varchar(250)
 );
 



Get the total number of movies that are released in year 1991
Q1="Write your query here"
...


Get the least rank for a movies
...
Q2="Write your query here"
...


Get the maximum rank for movies that are released in year 2000
...
Q3="Write your query here"
...


Get the average ranking for movies that are released in year 2000
...
Q4="Write your query here"
...

Find the total number of unique years in the imdb database given to you.
...
Q5="Write your query here"
...


Find the time period that this database covers. (start year, end year)
...
Q6="Write your query here"
...


