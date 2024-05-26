#class and objects----------
'''class Student:
    name="Ferthosi"

s1 =Student()
print(s1.name)

class Car:
    color="blue"
    brand ="Mercedes"

car1=Car()

print(car1.color)
print(car1.brand)'''

#Constructor---------------

#_ _init_ _ function
#all classes have a function called a _init_() function, which is always executed when the object is being initiated
 
'''class Student:
    #default constructors
    def __init__(self): #constructor always takes a argument-called a self perameter
        pass
    #Perameterized constructors
    def __init__(self, fullname,marks): #constructor always takes a argument-called a self perameter
        self.name = fullname
        self.marks = marks
        print("adding new student in Database..")
    
s1 =Student("Ferthosi", 87)
print(s1.name,s1.marks)

s2 = Student("Arjun",89)
print(s2.name,s2.marks)'''


#Class & INstances Attributes-----------

'''class Student:
    college_name ="ABC College"#class atrribute
    
    def __init__(self, fullname,marks): #constructor always takes a argument-called a self perameter
        self.name = fullname
        self.marks = marks
        print("adding new student in Database..")
    
s1 =Student("Ferthosi", 87)
print(s1.name,s1.marks)

s2 = Student("Arjun",89)
print(s2.name,s2.marks)

print(s2.college_name)
print(Student.coll)'''
#Class attribute & Object attributes---------
'''class Student:
    college_name ="ABC College"#class atrribute
    name = "anonymous"# class attribute
    def __init__(self, fullname,marks): 
        self.name= fullname #obj attr > class attr
        self.marks = marks
        print("adding new student in Database..")
    
s1 =Student("Ferthosi", 87)'''



# Methods-------------------------
# Methods are functions that belongs to the objects
 
'''class Student:
    college_name ="ABC College"

    def __init__(self, fullname,marks): 
        self.name= fullname 
        self.marks = marks
    def welcome(self):
        print("welcome student",self.name)

    def geta_marks(self):
        print("Marks:",self.marks)

s1 =Student("Ferthosi", 87)
s1.welcome()
s1.geta_marks()'''

#create a student class that takes name & marks of 3 subjects as arguments in constructor
# Then create a method to print the average

'''class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avrg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name,"Your avrg marks:", sum/3)

s1 = Student("Ferthosi",[87,93,94])
s1.get_avrg()

s1.name="Fayaz"
s1.get_avrg()'''


# Static Method----------------
# works at class level

'''class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod # Decorator
    def hello():
        print("hello")

    def get_avrg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name,"Your avrg marks:", sum/3)

s1 = Student("Ferthosi",[87,93,94])
s1.get_avrg()
s1.hello()'''

# Abstraction

'''class Car:
    def __init__(self):
        self.acc= False
        self.brk =False
        self.clutch=False
    
    def start(self):
        self.clutch = True
        self.acc= True
        print("car started")

car1 = Car()
car1.start()'''

# Encapsulation
# Wrapping the data and functions into a single unit (object)


# Practice-----------
'''class Account:

    def __init__(self, balance,acc):
        self.balance = balance
        self.acc= acc

    def debit(self,ammount):
        self.balance -= ammount
        print("Taka", ammount,"was debited")
        print("Total balance", self.get_balance())

    def credit(self,ammount):
        self.balance += ammount
        print("Taka", ammount,"was creited")
        print("Total balance", self.get_balance())
    
    def get_balance(self):
        return self.balance
  
acc1 = Account(15000,160)
acc1.debit(1000)
acc1.credit(5000)'''


# del keywords
# used to delete object properties or object itself
'''class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Ferthosi")

del s1
print(s1)'''


# Private & Public Attributes
# private attributes & methods are meant to be used only within the class 
# And are not accessable from outside the class
'''class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("1234","abcd")
print(acc1.acc_no)
print(acc1.reset_pass())'''

'''class Person:
    __name= "Ferthosi"

    def __hello(self):
        print("Hello person")
    
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())'''

# Inheritance---------------


# Single inheritence
'''class Car:
    color = "black"
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("car stoped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name 

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.name)
print(car2.name)
print(car1.color)
print(car1.start())'''

# INheritence are three types
# 1. Single Inheritence 2. Multi level Inheritance 3. Multiple inheritence

# Multi-level inheritance
'''class Car:
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("car stoped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.name = brand

class Fortune(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1= Fortune("Disel")
car1.start()'''


# Multiple inheritance
'''class A:
    varA = "welcome to class A"

class B:
    varB ="Wlcome to class B"

class C(A, B):
    varC ="Welcome to class C"

c1= C()
print(c1.varC)
print(c1.varB)
print(c1.varA)'''

# super method

'''class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("car stoped")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name 
        super().start()

car1 = ToyotaCar("Prius","electric")
print(car1.type)
print(car1.start())'''

# Class Method

'''class Person:
    name="anonymus"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 =Person()
print(p1.name)
p1.changeName("Ferthosi")
print(Person.name)'''

#Polymorphism

#Operators and Dunder function

'''class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self, num2):
        newreal=self.real+ num2.real
        newimg = self.img + num2.img
        return Complex(newreal,newimg)
    
    def __sub__(self, num2):
        newreal=self.real- num2.real
        newimg = self.img - num2.img
        return Complex(newreal,newimg)

num1= Complex(5,4)
num1.showNumber()

num2 = Complex(1,3)
num2.showNumber()

num3 = num1+num2
num3.showNumber()

num3 = num1-num2
num3.showNumber()'''

'''class Circle:
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return 3.14 * self.radius**2
    
    def perimeter(self):
        return 2*3.14*self.radius


c1= Circle(5)
print(c1.area())
print(c1.perimeter())'''

'''class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role=",self.role)
        print("Dept=", self.dept)
        print("Salary=",self.salary)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name= name
        self.age= age
        super().__init__("Engineer","IT","75,0000")

e1 = Engineer("Ferthosi","25")
e1.showDetails()'''

#Createa class called order which stores Item andits price

