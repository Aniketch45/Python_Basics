input='1-3,5,7-9'
nlist=[]
l1=input.split(",")
print(l1)

for item in l1:
    if '-' in item:
        s=item.split('-')
        print(s)
        for x in range(int(s[0]),int(s[1])+1): #1,(3+1)4   prints 1,2,3  4 excluded
            nlist.append(x)
    else:
        nlist.append(int(item))

print(nlist)