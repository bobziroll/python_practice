"""
Challenge:

Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') --> True
end_other('AbC', 'HiaBc') --> True
end_other('abc', 'abXabc') --> True
"""


def end_other(a, b):
    if len(a) > len(b):
        return b.lower() in a[-len(b):].lower()

    elif len(b) > len(a):
        return a.lower() in b[-len(a):].lower()

    else:
        return a.lower() == b.lower()

# Coding Bat's solution is better:

# def end_other(a, b):
#   a = a.lower()
#   b = b.lower()
#   return (b.endswith(a) or a.endswith(b))