#Chapter-3 List & Tuple


#list- Mutable
'''marks =[94.4, 87.9, 95.2, 66.4, 45.1]

print(marks)
print(type(marks))
print(marks[0])

student= ["Ferthosi", 95.4, 17,"Dhaka"]
student[0]= "Mahmud"#List are mutable, changes are possible inside the list
print(student)'''

# list slicing
'''marks =[94.4, 87.9, 95.2, 66.4, 45.1]
print(marks[0:3])
print(marks[-4:-1])'''

#list method

#list =['Apple', 'coconut','jackfruit', 'peach', 'bananna', 'lichi','grape']
#list.append(8)
#print(list)
#list.sort()
#print(list)
#list.sort(reverse = True)
#print(list)
#list.reverse()
#print(list)
#list.insert(1, "dragonfruit")
#list =[2, 1,3,1]
#list.remove(1)#element as perameter
#list.pop(2)#index as perameter
#print(list)



#Tuple in python- immutable

'''tup= (2,3,4,5,6,7,8,)
print(tup[0])
#tup[0]=5

tup1=()
print(tup1)
print(type(tup1))

tup2 =(1,)#single value tuple
print(tup2)
print(type(tup2))

tup3 =(1)#can not define without ",", makes it integer
print(tup3)
print(type(tup3))'''

#Tuple slicing
'''tup =(1,2,3,4)
print(tup[1:3])'''

#tuple method
'''tup=(1,2,3,4)
print(tup.index(2))
print(tup.count(2))'''

#EXCERCISE

#ask the user to enter names of their 3 fav movies and store 
#them in a list
'''movies =[]
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)'''
'''movies =[]
movies.append(input("enter 1st movie: "))
movies.append(input("enter 2nd movie: "))
print(movies)'''

#Check if a list contains a palinfrome of elelments

'''list1 =[1,2,3]
#list2 =[1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 ==list1):
    print("palindrome")
else:
    print("Not palindrome")'''
#Count the number of A grades for a student
'''grade = ("C","B","A","A","D","B","B")   
print(grade.count("A"))'''
#store the above values in a list & sort them from "A" to "D"

grade = ["C","B","A","A","D","B","B"] 
grade.sort()  
print(grade)

