#word dictionary
from PyDictionary import PyDictionary

'''dictionary = PyDictionary()

while True: 
    word = input("Enter your word: ")
    if word=="":
        break
        
    print(dictionary.meaning(word))'''
dictionary = PyDictionary("eyes","indentation", "head")

print(dictionary.getMeanings())