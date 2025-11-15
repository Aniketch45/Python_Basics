# for i in range(3):
#     for j in range(2):
#         print("Hello",end=" ")
#     print()


'''Q) star pattern'''

# for i in range(3):
#     for j in range(i+1):
#         print(" *",end="")
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print(i,end="")
#     print()

for i in range(1,5): 
    for j in range(i//2):
        if j==2:
        print("*",end=" ")
    
   
# ''' * * * *
#     *     *
#     *     *
#     * * * *

#     * 
#     * *
#     1 2 3 
#     * * * *

# for i in range(1,5): //ok
#     for j in range(i):
#         if(i==3):
#             print(j+1,end=" ")
#         else:
#             print("*",end=" ")
#     print()