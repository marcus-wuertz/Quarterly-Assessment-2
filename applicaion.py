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

# Fetch questions from the selected category
cursor.execute(f"SELECT * FROM {table_name}")
questions = cursor.fetchall()

# Using a for loop to ask the user all the questions in the table
for question in questions:
    id, question, option1, option2, option3, option4, correct_answer = question
    
    # Dictionary mapping letter to option text
    option_mapping = {
        'A': option1,
        'B': option2,
        'C': option3,
        'D': option4
    }

    # Present the question and options to the user
    print(f"Question: {question}")
    print(f"A. {option1}")
    print(f"B. {option2}")
    print(f"C. {option3}")
    print(f"D. {option4}")

    # Prompt the user for their answer
    user_input = input("Your answer (A/B/C/D): ").strip().upper()

    # Adding an if statement to let users know if their input is invalid
    if user_input not in option_mapping:
        print(f"{RED}Invalid option! Please choose from A, B, C, or D.{RESET}")
        continue
    
    # Check if the user's input corresponds to the correct answer
    if option_mapping.get(user_input) == correct_answer.upper():
        print(f"{GREEN}Correct!{RESET}")
    else:
        print(f"{RED}Incorrect.")
        print(f"The correct answer was:{RESET} {GREEN}{correct_answer}{RESET}")

# Reset color settings
print(RESET)