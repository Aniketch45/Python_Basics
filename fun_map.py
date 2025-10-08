# function map()

# def sq(n):
#     return 2*n

# l1=[2,6,8,7,5,3,99]
# res=list(map(sq,l1))
# print(res)

# res=list(map(lambda n:2*n,l1))
# print(res)

l1=[2,6,8,7,5,3,99]
l2=[4,6,7,3,56,76,23]
# res=list(map(lambda x,y:x+y,l1,l2))
# print(res)

def add(x,y):
    return x+y

res=list(map(add,l1,l2))
print(res)
