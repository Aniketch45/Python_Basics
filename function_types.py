#function with no return & no arguments
#function with return & no arguments
#function with no return & arguments
#function with return & arguments

#1)
# def demo():
#     x,y=10,5
#     z=x+y
#     print(z)

# demo()
# d=demo()
# print(d)  #None

#2)
# def demo():
#     x,y=10,5
#     z=x+y
#     return z

# z=demo()
# print(z)

#3)
# def demo(x,y):
#     x,y=10,5
#     z=x+y
#     print(z)

# demo(10,5)

#4)
# def demo(x,y):
#     x,y=10,5
#     z=x+y
#     return z

# s=demo(10,5)
# print(s)

#types of arguments
#1)Positional argument
#2)Keyword argument
#3)Default argument
#4)Variable Length argument

# def funarg(a,b,kw):   #Positional arguments
#     print(a+b)

# funarg(10,20,kw="hello") #keyword argument
#first positional then keyword iif not then synatx error positinal arguments follow keyword arg


#default arg
# def funarg(a,b,name="Aniket"):
#     print(name,":",a+b)

# funarg(30,20)
# funarg(10,20,"Viki") #If we are not passing any arguments then only default value will be considered.

#variable length arg   
# def sum(*n):
#     total=0
#     for i in n:
#         total+=i
#     print("Sum is : ",total)

# sum()
# sum(20,20)
# sum(10,40,60,4)

# def vlarg(a,*s):
#     res=0
#     for i in s:
#         res+=i
#     print(a,"sum is : ",res)

# vlarg("Aniket")
# vlarg("Aniket",30,70)

# def fun1(*s,name):   #After variable length argument, if we want to provide positional argument 
#     mul=1            #then compulsurily we have to provide those values as keyword arguments only
#     for i in s:
#         mul*=i
#     print(name,mul)   

# fun1(name="Aniket")
# fun1(19,9,name="mohit")

# variable lenght keyword argument
def display(**kwargs):
    for k,v in kwargs.items():
        print(k," : ",v)

display(rno=17,name="Aniket",std="fy Msc",subject="Python")
print("////////////////////////")
display(rno=17)