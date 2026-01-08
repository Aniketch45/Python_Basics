#assigning sigle value to multiple variables
# a = b = c = 5
# print(a,b,c)

#multiple values to multiple variables
# a,b,c = 2,6,9
# print(a,b,c)

#Unpacking Elements from collection
# a,b,*c = [10,40,20,23,88,76]
# print(a)
# print(b)
# print(c)

#Two types of Variables 1. Local(Created inside the function, Used in only that Function) 2. Global(Created Outside the function, used in Anywhere in Python Script)
# num1 = 60    #global
# def func():
#     num2 = 20    #local
#     print(num2)
#     print(num1)

# func()

#String
#single line 
# str2 = 'Chafekar'
# print(str2)
# str1 = "Aniket"
# print(str1)

#multiline
# str1='''Happy New Year
# This year may Bring Happiness in your life
# Stay Consistent and Trust The Process'''

# print(str1)

#array using string in python
Dob = '02/12/2004'
# print(Dob[1])

# length = len(Dob)
# print("The size is:",length)

#Slicing string
# print(Dob[6:])
# print(Dob[:])
# print(Dob[::-1]) #reverse string
# print(Dob[-1])
# print(Dob[-6:-1])        #negative slicing
# print(Dob[0:9:2])    #start : end : step

#string is Immutable
# name = 'Aniket'
# print(id(name))
# print(name)
# name = name.upper()
# print(name)
# print(id(name))

# print(name.lower())
# print(name.capitalize())
# print(name.casefold())
# print(name.find('n'))

country = "            India       ."
# print(country.strip())
# print(country.lstrip())
# print(country.rstrip())


country="India"
# print(country.replace('I','i'))
# print(country.replace('ia',' '))

stmt="hi good evening"
# print(stmt.split())

#tuple
# num=(10,20,30,40,10)
# print(num.count(10))
# print(num.index(20))

# print(stmt+country)

# var = 'It\'s Aniket' 
# print(var)

# var = 'hi hello \n how\b are \t you?'
# print(var)

# students=["Amit","Chirag","Akash","Sagar","Uday","Aniket"]
# print(students[2])

# print(len(students))

list2=['Ram',25,8.90,'Aniket',True,[10,49,80],('Chafekar',51)]
# print(list2[5])

# tup=('Chafekar',51)
# print(type(tup))
# list=list(tup)
# print(type(list2))

# list2.append('2026')
# print(list2)

#copying doesn't change to original
# li=list2.copy()
# print(li)
# li.pop()
# print(li)
# print(list2)

#Aliasing referencing to same memory Address
# li=list2
# print(li)
# li.remove("Aniket")
# print(li)
# print(list2)

# print(list2.count(25))
# print(list2.index('Aniket'))
# list2.insert(4,"Heloo")
# print(list2)
# list2.remove('Heloo')
# print(list2)
# list2.reverse()
# print(list2)

list3=[20,11,64,9,64,10,88]
# list3.sort()
# print(list3)

# list3.sort(reverse=True)
# print(list3)


#tuple
# data = ('Nashik','Pune','Chh. Sambhajinagar','Dhule','A.Nagar')
# print(data.count('Nashik'))
# print(data.index('Chh. Sambhajinagar'))

#tuple is immutable ordered and unchangeable
#so we can't update tuple to update it we have to do tule->list->update list->tuple

# data= ('Nashik','Pune','Chh. Sambhajinagar','Dhule','A.Nagar')
# data2 = list(data)
# data2.insert(5,'Mumbai')
# print(data2)
# data = tuple(data2)
# print(data)
# print(type(data))

#set
#unordered, unchangeable and unindexed Collection
# data={10,20,10,30,40,22,50}
# print(data)
# print(type(data))

#we cn't access using index set items we use for loop
# for i in data:
#     print(i)

# # data.add(77)
# print(data)

# data2={20,40,55,39}
# data.update(data2)
# print(data)

# data.remove(55)              #if value not present gives key error
# print(data)

# data.discard(30)         #if value not present not give any error
# print(data)

# print("popped item is",data.pop())
# print("popped item is",data.pop())

# data.clear()
# print(data)

#del keyword
#remove whole set
# del data

# data1 = {30,20,40,60,80}
# data2 = {40,30,66,80,45}
# data3 = data1.union(data2)
# print(data3)

# data1.update(data2)
# print(data1)

# data3 = data1 | data2
# print(data3)

# data1.intersection_update(data2)
# print(data1)

# data1.intersection_update(data2)
# print(data1)

# 
# data3 = data1 - data2
# print(data3)

# data1.difference_update(data2)
# print(data1)

# data3 = data1.symmetric_difference(data2)
# print(data2)

# data3 = data1 ^ data2
# print(data3)

# data1.symmetric_difference_update(data2)
# print(data1)



