"""
Challenge:

Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) --> True
has22([1, 2, 1, 2]) --> False
has22([2, 1, 2]) --> False
"""


def has22(nums):
    if 2 in nums:
        for i in range(len(nums)):
            if nums[i] == 2:
                try:
                    if nums[i+1] == 2:
                        return True
                except IndexError:
                    return False
    return False

# One person's solution I found online. It's better than mine :)

# def has22(nums):
#   for i in range(0, len(nums)-1):
#     #if nums[i] == 2 and nums[i+1] == 2:
#     if nums[i:i+2] == [2,2]:
#       return True
#   return False


print has22([1, 2, 2])
print has22([1, 2, 1, 2])
print has22([2, 1, 2])