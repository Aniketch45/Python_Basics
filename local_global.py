#local global variable
a=90
def fun1():
    global a
    a=60
    print(a)

def fun2():
    print(a)

fun1()
fun2()

#Acess variable using globals()
a=100
def f1():
    a=10
    print("local :",a)
    print("global :",globals()['a'])

f1()