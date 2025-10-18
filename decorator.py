#we use decorator to add additonal functionality to func without changing it

# def decorator(func):
#     def inner(n1,n2):
#         if n2==0:
#             print("Not Divisible by zero")
#         else:
#             func(n1,n2)
#     return inner

# @decorator
# def func1(x,y):
#     div=x/y
#     print(div)

# func1(10,20)
# func1(30,0)

#Chaning of decorators is allowed
# def decorator(wish):
#     def inner(name):
#         print("first decor execution")
#         wish(name)
#     return inner

# def decorator1(wish):
#     def inner(name):
#         print("second decor execution")
#         wish(name)
#     return inner

# @decorator
# @decorator1
# def wish(name):
#     print("hello",name,"Good Morning")


# wish("anand")
 