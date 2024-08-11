# Lecture 1
# Python Syntax
# FOUR SPACES

def some_function(input1, input2):
    count=0
    for i in input1:
        print(i, end=" ")
        
        for z in input2:
            print(z, end=" ")
            count+=1
            pass
        
        print("")
        
    return(count)

def main():
    number=some_function((1,2,3), ["python", "is" , "fun"])
    print("The count for this program is {}" .format(number))
    pass

if __name__ == "__main__":
    main()

#### Data Types

# b_text="sometext"
# print(type(b_text))

# b_number=5000
# print(type(b_number))

# b_boolean=True
# print(type(b_boolean))

# b_list=[1, 2, 3, 4]
# print(type(b_list))

# b_tuple=(1, 2, 3, 4)
# print(type(b_list))

# b_dictionary={'Student_ID': 18475, 'first_name': 'Bret', 'last_name': 'May'}
# print(type(b_dictionary))

# dog = ('Bruce', 'cocker spaniel', 19, False)
# print(dog[0])		# output: Bruce
# dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# empty_list = []
# ninjas = ['Rozen', 'KB', 'Oliver']
# print(ninjas[2]) 	# output: Oliver
# ninjas[0] = 'Francis'
# ninjas.append('Michael')
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
# ninjas.pop()
# print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
# ninjas.pop(1)
# print(ninjas)	# output: ['Francis', 'Oliver']

# empty_dict = {}
# new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
# new_person['hobbies'] = ['climbing', 'coding']
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# w = new_person.pop('weight')	# removes the specified key and returns the value
# print(w)		# output: 160.2
# print(new_person)	
# # output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

# print(type(2.63))		# output: <class 'float'>
# print(type(new_person))		# output: <class 'dict'>

# print(len(new_person))		# output: 4 (the number of key-value pairs)
# print(len('Coding Dojo'))	# output: 11 

#### Numbers

# print(type(24))
# print(type(3.9))
# print(type(3j))

# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# import random
# print(random.randint(2,5000))

#### Strings

# print("this is a sample string")

# name = "Zen"
# print("My name is", name)

# name = "Zen"
# print("My name is " + name)

# print("Hello " + 42)			# output: TypeError
# print("Hello " + str(42))		# output: Hello 42

# total = 35
# user_val = "26"
# total = total + user_val		# output: TypeError
# total = total + int(user_val)		# total will be 61

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"My name is {first_name} {last_name} and I am {age} years old.")

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# # output: My name is Zen Coder and I am 27 years old.
# print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# # output: My name is 27 Zen and I am Coder years old.

# # Practice Challenge: Correct the errors!
# first_name = "Alana"
# last_name = "Da Silva"
# age = 36
# profession = "Software Developer"
# years_experience = 5
# greeting = "Hello my name is ", first_name, last_name
# print(greeting) 
# # Desired output: Hello my name is Alana Da Silva
# print("I am {age} years old") 
# # Desired output: I am 36 years old
# print("I work as a profession.".format("profession"))
# # Desired output: I work as a Software Developer.
# exp_string = "I have worked in the field for {} years."
# print(exp_string.format())
# # Desired output: I have worked in the field for 5 years.
# print("I started in the field when I was " + age - years_experience " years old.")
# # Desired output: I started in the field when I was 31 years old.

# hw = "Hello %s" % "world" 	# with literal values
# py = "I love Python %d" % 3 
# print(hw, py)
# # output: Hello world I love Python 3
# name = "Zen"
# age = 27
# print("My name is %s and I'm %d" % (name, age))		# or with variables
# # output: My name is Zen and I'm 27

# x = "hello world"
# print(x.title())
# # output:
# "Hello World"


# Lecture 2
# Lists Overview

# List Manipulation

# Built-in Functions for Lists

# Tuples

# Conditionals

# Lecture 3
# Loops

# Looping Over Lists & Strings

# Functions

# Default Parameters & Named Arguments

# Debugging

# Dictionaries

# Dictionary Manipulation

# Loops & Dictionaries

# Nested Dictionaries & Lists
