#loops

#While loops
#print numbers from 1 to 5
'''count = 1
while count<=5:
    print("hello")
    count +=1
print(count)'''

'''i = 5
while i >=1:
    print(i)
    i -= 1
print("loop ended")'''

#print multiplication table of a number n
'''n= int(input("enter number: "))
i =1
while i <= 10:
    print(n*i)
    i += 1'''
# Print the lement of the following list using a loop
 #[1,4,9,16,25,36,49,64,81,100]

'''num = [1,4,9,16,25,36,49,64,81,100]
indx = 0
while indx < len(num):
    print(num[indx])
    indx +=1'''

#practice-2
'''num = [1,4,9,16,25,36,49,64,81,100,36]
i =0
x=36
while i < len(num):
    if(num[i]==x):
        print("found at idx", i)
    else:
        print("finding..")
    i += 1'''
#Break & Continue

'''i =1
while i <=5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")'''

'''num = [1,4,9,16,25,36,49,64,81,100,36]
i =0
x=36
while i < len(num):
    if(num[i]==x):
        print("found at idx", i)
        break
    else:
        print("finding..")
    i += 1'''

'''i= 0
while i <= 5:
    if(i ==3):
        i += 1# 3 will be not printed
        continue
    print(i)
    i +=1'''
#odd numbers
'''i= 0
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i +=1'''
#Even numbers
'''i= 0
while i <= 5:
    if(i ==3):
        i += 1# 3 will be not printed
        continue
    print(i)
    i +=1'''

'''num =[1,2,3,4,5]

for val in num:
    print(val)'''

'''tup =[1,2,3,4,5]

for num in tup:
    print(num)'''

'''str = "amarcollege"

for char in str:
    print(char)'''

'''str = "amarcollege"

for char in str:
    if(char=='o'):
        print("o found")
        break
    print(char)
else:
    print("END")'''

'''nums = [1,4,9,16,25,49,64,81,100,49]
x= 49
idx =0
for val in nums:
    if(val==49):
        print("found ar idx",idx)
        #break
    idx +=1''' 

#practice-Range

'''for i in range(5):
    print(i)

for i in range(2,10):
    print(i)'''
#print num from 1 to 100 / 100 to 1
'''for i in range(1, 101):
    print(i)

for i in range(101,0,-1):
    print(i)'''

#Print calculator of a num
'''n = int(input("enter num :"))

for i in range(1,11):
    print(i*n)'''

#PASS statement
for i in range(5):
    pass


#Practiec

#Wap to find the sum of first n numbers
'''n= 5
sum =0
for i in range(1, n+1):
    sum +=i

print(sum)'''

# WAP to find the factorial of first n numvers(using for )
'''n = 5
#i= 1
fact=1
while i<=n:
    fact *= i
    i += 1

print("factorial= ", fact)'''

'''for i in range(1,n+1):
    fact *= i

print("factorial= ", fact)'''
