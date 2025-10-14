# l1=eval(input("Enter a list Elements :")) //eval() automatically detects data list/tuple/string/list/dict
# print(l1)
# print(type(l1))


# l2=[30,60,'Aniket',10.60,True,60]
# print(l2)
# print(type(l2))

#print using for loop
# i=len(l2)
# for i in l2:
#     print(i)

# using while
# len=len(l2)
# i=0
# while i<len:
#     print(l2[i])
#     i+=1

#Q1). create a list of even numbers from 1 to 100 which are divisble by 7

# l1=[]
# for i in range(0,101,2):
#     if i%7==0:
#         l1.append(i)

#  print(l1)

#insert(pos,element) fun

# l1=[10,35,76,32,465,7]
# l1.insert(2,5)
# print(l1)
# l1.insert(-2,80)
# print(l1)

# print(l1.index(76))


#extend(sequence) fun //takes only on arg

l3=[20,10,40,30,70]
l2=[55,6,66,74,34]
# l3.extend(l2)
# print(l3)

# s1="java"
# l3.extend(s1) #seprates each character of a string in list
# print(l3)

# l3.remove(10) #element removes
# l3.pop() #last elemnt removes
# l3.clear() # clear all elemets empty list remain
# del l3 #delete list also

# l2.sort() # when sorting same datatype reqiured in list
# print(l2)

# l2.sort(reverse=True)
# print(l2)


# q) print even numbers in list
# l1=[10,20,5,7,6,8,2,4,5,9,22]
# for i in l1:
#     if i%2==0:
#         print(i)
#     i+=1

# q)using for loop print string characters
# a="Aniket"
# for i in a:
#     print(i)

# using while loop
# s="Aniket"
# len=len(s)
# i=0
# while i<len:
#     print(s[i])
#     i+=1

# print even numbers from the list
# l1=[23,4,5,66,55,33,8,2,98]
# for i in l1:
#     if i%2==0:
#         print(i)

# list functions
# count()
# insert(index,item)
# update(element)
# extend()
# remove(elemnt)
# pop() --last elemnt
# clear() all clears but [] remain empty
# del l --error 

# q) to add all elemnts to list upto 100 which are divisible by 10
l=[]
for i in range(1,101):
    if i%10==0:
        l.append(i)

print(l)
