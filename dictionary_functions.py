d={'a':"Apple",'b':"Banana",'m':"mango",'n':34,56:"welcome"}
# print(d)
# print(id(d))
# print(type(d))

# item=d.items()
# print(item)

# for k,v in d.items():
#     print(f"key :{k} value :{v}")

# d2=d.copy() // clone that dict only changes in one not Appear in second
# d['d']='dog'
# print(d)
# print(d2)

# d2=d //aliasing address same we change in one reflect to other
# d['c']="cat"
# print(d)
# print(d2)

# print(d.keys())
# for k in d.keys():
#     print(k)

# print(d.values())
# for v in d.values():
#     print(v)

# info={'Ram':{'eng':45,'math':89,'history':78},'ramesh':{'eng':56,'math':79,'history':70}}
# print(Ram['eng'])

d={'a':"Apple",'b':"Banana",'m':"mango",'n':34,56:"welcome"}
# d.setdefault('g','Bat')
# print(d)           //if key is present in dict it returns dict value if key is not pressent
                     #//it adds given key value pair

# d3={12:'tu','one':78}
# d.update(d3)   #updates add all to the dest.
# print(d)

#comprehension
# d={ x:x*x for x in range(1,6)}
# print(d)

#q) program to find vowels present in string and count of vowels
# st="hi hello how are you"
# s={'a','e','i','o','u'}
# d={}
# for x in st:
#     if x in s:
#         d[x]=d.get(x,0)+1
# for k,v in sorted(d.items()):
#     print(k," occured ",v,"times")

#q) write a program to find number of occurences of each letter present in the given string?
# word=input("Enter a string : ")
# d={}
# for i in word:
#     d[i]=d.get(i,0)+1

# for k,v in d.items():
#     print(k," occured ",v," times")

d=eval(input("Enter dictionary:"))
s=sum(d.values())
print(s)
    
