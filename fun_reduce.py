#reduce() function perform operation on one list and returns its one elemnet by applyinf operation

from functools import reduce;
# l=[1,4,2,67,54]
# res=reduce(lambda x,y:x+y,l)
# print(res)

# prod=reduce(lambda x,y:x*y,l)
# print(prod)

sum=reduce(lambda x,y:x+y,range(1,101))
print(sum)


















