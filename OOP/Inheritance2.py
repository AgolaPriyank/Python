
class A:

    def __init__(self,a1):
        print("in A Init")
        self.a1 = a1

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")

class B:

    def __init__(self):
        # super().__init__()
        print("in B Init")

    def feature1(self):
        print("Feature 1-B working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):

    def __init__(self,a1,c1):
        super().__init__(a1)
        print("in C init")
        self.c1 = c1
        
        


    def feat(self):
        super().feature2()
        super().feature1()
        

obj1 = C('priyank',20)
obj1.feat()
print("a1 ", obj1.a1)
print("c1 ", obj1.c1)
