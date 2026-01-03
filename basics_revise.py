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

name = input("Enter name :")
age = int(input("Enter Age :"))
match name:
    case "Aniket" | "Viki" | "Rushikesh" if age > 10:
        print("student in class number is 302")
    case "Chirag" | "Pravin" | "Mohan" if age > 10:
        print("Student class number is 201")
    case _:
        print("Wrong Student Name Entered !")




