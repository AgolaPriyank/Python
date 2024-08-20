def toptan():
    n = 1
    
    while n <= 10:
        seq = n*n
        yield seq
        n += 1
        

g = toptan()

for i in g:
    print(i)