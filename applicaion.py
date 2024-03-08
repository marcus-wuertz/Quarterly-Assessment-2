import sqlite3

# Connect to the quiz bowl database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Get user input for the category
user_input = input("Welcome to the Quiz Bowl! Please select a category from the following options:\n"
                   "- Business Strategy\n"
                   "- Business Applications\n"
                   "- Programming Logic\n"
                   "- Analytics Capstone\n"
                   "- Business Law\n"
                   "Your choice: ").strip().lower().replace(" ", "")

#print(user_input)

# Define the database table based on the user input
if user_input == 'businessstrategy':
    table_name = 'BusinessStrategy'
elif user_input == 'businessapplications':
    table_name = 'BusinessApplications'
elif user_input == 'programminglogic':
    table_name = 'ProgrammingLogic'
elif user_input == 'analyticscapstone':
    table_name = 'AnalyticsCapstone'
elif user_input == 'businesslaw':
    table_name = 'BusinessLaw'
else:
    print("Invalid category selection. Please try again.")
    exit()
#print(table_name)

# ANSI escape codes for text colors
GREEN = '\033[92m'  # Green color
RED = '\033[91m'    # Red color
RESET = '\033[0m'    # Reset color

# Initialize a variable to track the number of correct answers
correct_count = 0

# Fetch questions from the selected category
cursor.execute(f"SELECT * FROM {table_name}")
questions = cursor.fetchall()

# Using a for loop to ask the user all the questions in the table
for question in questions:
    id, question, option1, option2, option3, option4, correct_answer = question

    # Present the question and options to the user
    print(f"Question: {question}")
    print(f"A. {option1}")
    print(f"B. {option2}")
    print(f"C. {option3}")
    print(f"D. {option4}")

    # Prompt the user for their answer
    user_input = input("Your answer (A/B/C/D): ").strip().upper()

    # Adding an if statement to let users know if their input is invalid
       # Check if the user's input is a valid option
    if user_input not in ['A', 'B', 'C', 'D']:
        print(f"{RED}Invalid option! Please choose from A, B, C, or D.{RESET}")
        continue

    # Check if the user's input corresponds to the correct answer
    if user_input == 'A':
        user_answer = option1
    elif user_input == 'B':
        user_answer = option2
    elif user_input == 'C':
        user_answer = option3
    elif user_input == 'D':
        user_answer = option4

    if user_answer == correct_answer:
        print(f"{GREEN}Correct!{RESET}")
        correct_count += 1
    else:
        print(f"{RED}Incorrect.{RESET}")
        print(f"The correct answer was: {correct_answer}")

# Display the total number of correct answers
print(f"\nYou answered {correct_count} out of {len(questions)} questions correctly.")

# Reset color settings
print(RESET)