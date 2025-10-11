#union
# s1={10,20,40,50}
# s2={40,50,60,90}
# s1=s1.union(s2)
# s1.update(s2)

# print(s1|s2)
# print(s1)

#intersection

s1={10,20,40,50}
s2={40,50,60,90}
# s1=s1.intersection(s2)
# s1.intersection_update(s2)
# print(s1&s2)
# print(s1)

#difference  //returns element in first not in 2nd
# s1=s1.difference(s2)
# s1.difference_update(s2)
# print(s1-s2)
# print(s1)

#symmetric retuns all elemts that are diffrent in each
# s1=s1.symmetric_difference(s2)
# s1.symmetric_difference_update(s2)
# print(s1^s2)
# print(s1)


# s={i*i for i in range(0,51,2)}
# print(s)

#Q write a program to print vowels present in  the given  word?
w=input("Enter a string : ")
s=set(w)
v={'a','e','i','o','u','A','E','I','O','U'}
s.intersection_update(v)
print("the vowel presnt in",w,"are",s)