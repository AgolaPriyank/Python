class student:
    
    def sum(self, a= None, b = None,c = None):
        s=0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        
        elif a!=None and b!=None:
            s=a+b
            
        elif a!=None:
            s=a
            
        return s
    
    
s1 =student()
print(s1.sum())