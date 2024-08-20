nums = [25 , 68 , 73 , 42 , 22 , 90]
print(nums)

nums.append(99)
print(nums)

nums.sort()
print(nums)

nums.extend([60 , 55])
print(nums)

nums.remove(60)
print(nums)

nums.pop(2)
print(nums)

print(min(nums))

print(max(nums))

nums[0] = 30
print(nums)