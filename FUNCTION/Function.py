# def sum(x,y):  # formal arguments
#     c = x+y
#     return c

# sum = sum(5,5)  # akchul arguments
# print(sum)

def sum_sub(x,y):
    c = x+y
    d = x-y
    return c,d

sum1,sub1 = sum_sub(5,5)
print(sum1 , sub1)

# function in python is not follow pass by value nor pass by refrances 
# primativ data type are immutebal that create a new object not change its value  / in function call that not change it's orignal value that change in only in function variabal value create new object
# mutebl (list) change it's orignal value


# variabal argument

def sum(*a):
    sum = 0
    print(a)
    
    for i in a:
        sum= sum+i
    
    print("sum = ",sum)
    

sum(5,5,10,20)

# variabal argument pass using  with keywords

def persion(name , **data):
    
    print(name)
    print(data)
    
    for i,j in data.items():
        print(i ,j)
    
    
persion("priyank" , age=19 , city="surendrnagar" , mob = 3441314577)

# in function use global variabal thats diclar it's as global
# dikled as      global variabla_name
# EX = global a
# but in this we can not create same name local  variabal in function

a = 10

def ren():
    a = 9
    
    print("in fun = ", a)
    
    globals()['a'] = 15
    

ren()

print("outside = " , a)


