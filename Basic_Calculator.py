# Basic calculator

#define the functions needed : add, sub
#Ask the operator
#ask for the value
#Call the function
#print the value

def add(a,b):
    answer = a+b
    print(str(a) + "+" + str(b) + "=" + str(answer))


def sub(a,b):
    answer = a-b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def multiply(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def divide(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))

def modeulus(a,b):
    answer = a%b
    print(str(a) + "%" + str(b) + "=" + str(answer))

print("A. Addition")
print("B. SUbstraction")
print("C. Multiplication")
print("D. Division")
print("M. Modulus")

choice = input("Enter your choice: ")

if choice == "a" or choice =="A":
    print("Addition")
    a = int(input("Input first num: "))
    b= int(input("Input second num: "))
    add(a,b)
elif choice == "b" or choice =="B":
    print("Addition")
    a = int(input("Input first num: "))
    b= int(input("Input second num: "))
    sub(a,b)
elif choice == "c" or choice =="C":
    print("Addition")
    a = int(input("Input first num: "))
    b= int(input("Input second num: "))
    multiply(a,b)
elif choice == "d" or choice =="D":
    print("Addition")
    a = int(input("Input first num: "))
    b= int(input("Input second num: "))
    divide(a,b)
elif choice == "m" or choice =="M":
    print("Addition")
    a = int(input("Input first num: "))
    b= int(input("Input second num: "))
    modeulus(a,b)
else:
    print("Exicuition not ouccured")
    quit()
