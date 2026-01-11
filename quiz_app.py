questions = {
    "What is the capital of India? ": "Delhi",
    "Which language is used for web development? ": "Python",
    "What does CPU stand for? ": "Central Processing Unit"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question)
    if user_answer.strip().lower() == answer.lower():
        score += 1

print(f"Your Score: {score}/{len(questions)}")
