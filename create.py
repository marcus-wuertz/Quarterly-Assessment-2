import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_bowl.db')
cursor = conn.cursor()

# create a list of dictionaries with the questions and answers for Business Strategy
questions = [
    {
        "id": 1,
        "question": "Porter's Five Forces framework assesses _____?",
        "option1": "Industry",
        "option2": "Organization",
        "option3": "Market",
        "option4": "Country",
        "correct_answer": "Industry"
    },
    {
        "id": 2,
        "question": "What does SWOT analysis stand for?",
        "option1": "Strengths, Weaknesses, Opportunities, Threats",
        "option2": "Strengths, Weaknesses, Opportunities, Trends",
        "option3": "Strategies, Weaknesses, Opportunities, Threats",
        "option4": "Strengths, Warnings, Opportunities, Threats",
        "correct_answer": "Strengths, Weaknesses, Opportunities, Threats"
    },
    {
        "id": 3,
        "question": "Successful business strategy characteristics include being _____?",
        "option1": "Clear, Focused",
        "option2": "Detailed, Long",
        "option3": "Ambiguous, General",
        "option4": "Uncertain, Vague",
        "correct_answer": "Clear, Focused"
    },
    {
        "id": 4,
        "question": "Differentiation strategy focuses on offering _____ products or services.",
        "option1": "Unique",
        "option2": "High-cost",
        "option3": "Similar",
        "option4": "Expensive",
        "correct_answer": "Unique"
    },
    {
        "id": 5,
        "question": "Competitive advantage contributes to business _____?",
        "option1": "Success",
        "option2": "Failure",
        "option3": "Mediocrity",
        "option4": "Stagnation",
        "correct_answer": "Success"
    },
    {
        "id": 6,
        "question": "The role of strategic planning involves _____?",
        "option1": "Goal setting",
        "option2": "Analysis, Planning",
        "option3": "Execution",
        "option4": "All the above",
        "correct_answer": "All the above"
    },
    {
        "id": 7,
        "question": "Main components of a strategic management process include _____?",
        "option1": "Environmental scanning, Formulation, Implementation",
        "option2": "Strategy, Tactics, Operations",
        "option3": "HR, Finance, Marketing",
        "option4": "None of the above",
        "correct_answer": "Environmental scanning, Formulation, Implementation"
    },
    {
        "id": 8,
        "question": "Blue ocean strategy aims for uncontested _____?",
        "option1": "Market",
        "option2": "Competitive edge",
        "option3": "Innovation",
        "option4": "Industry",
        "correct_answer": "Market"
    },
    {
        "id": 9,
        "question": "Environmental scanning helps identify _____ and threats?",
        "option1": "Opportunities",
        "option2": "Competitors",
        "option3": "Risks",
        "option4": "None of the above",
        "correct_answer": "Opportunities"
    },
    {
        "id": 10,
        "question": "Challenges of implementing a new business strategy include _____?",
        "option1": "Resistance to change",
        "option2": "Resource constraints",
        "option3": "Organizational inertia",
        "option4": "All the above",
        "correct_answer": "All the above"
    }
]
# Insert questions into the BusinessStrategy table
for question in questions:
    cursor.execute('''INSERT INTO BusinessStrategy (id, question, option1, option2, option3, option4, correct_answer)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
                                                         question['option2'], question['option3'], question['option4'],
                                                         question['correct_answer']))
# use select query to check if your data properly populated the table
#cursor.execute('''SELECT * FROM BusinessStrategy''')

# Fetch all rows from the result set
#rows = cursor.fetchall()

# Print the fetched rows
#for row in rows:
#    print(row)

# List of questions for Business Applications Development course
business_app_questions = [
    {
        "id": 1,
        "question": "What is the purpose of using generative AI in software development?",
        "option1": "To automate testing processes",
        "option2": "To generate code automatically",
        "option3": "To design user interfaces",
        "option4": "To analyze user behavior",
        "correct_answer": "To generate code automatically"
    },
    {
        "id": 2,
        "question": "Which Python control structure is typically used to iterate over a sequence of elements?",
        "option1": "if-else statement",
        "option2": "for loop",
        "option3": "while loop",
        "option4": "try-except block",
        "correct_answer": "for loop"
    },
    {
        "id": 3,
        "question": "What is the purpose of using dictionaries in Python?",
        "option1": "To store ordered data",
        "option2": "To store data in key-value pairs",
        "option3": "To store only numeric data",
        "option4": "To perform mathematical operations",
        "correct_answer": "To store data in key-value pairs"
    },
    {
        "id": 4,
        "question": "What is the primary purpose of using functions in programming?",
        "option1": "To repeat a block of code",
        "option2": "To organize code into reusable units",
        "option3": "To display output on the screen",
        "option4": "To handle errors and exceptions",
        "correct_answer": "To organize code into reusable units"
    },
    {
        "id": 5,
        "question": "What is the purpose of using databases in software development?",
        "option1": "To improve user interface design",
        "option2": "To perform mathematical calculations",
        "option3": "To store and manage data persistently",
        "option4": "To generate random numbers",
        "correct_answer": "To store and manage data persistently"
    },
    {
        "id": 6,
        "question": "Which Python statement is used to catch and handle exceptions?",
        "option1": "try-except",
        "option2": "if-else",
        "option3": "for",
        "option4": "while",
        "correct_answer": "try-except"
    },
    {
        "id": 7,
        "question": "What does the term 'IDE' stand for in software development?",
        "option1": "Integrated Development Environment",
        "option2": "Interpreted Development Environment",
        "option3": "Interactive Design Environment",
        "option4": "Innovative Development Engine",
        "correct_answer": "Integrated Development Environment"
    },
    {
        "id": 8,
        "question": "What is the purpose of a while loop in Python?",
        "option1": "To execute a block of code a fixed number of times",
        "option2": "To iterate over a sequence of elements",
        "option3": "To execute a block of code indefinitely until a condition is met",
        "option4": "To handle errors and exceptions",
        "correct_answer": "To execute a block of code indefinitely until a condition is met"
    },
    {
        "id": 9,
        "question": "Which data structure in Python is used to represent a collection of elements with unique keys?",
        "option1": "List",
        "option2": "Tuple",
        "option3": "Set",
        "option4": "Dictionary",
        "correct_answer": "Dictionary"
    },
    {
        "id": 10,
        "question": "What is the purpose of using modules in Python?",
        "option1": "To store and manage data",
        "option2": "To perform mathematical operations",
        "option3": "To organize code into separate files for reusability",
        "option4": "To handle errors and exceptions",
        "correct_answer": "To organize code into separate files for reusability"
    }
]
