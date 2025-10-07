def show(**kwargs):
    for key,value in kwargs.items():
        print(f"key is {key} and value is {value}")

    

show(empn0=101,empname="Tom",empsal=40000)