#Dictionary
#store key : value pair access using keys
#dictionary is ordered and changeable collection, does not allow duplicate keys
#  we can update values using keys also have update()

data = {"name": "Aniket", "surname" : "Chafekar" , "Education" : "Bachlore's" , "Address" : "Chh. Sambhajinagar"}
# print(data)
# print(type(data))

# print(data.keys())
# print(data.values())
# print(data.items())

# data.update({"age" : 21})
# data.update({"college" : "kkw Nashik"})
# print(data)

# data["cgpa"] = 8.68   #we can add data using assigning value to dicti.
# print(data)

# data.pop("cgpa")     #remove specified keys value
# print(data)

# data.popitem()    #remove last inserted item
# print(data)

# del data["surname"]   #delete using del keyword with specified key
# print(data)

# del data               #delete dictionary
# print(data)

# data.clear()         #clear all data dictionary structure remain {}
# print(data)

#for copying Dictionary copy(), dict()
# data2 = data.copy()
# print(data2)

# data2.popitem()
# print(data2)
# print(data)

# data2 = dict(data)

# data2.pop("name")
# print(data2)
# print(data)

#it is aliasing if we change in anyone it reflect to other 
# data2 = data

# data2.popitem()
# print(data2)
# print(data)

#fromkeys()  returns a dictionary with the specified keys and value 
#use for intializing value to any value by default is None
# ex
# products = ["Watch" , "Mobile" , "Earphones"]
# inventory = dict.fromkeys(products, 0) 
# print(inventory)

#place element startwith A in another list and all into another
# arr = ["Aniket" , "Rahul" , "Chirag" , "Ram" , "Suresh" , "Pravin"]
# arr2 = []
# arr3 = []
# for i in arr:
#     if i.startswith('A'):
#         arr2.append(i)
#     else:
#         arr3.append(i)


# print(arr3)
# print(arr2)


#Conditional statements
#1. if
#2. if else
#3. elif ladder
#4. match Statement (switch like)

# a = -1
# if a>0: print("positive Number")

# print("Positive Number") if a>0 else print("Negative Number")

# username = "abc"
# password = "abc@123"
# if username == "abc" and password == "abc@123":
#     print("Login Successfully")
# else:
#     print("invalid Credentials")

# name = "Aniket"
# bloodgroup = "O"
# if name == "Aniket" or bloodgroup == "B+":
#     print("Welcome")
# else:
#     print("Thanks")

# a = 20
# b = 19
# if not a == b:
#     print("true 1")
# else:
#     print("false 1")

#elif ladder
# num = 10
# if num < 0:
#     print("Negative Number")
# elif num > 0:
#     print("positive Number")
# else:
#     print("Number is zero")

#Match Statement

# status = 204
# match status:
#     case  404:
#         print("Not Found")
#     case 400:
#         print("Bad Request")
#     case 200:
#         print("Success")
#     case 204:
#         print("No Content")
#     case 500:
#         print("Server Error")
#     case 503:
#         print("Service Unavailable")
#     case _:                                    #default case
#         print("Invalid status")

# name = input("Enter name :")
# age = int(input("Enter Age :"))
# match name:
#     case "Aniket" | "Viki" | "Rushikesh" if age > 19:
#         print("student in class number is 302")
#     case "Chirag" | "Pravin" | "Mohan" if age > 19:
#         print("Student class number is 201")
#     case _:
#         print("Wrong Student Name Entered !")

#Loops
'''1) for loop
2)while loop
'''
marks = [66,78,45,98,77,66]
# for i in marks:
#     print(i,end=" ")

# print()
# name = "Aniket"
# for i in name:
#     print(i,end=" ")

# for i in marks:
#     if i == 98:
#         break      #stop iteration at that time
#     print(i)

names = ["Aniket", "Viki", "Harsh", "Raj"]
# for i in names:
#     if i == "Viki":
#         continue           #skip current iteartion move to the next ite.
#     print(i)

# for i in names:
#     print(i)
# else:
#     print("loop Completed")

#While loop
# i=1
# while (i<=20):
#     if i == 10:
#         break
#     print(i,end=" ")
#     i+=1

# i=0
# while(i<20):
#     i+=1
#     if i==5:
#         continue       #skip current move to next ite.
#     print(i)

# for i in range(5):
#     for j in range(5):
#         pass         #use for syntactically don't want to execute 
        #logic not decided yet

#Functions
# A function is a block of code which runs when we call that function by object
# we can pass data to functions is called parameters, a fuction can return data as a result
'''def Keyword is used for declartion of a function
syntax = def fun_name(arguments):
              func_logic
              
for fuction we have to call it then it will be Executed
for calling 
syntax = func_name()'''

# def func(name):
#     print(name)

# func("Aniket")
# func("Viki")

#if we don't known how many arguments are passed  we can use *args store in a tuple
# def func(*args):
#     print("Names are :",args)
#     print(args[2])

