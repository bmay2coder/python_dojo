#### Lecture 1
#### Python Syntax

# FOUR SPACES

# def some_function(input1, input2):
#     count=0
#     for i in input1:
#         print(i, end=" ")
        
#         for z in input2:
#             print(z, end=" ")
#             count+=1
#             pass
        
#         print("")
        
#     return(count)

# def main():
#     number=some_function((1,2,3), ["python", "is" , "fun"])
#     print("The count for this program is {}" .format(number))
#     pass

# if __name__ == "__main__":
#     main()

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


#### Lecture 2
#### Lists Overview

# # A good example is a grocery list.

# groceries=[
#     "eggs",
#     "turkey bacon",
#     "hashbrowns",
#     "pancakes"
# ]
# print(*groceries)

# print("printing lists separated by commas")
# print(*groceries, sep = ", ") 

# # print in new line
# print("printing lists in new line")
# print(*groceries, sep = "\n")

# # You can have lists within a list 
# ninjas = ['Rozen', 'KB', 'Oliver']
# my_list = ['4', ['list', 'in', 'a', 'list'], 987]
# empty_list = []

# # You can concatenate lists
# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)

#### List Manipulation

# drawers = ["documents", "envelopes", "pens"]
    
# # access the drawer with index of 0 and print value
# print(drawers[0])  #prints documents
# # access the drawer with index of 1 and print value
# print(drawers[1]) #prints envelopes
# # access the drawer with index of 2 and print value
# #print(drawers[="constant numeric from-rainbow">2]) #prints pens
    
# # replace "documents" with "tchotchkes"
# drawers[0] = "tchotchkes"
# print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# # stores the value "tchotchkes" in a temporary variable.
# top_contents = drawers[0]
    
# # Replaces the value at index 1
# # with whatever value is stored at index 0
# drawers[1] = drawers[0]
# print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

# # Slicing
# words = ["start","going","till","the","end"]
# # Sub-ranges (portions) of the list
# print(words[1:]) # prints ['going', 'till', 'the', 'end']
# print(words[:4]) # prints ['start', 'going', 'till', 'the']
# print(words[2:4]) # prints ['till', 'the']
    
# # Making a copy of a list
# copy_of_words = words[:]
# copy_of_words.append("dojo") # only appends to the copy
# print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
# print(words) # prints ['start', 'going', 'till', 'the', 'end']

#### Built-in Functions for Lists

# my_list = [1, 'Zen', 'hi']
# print(len(my_list))

# my_list = [1, 2, 5, 4, 3, 8, 6, 7]
# print(max(my_list))
# print(min(my_list))
# print(sorted(my_list))

# my_list.pop()
# print(my_list)

# my_list.append(7)
# my_list.append(9)
# print(my_list)

# print(my_list.index(3))
# new_list=[0,1,2,5,4,3]
# print(new_list)
# new_list.reverse()
# print(new_list)
# new_list.sort()
# print(new_list)

#### Tuples

# # Use the parathesis () instead of brackets [] like lists, or no () at all. Normal is using ()
# # You can't change Tuples they are immuntable.

# tuple_data = ('physics', 'chemistry', 1997, 2000)
# tuple_num = (1, 2, 3, 4, 5 )
# tuple_letters = 1, 2, 3, 4

# print(type(tuple_data))
# print(type(tuple_num))
# print(type(tuple_letters))

#### Conditionals

# multiple line tab forward and alt tab backwards
    # x = 12
    # if x > 50:
    #     print("bigger than 50")
    # else:
    #     print("smaller than 50")
    # # because x is not greater than 50, the second print statement is the only one that will execute

    # x = 55
    # if x > 10:
    #     print("bigger than 10")
    # elif x > 50:
    #     print("bigger than 50")
    # else:
    #     print("smaller than 10")
    # # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

    # if x < 10:
    #     print("smaller than 10")
    # # nothing happens, because the statement is false   

#### Lecture 3
#### Loops

# # Loops using range()
# for i in range(5):
#     print(i)

# for i in range(2, 7):
#     print(i)

# for i in range(2, 16, 3):
#     print(i)

# for x in range(0, 10, 2):
#     print(x)
# # What is going to be the output

# for x in range(5, 1, -3):
#     print(x)
# # What is going to be the output

#### Looping Over Lists & Strings

# for x in 'Hello':
#     print(x)

# my_list = ["abc", 123, "xyz"]
# for i in range(0, len(my_list)):
#     print(i, my_list[i])
    
# for v in my_list:
#     print(v)

# for count in range(0,5):
#     print("looping =", count)

# count = 0
# while count <= 5:
#     print("looping - ", count)
#     count += 1

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
# else:
#     print("Final else statement")

# for val in "string":
#     if val == "i":
#         break
#     print(val)


# for val in "string":
#     if val == "i":
#         continue
#     print(val)

# y = 3
# while y > 0:
#     print(y)
#     y = y - 1
#     if y == 0:
#         break
# else:		# only executes on a clean exit from the while loop (i.e. not a break)
#    print("Final else statement")

#### Functions

# def add(a,b):	# function name: 'add', parameters: a and b
#     x = a + b	# process
#     return x	# return value: x

# new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
# print(new_val)    # the result of the add function gets sent back to and saved into new_val, so we will see 8

# def say_hi(name):
#     print("Hi, " + name)

# # invoking the function 3 times, passing in one argument each time
# say_hi('Michael')
# say_hi('Anna')
# say_hi('Eli')

# def say_hi(name):
#     return "Hi " + name
# greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
# print(greeting) # this will output 'Hi Michael'

# def add(a, b):
#     x = a + b
#     return x
# sum1 = add(4,6)
# print(sum1)
# sum2 = add(1,4)
# print(sum2)
# sum3 = sum1 + sum2
# print(sum3)

#### Default Parameters & Named Arguments

# # set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
	
# be_cheerful()    # output: good morning (repeated on 2 lines)
# be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# # # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

#### Debugging

def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def multiply(num_list, num):
    print(num_list, num)
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def multiply(num_list,num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(x)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)

#### Dictionaries

#### Dictionary Manipulation

#### Loops & Dictionaries

#### Nested Dictionaries & Lists
