"""
Return the number of times that the string "hi" appears anywhere in the given string. 

count_hi('abc hi ho') --> 1
count_hi('ABChi hi') --> 2
count_hi('hihi') --> 2
"""


def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == "hi":
            count += 1
    return count


# def count_hi(str):
#     count = 0
#     for index, letter in enumerate(str):
#         if letter == "h":
#             if str[index + 1] == "i":
#                 count += 1
#     return count

print count_hi("hihellohithere")
print count_hi("nohellohere")
print count_hi("nothing")