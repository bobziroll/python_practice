"""
Challenge:

Check to see if a given string is a palindrome. The strings may contain capital letters and non-alphabetic characters.

is_palindrome("I am a string") --> False
is_palindrome("I, madam; I made radio. So I dared! Am I mad?? Am I??!?!") --> True
is_palindrome("Star. rats") --> True
"""


# Possible solution #

# def is_palindrome(string):
#     for index, let in enumerate(string):
#         if let != string[-index - 1]:
#             return False
#
#     return True

# Problem with this solution is that it uses a for loop when it doesn't need one, since you could simply do:
# def is_palindrome(string):
#     return string == string[::-1]
# AND it still doesn't catch punctuation or capitalization


# New Solutions #

# def is_palindrome(s):
#     normalized_string = ''
#     for let in s:
#         if let.isalpha():
#             normalized_string += let.lower()
#     return normalized_string == normalized_string[::-1]

# The above works great! One thing that could be better for modularity is to make a helper function that
# does the "normalization" for you. Example below.


# def normalize_string(s):
#     normalized_string = ''
#     for let in s:
#         if let.isalpha():
#             normalized_string += let.lower()
#     return normalized_string
#
#
# def is_palindrome(s):
#     return normalize_string(s) == normalize_string(s)[::-1]
#
#
# string1 = "I, am: a ;string"
# string2 = "Mad:am"
# string3 = "Star. rats"
# string4 = "I, madam; I made radio. So I dared! Am I mad?? Am I??!?!"
# string5 = "I, madam; I made radio. So I dared! Are you mad?? Are you??!?!"
#
#
# print is_palindrome(string1)  # False
# print is_palindrome(string2)  # True
# print is_palindrome(string3)  # True
# print is_palindrome(string4)  # True
# print is_palindrome(string5)  # False


# Old Solution #

# def normalize_string(s):
#     lower_case_string = s.lower()
#     no_spaces_string = lower_case_string.replace(' ', '')
#
#     letters_list = []
#     for let in no_spaces_string:
#         if let.isalpha():
#             letters_list.append(let)
#     final = ''.join(letters_list)
#     return final
#
#
# def reverse_string(s):
#     normalized_string = normalize_string(s)
#     reversed_string = normalized_string[::-1]
#     return reversed_string
#
#
# def is_palindrome(s):
#     return normalize_string(s) == reverse_string(s)
