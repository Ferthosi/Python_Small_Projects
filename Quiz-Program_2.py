questions=[
    {
        "promt":"What is the capital of Palestine?",
        "options":["A. Paris","B. Jerusalem","C. Lahor","D. Rafah"],
        "answer":"B"
    },
    {
        "promt":"Which language is spoken in Saudi Makka?",
        "options":["A. Arabic","B. Urdu","C. Farshi","D. Turkish"],
        "answer":"A"
    },
    {
        "promt":"What is the smalles prime number?",
        "options":["A. 1","B. 3","C. 2","D. 0"],
        "answer":"C"
    },
    {"promt":"Who wrote 'To kill a Mocking Bird?",
        "options":["A. Harper Lee","B. Mark Twain","C. J.K Rowling","D. Ernest Hemingway"],
        "answer":"A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['promt'])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A,B,C,D): ")
        if answer.upper() == question["answer"]:
            print("Correct, Hooray!!\n")
            score +=1
        else:
            print("Opps! Worng Answer")
            print("Correct answer was:",questions["answer"])

    print(f"You got {score} out of {len(questions)} questions correct.")



run_quiz(questions)