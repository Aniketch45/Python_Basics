#calling function using return and aliasing //in outer of greet function
# def greet():
#     print("Hello Welcome to Pune")
#     def inner():
#         print("the City")
#     print("Thanks for visiting")
#     return inner

# inn=greet()
# print("test")
# inn()


#calling inner in inside greet function

# def greet():
#     print("Hello Welcome to Pune")
#     def inner():
#         print("the City")
#     inner()
#     print("Thanks for visiting")

# greet()
 
def greet():
     print("Hello Welcome to Pune")
     def inner():
        print("the City")

     print("Thanks for visiting")
     return inner

# f1=greet
# f1()
f1=greet()
f1()



