# l=[i*i for i in range(10000000)]
# print(l)
# it takes more meemory give mermory error and hang for overcome

#we use Generator it generates value stored in genrator object by using yield and access using next
# we cant iterate back to geneartor it gives error
def gen1(num):
    n=1
    while(n<=num):
        yield n
        n+=1

g=gen1(5)
print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

l1=list(next(g) for i in range(5))
print(l1)





