nums = [21,34, 54, 12]

for num in nums:
    print(num)

for i in range(len(nums)):
    print(nums[i])

for i, num in enumerate(nums):
    print(i, num)

nums.append(32)
print(nums)

nums_1 = [45,59, 13]
nums.extend(nums_1)
print(nums)

nums.insert(4, 67)
print(nums)

del nums[0: 2]
print(nums)

#shallow copy
nums_2 = nums[:]
print("shallow copy: ", nums_2)