# Quarterly-Assessment-2
This README file details the purpose of each file in the repository, and how to interact with them. 
This document clearly outlines different instructions for those attempting to use the program and those looking to add to it.
## Users only need to run the "application.py" file to use the quiz bowl

# quiz_bowl_db.py
-Users do NOT need to interact with this file
-This is a file designed to create our database ('quiz_bowl.db') and put our blank tables in it
-Programmers should use this file if they wish to add another table (course) into the database
-Use the same format as previous tables

# create.py
-Users do NOT need to interact with this file
-This file is designed to populate our tables in the database with our questions, options, and answer
-This file stores the questions for each table in separate lists, with each question in it's own dictionary
-Programmers should interact with this file ONLY to add more questions into our database
-Programmers should NOT add another dictionary to the list and run the for loop
-That would add duplicate data into the database
-To add new questions, use the 'add_question' function
-Make sure your data is formatted correctly (match to the column names from the table)
-Run the read.py file to see the format of columns, as well as the data in the tables

# read.py
-Users do not need to run this file, but they can if they want to see what's in the database
-Users should not need to alter the code for this file, just run it 
-This file's purpose is to check what data populated into each table in our database
-Programmers should not need to alter the code, UNLESS they added another table into the database, in which case you'll need to insert it into the 'tables' variable

# application.py
## This is the ONLY file users are required to run to use the quiz bowl application
-Users should interact with the terminal, NOT the code itself
-Users simply need to run the file, and follow the directions in the terminal. 
-Users will be prompted to select a category (as long as it's spelled correctly it will work regardless of capitalization or spelling)
-Then, youll see a question followed by multiple choice options
-Your answers should be either A, B, C, or D, and the program will tell you if you are correct
-After you've answered all the questions in the table, youll see your total score, and will be asked if you'd like questions from another category
-Programmers should also exclusively interact with the terminal UNLESS they added another table, in which case they should include the table(s) in the 'user_input' and the following if statement

