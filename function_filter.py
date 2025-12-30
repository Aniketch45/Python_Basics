# l1=[10,40,45,67,3,2,8,6,22]

# even=list(filter(lambda n:n%2==0,l1))
# print(even)

l2=['t','u','t','o','r','i','a','l']
# # res=list(filter(lambda x:x!='t',l2))
# # print(res)

def fun1(x): 
    if x!='t':
        return True
    else:
        return False

res=list(filter(fun1,l2))
print(res)

# list1=[10,15,5,20,37,12]
# list2=[11,20,55,15]

# ans=list(filter(lambda x:x not in list2,list1))
# print(ans)

# l=[10,3,44,23,41,7,9,12]
# odd=list(filter(lambda a:a%2!=0,l))
# print(odd)