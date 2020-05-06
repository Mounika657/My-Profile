iBHubs

Home
AssignmentID - DB004
Submission Guidelines
Coding Guidelines
# Submission Guidelines

Create a folder /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_004. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/dbms/dbms_submissions/dbms_assignment_004/
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
 



Get the total number of movies that are released in the year 2002, Where the movie name starts with "Ha" and movie rating is greater than 2
Q1="Write your query here"
...

Get the maximum rank among the movies whose names start with "Autom" and released in the year 1983 or 1994
...
Q2="Write your query here"
...


Get the total number of actors whose
gender is "M"(male) and
the fname ends with ei" or the lname starts with "ei"
...
Q3="Write your query here"
...

Get the average ranking of all the movies
that are released in 1993 or 1995 or 2000 &
their rank is greater than or equal to 4.2.
the column name of the result should be average_rank_of_movies instead of AVG(rank)

...
Q4="Write your query here"
...


Get the sum of ranks of all the movies whose
movie name contains "Harry" and
released between 1981 and 19984 (both inclusive) and
its rank is less than 9
...
Q5="Write your query here"
...


Get the year in which a movie got rank = 5 for the first time.
...
Q6="Write your query here"
...


Count the total number of female actors in the database and also include the actors which have same first and last names.
...
Q7="Write your query here"
...


Get 100 distinct fnames of actors whose lname ends with "ei" and the result should be in the ascending order of actor first name
...
Q8="Write your query here"
...


Skip the first 10 rows and get 25 movies that are released in the year (2001, 2002, 2005, 2006) and the output should have column movie_title instead of name.
...
Q9="Write your query here"
...

# Output Format:
id, movie_title, year
1, Harry Potter, 2004
...
Get the first 5 distinct lnames of directors whose fname is in ("Yeud", "Wolf", "Vicky). The result should be in the ascending order of director's lname.
...
Q10="Write your query here"
...


