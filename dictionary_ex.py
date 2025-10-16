# Write a Program to accept Student Name and Marks from the Keyboard and create a Dictionary. Also display Student Marks by taking Student Name as Input?
# n=int(input("Enter the number of students : "))
# d={}
# for i in range(n):
#     name=input("Enter student name :")
#     marks=int(input("Enter student marks : "))
#     d[name]=marks

# while True:
#     name=input("Enter student name to get Marks : ")
#     marks=d.get(name,-1)
#     if marks==-1:
#         print("Student Not Found")
#     else:
#         print("the marks of",name,"are",marks)
    
#     option=input("Do you want to find another student marks [y/n] :-")

#     if option=="n":
#         break

# print("thanks for using my application")

#q) write a program to find number of occurences of each letter present in the given string?
string=input("Enter a String : ")
d={}
for i in string:
    d[i]=d.get(i,0)+1

print("The number of occurence of each leeter in string  : ")
for k,v in d.items():
    print(f"{k} Occured {v} times")