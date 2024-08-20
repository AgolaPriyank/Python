from abc import ABC,abstractmethod

class computer(ABC):
    
    @abstractmethod
    def process(self):
        pass
    
    
class laptop(computer):
    
    def process(self):
        print("running in laptop")



# c1 = computer() 
l1 = laptop()  
l1.process()
    