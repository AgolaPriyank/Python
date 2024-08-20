# f = open('D:\Python\OOP\MyData.txt','r')

# print(f.readline())

# f.write("I am a B.E student")

# for data in f:
#     print(data, end = " ")

# f1 = open('D:\Python\OOP\abc.txt','r')

# for data in f:
#     f1.write(data)

# for data in f1:
#     print(data, end = " ")
    
f3 = open('D:\Python\OOP\photo.jpg', 'rb')
# print(f3.read())

f4 = open('D:\Python\OOP\myphoto.jpg', 'wb')

for d in f3:
    f4.write(d)
    
