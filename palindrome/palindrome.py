def normalize_string(s):
    lower_case_string = s.lower()
    no_spaces_string = lower_case_string.replace(' ', '')

    letters_list = []
    for let in no_spaces_string:
        if let.isalpha():
            letters_list.append(let)
    final = ''.join(letters_list)
    return final


def reverse_string(s):
    normalized_string = normalize_string(s)
    reversed_string = normalized_string[::-1]
    return reversed_string


def palindrome(normalized, reversed_string):
    return normalized == reversed_string


string1 = "I, am: a ;string"
string2 = "Mad:am"
string3 = "Star. rats"
string4 = "I, madam; I made radio. So I dared! Am I mad?? Am I??!?!"
string5 = "I, madam; I made radio. So I dared! Are you mad?? Am I??!?!"


print palindrome(normalize_string(string1), reverse_string(string1))
print palindrome(normalize_string(string2), reverse_string(string2))
print palindrome(normalize_string(string3), reverse_string(string3))
print palindrome(normalize_string(string4), reverse_string(string4))
print palindrome(normalize_string(string5), reverse_string(string5))
