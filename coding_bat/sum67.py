"""
Challenge:

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the
next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) --> 5
sum67([1, 2, 2, 6, 99, 99, 7]) --> 5
sum67([1, 1, 6, 7, 2]) --> 4
"""


def sum67(nums):
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
        if nums[i] == 6:
            nums[i] = 0
            for j in range(i, len(nums)):
                temp_num = nums[j]
                nums[j] = 0
                if temp_num == 7:
                    i = j + 1
                    break
    return sum(nums)

print sum67([1, 2, 2])
print sum67([1, 2, 2, 6, 99, 99, 7])
print sum67([1, 1, 6, 7, 2])