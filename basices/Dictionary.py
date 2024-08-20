data = {1:"priyank" , 2:"jay" , 4:"khush"}
print(data)

print(data[1])

print(data.get(2,"Not Found"))
print(data.get(3,"Not Found"))

keys = [1 , 2 , 4]
values = ["priyank" , "jay" , "khush"]
data = dict(zip(keys,values))
print(data)


data[3] = "guniyes"
print(data)

del data[4]
print(data)

# help()