#function definition
'''def cal_sum(a,b): #parameter
    return a+b
#function call
sum= cal_sum(1,2) #arguments
print(sum)'''

#built in function

'''print("amarcollege","amarlife")#sep=" "
print("amarcollege","amarlife")# end ="\n"
print("amarcollege", end="$")
print("amarlife")'''


'''cities =["Dhaka","KHulna","Rajshahi","Sylhet","Gazipur"]
heroes =["Superman","Batman","Greenlantern","Wolveren"]'''
# WAF to find the legth of a list(list in parameter)
'''def print_len(list):
    print(len(list))
print_len(cities)'''
#WAP to print the elements of a list in a single line(list in parameter)
'''def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heroes)'''

#WAP to find the factorial of a number
'''def cal_fact(n):
    fact= 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact()'''

#WAF to convert USD to Taka
'''def converter(usd_val):
    taka = usd_val * 117
    print(usd_val,"USD =",taka,"TAKA")

converter(120)'''

#wap to find a nuber odd or even.
'''def determine(n):
    if(n%2==0):
        print("Even")
    else:
        print("odd")

determine(5)'''


#Recursion-------------------------

'''def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    #print("end")

show(3)'''

#Factorial in recursion

'''def fact(n):
    if(n ==1 or n==0):
        return 1
    return n*fact(n-1)

print(fact(5))'''

#Write a recursive function to calculate the sum of first n numbers

'''def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1)+n

print(cal_sum(5))'''

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits =["Mango","Jackfruite","Apple","Watermelon","Bannana","Orange"]

print_list(fruits)



