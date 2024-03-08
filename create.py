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
