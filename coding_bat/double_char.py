"""
Given a string, return a string where for every char in the original, there are two chars. 

double_char('The') --> 'TThhee'
double_char('AAbb') --> 'AAAAbbbb'
double_char('Hi-There') --> 'HHii--TThheerree'
"""


def double_char(str):
    let_list = []
    for let in str:
        let_list.append(let)
        let_list.append(let)
    result = ''.join(let_list)
    return result


# CodingBat's Solution is better:

# def double_char(str):
#     result = ""
#     for i in range(len(str)):
#         result += str[i] + str[i]
#     return result
