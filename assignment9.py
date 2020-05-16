iBHubs

Home
AssignmentID - DB009
Submission Guidelines
Know your data
Query Submission Guideline
Questions
Task 1
Task 2
Task 3
Task 4
Task 5
Task 6
Task 7
Task 8
Task 9
Task 10
Task 11
Task 12
Exam Duration: 180 minutes
Max Score: 43 Points

Note: You can make use of soccer.sqlite3 database given to solve this assignment

# Submission Guidelines
Create a folder /home/ec2-user/environment/database_submissions/dbms_assignment_009. Make use of the below example command
$ mkdir -p /home/ec2-user/environment/database_submissions/dbms_assignment_009/

# Know your data


Tables:

Team
Match
Player
MatchTeamDetails:
MatchCaptain
GoalDetails
Coding Guidelines:

Write your queries in query.py
Query for each question is to be assigned to a variable in the above metioned python file.
# Query Submission Guideline
Assign your query string to a variable with name have the following format

Q{question Number}="Write your query here"

Below are variable names for question 1 and 2 queries

Q1="Write your query here"
Q2="Write your query here"

#Questions
# Task 1
Get the average age of all the players in the database - [2 Points]

# Sample Output Format
3.245989213123125123

# Task 2
Get match_no and play_date of all the matches which have more than 50000 audience - [2 Points]
Your query should return match_no, play_date in ascending order of match_no.

# Sample Output Format
1	2016-06-11
2	2016-02-12
3	2018-02-01

# Task 3
Get the team_id and the number of matches the team has won for each team in the database (Only consider teams which have played atleast one match) - [2 Points]
Your query should return in the descending order of the number of matches won and then in the ascending ordering of team_id

# Sample Output Format
10012	4
10013	3
10014	0

# Task 4
Get the match_no, play_date for all matches whose stop1_sec is greater than average stop1_sec across all matches - [3 Points]
Your query should return match_no and play_date in descending order of match_no

# Sample Output Format
  3	2016-06-11
  2	2016-04-11
  1	2016-02-11

# Task 5
Get the team names and their captain names for all the matches in the database - [3 Points]
Your query should return match_no, team name and the captain name in ascending order of match_no and team name

# Sample Output Format
1	UK	Rob
1	USA	Mike
3	UK	John

# Task 6
Get the name of the player_of_the_match and his/her jersey_no for all the matches in the database - [3 Points]
Your query should result in match_no, player name and his/her jersey_no in ascending order of match_no

# Sample Output Format
 1	Mike	6
 2	Rob	8
 3	Pike	1

# Task 7
Get the team name and the average age of players in that team for all the teams whose average age is greater than 26 - [3 Points]
Your query should result in team name and average_age in ascending order of name

# Sample Output Format
UK	38.3
USA	27.5

# Task 8
Get the total number of goals scored by all players whose age is less than or equal to 27 - [3 Points]
Your query should return player name, jersey_no, age and the number of goals scored in the descending order of the number of goals and then ascending order of player name. (Consider only the players who scored atleast one goal)

# Sample Output Format
Rob	4	23	8
Pike	3	21	6
John	1	22	3

# Task 9
Get the percentage of goals each team has scored. - [5 Points]
percentage of goals scored by a team = (total number of goals scored by the team across all matches * 100) / total number of goals scored by all the teams acrosss all matches
Your query should return the team_id and the percentage of goals. (Consider only the teams which scored atleast one goal)

# Sample Output Format
   1	9.41234..
   2	30.58766..
   3	60.0

# Task 10
Get the average of total number of goals scored by a team across all the matches - [5 Points]

# Sample Output Format
1.8

# Task 11
Get all the players who didn’t score in any of the matches. - [5 Points]
Your query should return player_id, name and date_of_birth in the ascending order of player_id.

# Sample Output Format
1	Rob	1989-03-10	 
2	Mike	1989-03-10	 
3	Bob	1989-03-10	 

# Task 12
Get the audience count and the difference between the audience count and the teams average audience count for all matches in the database. - [7 Points]
Your query should return team_name, match_no, audience and the difference beteween the audience and the average audience across all matches played by that team in the ascending order of match_no

# Sample Output Format
USA	1	300000   12340
UK	2	123123  12340
Germany	3	123523  12340

