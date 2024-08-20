import sys


def count(a):
    even = 0
    odd = 0
    
    for i in a:
        if i%2 == 0 :
            even += 1
        
        else :
            odd += 1
            
    return even , odd
    
     


lis = [10,5,64,58,65,87,66]

even,odd = count(lis)

print("no of even = ", even)
print("no of odd = ", odd)  

print("Even : {} and odd : {}".format(even,odd))


# sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())