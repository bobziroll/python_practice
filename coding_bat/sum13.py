"""
Challenge:

Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky,
so it does not count and numbers that come immediately after a 13 also do not count.

sum13([1, 2, 2, 1]) --> 6
sum13([1, 1]) --> 2
sum13([1, 2, 2, 1, 13]) --> 6
"""


def sum13(nums):
    if len(nums) == 0:
        return 0

    total = 0
    for index, number in enumerate(nums):
        if number == 13 or nums[index-1] == 13 and index != 0:
            pass
        else:
            total += number
    return total


print sum13([1, 2, 2, 1])
print sum13([1, 1])
print sum13([1, 2, 2, 1, 13])