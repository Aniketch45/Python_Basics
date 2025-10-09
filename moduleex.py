# from modules import module1 as f

# print(f.x)
# print(f.y)
# f.prod(20,30)

# from modules import module1 
# module1.prod(10,20)

# from module2 import prod,x
# prod(20,30)
# print(x)
# print(y) we cannot access 

# from module2 import *
# prod(20,67)
# print(y)
# print(x)

# import module2 as m
# m.prod(3,5)

from module2 import prod as p
p(3,4)