# Quarterly-Assessment-2
This README file details the purpose of each file in the repository, and how to interact with them.  
This document clearly outlines different instructions for those attempting to use the program and those looking to add to it.  
## Users only need to run the "application.py" file to use the quiz bowl

# quiz_bowl_db.py
-Users do NOT need to interact with this file  
-This is a file designed to create our database ('quiz_bowl.db') and put our blank tables in it  
-Created tables for courses I'm taking this semester
-Tables are: BusinessStrategy, BusinessApplications, ProgrammingLogic, AnalyticsCapstone, and BusinessLaw
-Programmers should use this file if they wish to add another table (course) into the database  
-Use the same format as previous tables

# create.py
-Users do NOT need to interact with this file  
-This file is designed to populate our tables in the database with our questions, options, and answers  
-This file stores the questions for each table in separate lists, with dictionaries containting the questions, options, and answers  
-The file contains for loops used to add the contents of the lists to the database (these are commented out)  
-Programmers should interact with this file ONLY to add more questions into our database  
-Programmers should NOT add another dictionary to the list or run the for loops  
-That would add duplicate data into the database  
## To add new questions, use the 'add_new_question' function  
-I have provided an example of how to use the function, just call it and put the values in  
-Make sure your data is formatted correctly  
-The function will tell you whether or not your data populated the database  
-Run the read.py file to double check that your data entered the database correctly  

# read.py
-Users do not need to run this file, but they can if they want to see what's in the database  
-Users should not need to alter the code for this file, just run it  
-This file's purpose is to check what data populated into each table in our database  
-Programmers should not need to alter the code, UNLESS they added another table into the database, in which case you'll need to insert it into the 'tables' variable

# application.py
## This is the ONLY file users are required to run to use the quiz bowl application
-This file is designed to run a quiz bowl on a series of questions from a variety of topics stored in a database  
-Users should interact exclusively with the terminal, NOT the code itself  
-Programmers should also exclusively interact with the terminal UNLESS they added another table, in which case they should include the table(s) in the 'user_input' and the following if statement  
## If you added a question into a preexisting table, there is no need to alter the code on this file
-Users simply need to run the file, and follow the directions in the terminal  
-Users will be prompted to select a category (as long as it's spelled correctly it will work regardless of capitalization or spelling)  
-Then, youll see a question followed by multiple choice options  
-Your answers should be either 'A', 'B', 'C', or 'D', and the program will tell you if you are correct  
-After you've answered all the questions in the table, you'll see your score, and it will asked if you'd like more questions from another category  
-If you want more questions, type 'y', otherwise, type 'n' (capitalization and spaces won't matter)  

