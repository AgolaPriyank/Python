from functools import reduce


# Functions are objects in python
# anonyamas function / lambda exepresion

f = lambda a,b : a+b

result = f(5,10)
print(result)

# find even number from list uning filter

num = [4,6,8,2,3,9,7,1,5]

evens = list(filter(lambda n :n%2 == 0, num))
odds = list(filter(lambda n :n%2 != 0, num))

doubles = list(map(lambda n : n*2, evens))

sum = reduce(lambda a,b : a+b , doubles)


print(evens)
print(doubles)
print(sum)