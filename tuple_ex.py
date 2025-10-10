#write a prog to take tuple of numbers from the keyboard and print its sum and Average
t1=eval(input("Enter a numbers : "))
sum=0
for i in t1:
    sum+=i

len=len(t1)
avg=sum/len
print(sum)
print("Average is",avg)