# func("Aniket","Ravindra","Niraj","Sagar")

#keyword Argument
# pass data in arguments as key value pair
# def func(marks1,marks2,marks3):
#     print("Marks 1 are",marks1)
#     print("Marks 2 are",marks2)
#     print("Marks 3 are",marks3)

# func(marks2 = 80,marks3 = 45,marks1 = 90)

# variable length keyword arguments
# **kwargs
# def func(**kwargs):
#     print("first name :",kwargs["firstname"])
#     print("middle name :",kwargs["middlename"])
#     print("surname :",kwargs["surname"])

# func(firstname = "Aniket", middlename = "Sopan ", surname = "Chafekar")

#default parameter
#we can assign default value to parameter if value not passed in argument it takes default value
# def func(college = "KKW"):
#     print("College name is :",college)

# func("KTHM")
# func()

# we can pass any sequence to function also

# def func(centers):
#     for i in centers:
#         print("Center name is ",i)

# location = ["Pune","Mumbai","Banglore","Heydrabad","Delhi","Nashik"]
# func(location)

#function can return results using return keyword (in other languages we can return single value result in python
#  sequence also we can return as a result)

# def func():
#     a = 45
#     b = 12
#     c = a+b
#     return c

# num = func()
# print(num)

# 1) Function with no parameters and no return
# 2) function with parameters and no return
# 3) functiom with no parameters and return Value
# 4) function with parameters and return value

  
#function decorator means we add some additional functionality to the existing function without modifying that function using @ annotation
# we add some extra features to it
# syntax:
'''@decorator_name
def function_name():
    #code'''

# def greetings(fx): 
#     def greet():       
#         print("Good Morning.!")       
#         fx() 
#         print("Thank you for using function.!") 
#     return greet 

# @greetings 
# def func():  
#     print("Hello World.!")

# func()

# def message(fx):
#     def greet():
#         print("you have a Good day")
#         fx()
#         print("Thanks For Visiting")
#     return greet

# @message
# def f1():
#     print("hello Welcome to Fct")

# f1()

    

#Modules in python
# A group of functions, variables and classes saved to a file is called a Module.
# .py file is act as a module

#various ways to import module 
# import math
# print(math.lcm(20,30))

# import math as mt                 #Renaming to math as mt we also give to fuctions and properties
# print(mt.lcm(30,40))

# from math import lcm
# print(lcm(30,50))

# from math import lcm as l
# print(l(50,70))

# from math import *
# print(lcm(20,30))
# print(pi)
# print(ceil(8.1))
# print(floor(3.9))
# print(factorial(5))
# print(perm(5,2))
# print(gcd(12,18))
#sin, cos, tan, asin, acos, atan

# from math import lcm,fsum

# from math import lcm as l, fsum as f    #member aliasing

from random import *
# print(randint(1,20))

# li = [10,20,30,40,50,60]
# print(choice(li))

# for i in range(2):
#     print(random())       #return number 0 to 1 , 1 is excluded

# for i in range(2):
#     print(uniform(1,29))       # return a random float number in given range

# for i in range(5):
#     print(randrange(1,10))        #returns a random number
 
# for i in range(5):
#     print(randrange(0,20,2))            #start,stop,step

# file Handling
#we use file handling for storing our data permentantly for future purposes.

# two types of file
# 1) text File    use for storing text data   .txt extension is used
# 2) Binary File    use for storing data Binary files data audio, video, images

# file_handle = open(filename, mode)

# f = open("file2.txt", 'w+')
# # data = f.read(5)
# print(data)

# f.write("Hello sir, Good Morning thanks for giving me this opportunity")

# data = f.read()
# print(data)

# f.close()

#modes are 
'''
r = for reading file if file not exist gives error 'FileNotFoundError'
w = for write it also create a file if not exist
a = open an exisiting file for append operation add data to last if file is not present create a file
r+ = read + write it doesn't override the existing data insert data at the starting of the file
w+ = write + read it overrides existing data in the file
a+ = append + read data from existing file it not override file pointer at end of file  
x = to create exclusive a new file only, if file alredy exist gives error'''

# for binary add suffix b to all file modes a rb, wb, xb, xb+ etc

#with statement in file file -> we doen't care about closing a file

# with open("file2.txt",'r') as f:
#     data = f.read()
#     print(data)
# print(f.closed)

#tell() and seek() methods

# tell() -> used to find the pointer position of the cursor,by default at zero
# seek() -> we use seek method for move cursor (file pointer) to any location in the file

# f = open("file2.txt", 'r+')
# print(f.tell())
# data = f.read()
# print(f.tell())

# f.close()

# with open("file2.txt" , 'w+') as f2:
#     f2.write("hi how are you, Good Morning")
#     f2.seek(10)
#     data = f2.read()
#     print(data)

# How to check if a file is present or not ?
# import os
# print(os.path.isfile('file2.txt'))





























