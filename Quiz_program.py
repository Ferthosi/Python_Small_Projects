quiz ={
    "question1":{
        "ques":"what is the capital of Afganistan",
        "answer":"Kabul"
    },
     "question2":{
        "ques":"what is the capital of Palestine",
        "answer":"Jerusalm"
    },
     "question3":{
        "ques":"what is the capital of Iran",
        "answer":"Tehran"
    },
     "question4":{
        "ques":"what is the capital of Yamen",
        "answer":"Sanna"
    },
     "question5":{
        "ques":"what is the capital of Sudan",
        "answer":"Khartoum"
    },
     "question6":{
        "ques":"what is the capital of China",
        "answer":"Beijin"
    },
     "question7":{
        "ques":"what is the capital of Pakistan",
        "answer":"Lahor"
    },
     "question8":{
        "ques":"what is the capital of Bangladesh",
        "answer":"Dhaka"
    }
}

'''score =0
for key, value in quiz.items():
    print(value["ques"])
    answer= input("answer :")
    
    if answer.lower() == value["answer"].lower():
        print("Correct Ans")
        score +=1
        print("Your score is:"+ str(score))
    else:
        print("Wrong Ans")
        print("The ans is:" + value["answer"])
        print("Your score is: "+ str(score))'''

score =0
for key, value in quiz.items():
    print(value["ques"])
    answer = input("Answer :")

    if answer.lower() == value["answer"].lower():
        print("Your ans is correct")
        score += 1
        print("your score is: " + str(score))
    else:
        print("Wrong ans")
        print("the ans is: " + value["answer"])
        print("your score is: " + str(score))

print("You got " + str(score) + " out of 8 questions correctly")
print("Your percentage is " + str(int((score/len(quiz))*100)) + "%")