class Gparent:
    def show(self):
        print("hello Gparent")

class Child1(Gparent):
    pass
    # def show(self):
    #     print("hello Child1")

class Child2(Gparent):
    pass
    # def show(self):
    #     print("hello Child2")

class Gchild(Child1,Child2):      #in python we didn't get Daimond Problem because MRO (Method Resolution order) in other languager we use like java interface 
    pass
    # def show(self):   
    #    print("hello Grand Child")                                       
                                                            #     A
                                                            #    / \
                                                            #   B   C
                                                            #    \ /       D confuse to access A content in both its childs
                                                            #     D
    

obj=Gchild()
obj.show()

