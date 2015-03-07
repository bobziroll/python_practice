"""
Challenge:

Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any
letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') --> 1
count_code('codexxcode') --> 2
count_code('cozexxcope') --> 2
"""


def count_code(str):
    count = 0
    for i in range(len(str)-1):
        try:
            if str[i] == "c":
                if str[i + 1] == "o" and str[i + 1]:
                    if str[i + 2]:
                        if str[i + 3] == "e" and str[i + 3]:
                            count += 1
        except IndexError:
            return count
    return count

print count_code('aaacodebbb')
print count_code('codexxcode')
print count_code('cozexxcope')
print count_code('cozexxco')