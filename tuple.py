#tuple
#creating
# t1=tuple(range(10,40))
# print(t1)

#type casting
# l1=[10,20,70,30,90]
# t1=tuple(l1)
# print(t1)
# print(type(t1))

#FOR safe data take in program might path given like command that harms code in hacking
# import ast
# t1=ast.literal_eval(input("Enter values for tuple:"))
# print(t1)
# print(type(t1))

#empty
# t1=()
# print(t1)
# print(type(t1))

# without parenthesis
# t1=10,20.90,89,'Aniket',57
# print(t1)
# print(type(t1))

#intialize
# t1=(10,20,30,40)
# print(type(t1))

#Accessing
# t1=(10,20,"Aniket",70,50.60)
# print(t1[2])
# print(t1[-1:-4:-1])

# for x in t1:
#     print(x)

# t1[2]=100 //error beacause tuple is immutable

#mathemat op

# t1=(10,40,50,80)
# t2=("Aniket",30)
# print(t1+t2)  //concatenation

# print(t1*3)  //Repetation

#functions
t1=(10,40,50,80,10,5,90)
# print(len(t1))

# print(t1.count(5))

# print(sorted(t1))
# print(t1)
# t2=sorted(t1,reverse=True)
# print(t2)  #returns list

# print(min(t1))
# print(max(t1))


#packing & unpacking
# a,b,c=2,5,6
# t1=a,b,c
# print(t1)

# t2=(20,40,50,30)
# a,b,c,d=t2
# print(f"{a},{b},{c},{d}")  #less or more arg gives ValueError

#tuple comprension
t1=(x*x for x in range(1,6))
# print(t1) #generator object returns in tuple only
# print(type(t1))
# for x in t1:
#     print(x)


l1=[x*x for x in range(1,6)]
print(l1)

