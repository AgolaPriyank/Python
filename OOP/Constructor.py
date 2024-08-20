class student:
    
    col_name = "GECR"                   # class variables
    
    def __init__(self):
        self.name = "priyank"           # instance variables
        self.age = 19                   # instance variables
        
    def compare(self,other):
        return self.age == other.age
    
    
s1 = student()
s1.age = 25
# s1.col_name = "GECB"
student.col_name = "GECB"

s2 = student()

if s1.compare(s2):
    print("both age are same")
    
else:
    print("both age are different")

print(s1.name , s1.age , s1.col_name)
print(s2.name , s2.age , s2.col_name)
    