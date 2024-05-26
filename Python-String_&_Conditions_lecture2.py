# escape sequence charecters
'''str1 = "This is a string.\they how are you"
print(str1)'''

#Basic operations on string
#Concatanation and lenth of string

#indexing
'''str ="apna college"
ch =str[1]
print(ch)

str[4]= "@"
print(str)'''# string modification is not possible


#String Slicing
'''str = "Amar College"
print(str[1:4])
print(str[:4])#[0:4]
print(str[5:])#[5:len(str)]'''

'''str = "apple"
print(str[-3:-1])'''

#string Function

#endswith function
'''str = " i am studying python from my college"
print(str.endswith("ege"))
print(str.endswith("app"))'''


# capitalize function
'''str = "i am studying python from my college"
print(str.capitalize())'''

# replace function


'''str = "i am studying python from my college"
print(str.capitalize())
print(str.replace("t", "a"))'''
#find function

'''str = "i am from studying python from my college"
print(str.find("from"))
print(str.find("Q"))'''

#count function 
'''str = "i am from studying python from my college"
print(str.count("from"))'''


#practice

'''name = input("enter your name: ")
print("length of your name is", len(name))'''





#Conditional Statement
#Grade students based on marks

'''marks = int(input("enter your marks: "))

if(marks>=90):
    grade = "A"
elif(marks >= 80 and marks<90):
    grade="B"
elif(marks >=70 and marks<80):
    grade ="C"
else: 
    grade = "D"

print("Grade if the students :", grade)'''

#Nesting

'''age = 40
if (age >= 18):
    if(age>=65):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")'''

#excercise
#find a number is odd or even 

'''num = int(input("enter number: "))

rem = num % 2

if(rem == 0):
    print("the number is even")
else: 
    print("the number is odd")'''

#Find out the largest number of 3

'''a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: "))

if(a >= b and a >= c):
    print("1st is greatest", a)
elif(b >= c):
    print("2nd is greatest", b)
else:
    print("3rd is greatest", c)'''

# find a number is multiple of 7

'''x = int(input("enter number: "))

if(x%7==0):
    print("Number is multiple of 7")
else:
    print("Number is not multiple of 7")'''
    