# d={'a':"aplause",'Id':17,'fname':"Aniket",34:"homeno"}
# print(d)
# print(type(d))

# d['Id']=200
# print(d)

# d['f']="fan"
# print(d)

# d['rollno']=17
# print(d)

# d=eval(input("Enter a Dictionary:"))
# print(d)
# print(type(d))

d={'a':"Aniket",'rollno':17,'lname':"Chafekar",20:"yes"}
# print(d)

# for k in d:
#     print(k,":",d[k])

#n number students rollno and percentage using dict
# n=int(input("Enter number of students : "))
# d={}
# for i in range(n):
#     rno=input("Enter student rollno :")
#     per=input("Enter percentage : ")
#     d[rno]=per

# # print(d)
# for i in d:
#     print("rollno : ",i)
#     print("Percentage is : ",d[i])

# d={'Aniket':[40,65,78],'Shantanu':[65,89,90]}
# print(d)

#deleting key
# del d['Aniket']
# print(d)

# d.clear()
# print(d)

#list of tuple to dict using dict()
# d=dict([(10,'Aniket'),(20,'Amit'),(50,'Rahul')])
# print(d)
# print(type(d))

# d=dict({1:"Aniket",2:"Viki"})
# print(d)
# print(type(d))

# x=d.pop('rollno')
# print(x)  #specified element

# x=d.popitem()
# print(x) #last lelement with pair

# x=d.get('a')
# print(x)  #if key is not present gives None value

# x=d.get('f',0)
# print(x) #if key is not present give default value

# x=d['f']
# print(x)  #keyerror