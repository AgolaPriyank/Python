d1 = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
}
print(d1)

print(d1.keys())
print(d1.values())
print(d1.items())

print(d1.get(2))

print(len(d1))

d2 = {
    1:{'odd','even'},
    2:{'priyank' , 'uttam'}
}
print(d2)

d2.update({3:'shyam'})
print(d2)

d2.pop(3)
print(d2)

d3 = d2.copy()
print(d3)

d2.clear()
print(d2)



