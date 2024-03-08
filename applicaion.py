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