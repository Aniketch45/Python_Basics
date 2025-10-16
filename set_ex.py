#1)create set of square of even numbers from 1 to 20

# s={i*2 for i in range(0,21,2)}
# print(s)

#print vowels in given string using set
s=set(input("Enter a string : "))
vowel="AEIOUaeiou"
s.intersection_update(vowel)
print("vowels present in a string : ",s)
