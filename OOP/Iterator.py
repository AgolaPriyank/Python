# nums = [7,8,9,5]
#
#
# # for i in nums:
# #
# #     print(i)
#
#
# it = iter(nums)
#
# print(it.__next__())
#
# print(next(it))
#
# for i in nums:
#     print(i)


class TopTen:
    
    def __init__(self):
        self.num = 1
        
    def __iter__(self):
        return self 

    def __next__(self):
        
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        
        else:
            raise StopIteration
        

t1 = TopTen()

# print(next(t1))

for i in  t1:
    print(i)
    