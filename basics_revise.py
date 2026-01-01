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

students=["Amit","Chirag","Akash","Sagar","Uday","Aniket"]
print(students[2])

print(len(students))

list2=['Ram',25,8.90,'Aniket',True,[10,49,80],('Chafekar',51)]
print(list2[5])

tup=('Chafekar',51)
print(type(tup))
list=list(tup)
print(type(list2))




