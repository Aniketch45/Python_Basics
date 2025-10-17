def demo():
    l=eval(input("Enter a list : "))
    ls=list(map(int,l.split()))
    l1=sorted(ls)
    l2=list(reversed(ls))

    print("Original List is : ",ls)
    print("Sorted List is : ",l1)
    print("Reversed list is : ",l2)

demo()

