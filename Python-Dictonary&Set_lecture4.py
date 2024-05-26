#Dictonary
#they are unordered,mutable(Changable)& dont allow duplicate keys

'''info ={
    "name":"Ferthosi",
    "subjects":["python","Java","C+"],
    "topics":["Dic","Set"],
    "age": 24,
    "is_adult": True,
    "marks":94.5
}

null_dic={  
}
print(null_dic)
null_dic["name"] ="Mahmud"
print(null_dic)

info["name"]="Faiyaz" #overwrite
print(info["name"])
print(info["topics"])
print(info["subjects"])'''


#Nested Dictonary

'''student ={
    "name": "ferthosi",
    "subjects":{
        "phy": 95,
        "chem":94,
        "math":97
    },
    "age": 24
}
#print(student)
print(student["subjects"]["chem"])'''

#Dictonary Methods
#My_dict.keys() method- returns all the keys
'''student ={
    "name": "ferthosi",
    "subjects":{
        "phy": 95,
        "chem":94,
        "math":97
    },
    "age": 24
}
print(len(student))
print(student.keys())
print(list(student.keys()))#type casting'''
#Values methos_returns all values
'''student ={
    "name": "ferthosi",
    "subjects":{
        "phy": 95,
        "chem":94,
        "math":97
    },
    "age": 24
}
print(list(student.values()))'''

#items() method-Returns all (key, val) pairs as tuples

student ={
    "name": "ferthosi",
    "subjects":{
        "phy": 95,
        "chem":94,
        "math":97
    },
    "age": 24
}

#print(student.items())
#pairs = list(student.items())
#print(pairs[0])

#get() methode
'''print(student.get("name"))'''

#update() methode

#student.update({"city": "Dhaka"})
'''new_dict= {"city":"Dhaka"}
student.update(new_dict)
print(student)'''

#SETS in python- set is mutable but its elements are immutable,
# Only contains unque values.can not store list or dictonary
#set is unordered

'''collection ={1,2,3,4,"hello","world"}
#collection ={1,2,2,2,3,4,"hello","world"}# ignore the duplicate value
print(len(collection))# in length also ignore the duplicate values
print(collection)
print(type(collection))'''

#empty set
'''collection = set()
print(type(collection))'''

#Set methods

#set.add()
'''collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(3)
collection.add("ferthosi")
collection.add((1,2,3))# can add a tuple
#collection.add([1,2,3])# can not add a list. will come error after run'''
#set.remove
'''collection.remove(3)
#collection.remove(3)# will come error if the element doesnt exist
print(collection)
print(len(collection))'''
#set.clear()
'''collection.clear()
print(len(collection))'''
#set.pop()
'''print(collection.pop())
print(collection)'''

#set.union(set2)
'''set1={1,2,3}
set2={2,3,4}
#print(set1.union(set2)) #{1,2,3,4}
print(set1.intersection(set2)) #{2,3}'''

#Practice-1

#store following word meaning in python dictionary
'''table: "a piece of furniture","list of facts & figure"
cat: "a small animal"'''

'''dictionary ={
    "tabke":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}'''

#Practice-2

'''subjects ={
    "python","java","C++","python","javascript","java","python","java","C++","C"
}
print(subjects)
print(len(subjects))'''

#Practice-3-ENter marks of 3 sub from user, store them in dictonary
#start with empty dictionary adn add one by one.
'''marks={

}
phy = input("enter phy: ")
marks.update({"physics": phy})

math = input("enter math: ")
marks.update({"Math": math})

chem = input("enter chem: ")
marks.update({"Chemistry": chem})

print(marks)'''

#practice-4
#figure out a way to store 9 & 9.0 as seperate value in a set
#(you can take help of built in data type)

#solution-1
'''values ={"9",9.0}
print(values)'''
#solution-2
'''values={
    ("float",9.0),
    ("int",9)
}
print(values)'''




