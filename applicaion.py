import sqlite3

# Connect to the quiz bowl database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Get user input for the category
user_input = input("Welcome! Please select a category from the following options:\n"
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
    
# Fetch questions from the selected category
cursor.execute(f"SELECT * FROM {table_name}")
questions = cursor.fetchall()