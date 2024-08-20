a =2
b = 0

try:
    print("resources open")
    print(a/b)
    
except ZeroDivisionError as e:
    print("you can not divided num by zero ")


try:   
    k = int(input("Enter number : "))
    print(k)
    

    
except ValueError as e:
    print("Invalid input" , e)
    
except Exception as e:
    print(e)
    
finally:
    print("resources close")