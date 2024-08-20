mark = [50 , 69 , 87 , 31 ,79]
print(mark)

mark.append(40)
print(mark)

mark.sort()
print(mark)

mark.append(69)
print(mark)

mark.remove(69)
print(mark)

mark.extend([22 , 55])
print(mark)

mark.insert(1 ,80)
print(mark)



print(mark.index(80))

mark.pop(2)
print(mark)

mark.reverse()
print(mark)

mark.append(55)
print(mark)

print(mark.count(55))

# for input take from user

str = input("Enter data sepreted by coma : ")
list = str.split(',')
print(list)

