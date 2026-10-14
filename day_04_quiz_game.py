
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. define", "D. function"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!--", "C. **", "D. #"],
        "answer": "D"
    },
    {
        "question": "What does the len() function do?",
        "options": ["A. Counts items", "B. Prints text", "C. Adds numbers", "D. Takes input"],
        "answer": "A"
    },
    {
        "question": "Which data structure stores key-value pairs in Python?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    }
]

score = 0

print("=== WELCOME TO THE QUIZ ===")

for item in questions:
    print("\n" + item["question"])

    for option in item["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_answer == item["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct answer is", item["answer"])

print("\n===== QUIZ COMPLETED =====")
print("Your final score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent! You got all answers correct!")
elif score >= 3:
    print("Good job! Keep it up!")
else:
    print("Keep practicing. You will improve!")
