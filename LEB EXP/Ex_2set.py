set1 = {1,2,3,4,5,6,7,8,9,10}
print(set1)

set2 = {2,4,6,8,10}

set3 = {1,3,5,7,9}

print(set2.union(set3))
print(set2.intersection(set1))
print(set1.difference(set2))

print(set1.issuperset(set2))
print(set2.issubset(set1))

set1.add(99)
print(set1)

set1.remove(9)
print(set1)

set1.discard(99)
print(set1)

set1.add(99)
print(set1)
set1.add(99)
print(set1)

set1.pop()
print(set1)