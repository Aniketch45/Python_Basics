def sum(x):
   if x==5:
      s=5
   else:
      s=x+sum(x+1)
   return s
   
res=sum(1)
print("sum of first 5 numbers is : ",res)
print("hello")