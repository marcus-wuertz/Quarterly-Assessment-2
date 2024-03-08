import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# Fetch and display data from each table
tables = ['BusinessStrategy', 'BusinessApplications', 'ProgrammingLogic', 'AnalyticsCapstone', 'BusinessLaw']
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    print(f"Contents of {table} table:")
    for row in rows:
        print(row)
    print()