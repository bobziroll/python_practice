"""
Return True if the string "cat" and "dog" appear the same number of times in the given string. 

cat_dog('catdog') --> True
cat_dog('catcat') --> False
cat_dog('1cat1cadodog') --> True
"""


def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(len(str)-1):
        if str[i:i+3] == "cat":
            cat_count += 1

    for i in range(len(str)-1):
        if str[i:i+3] == "dog":
            dog_count += 1

    if cat_count == dog_count:
        return True
    return False

print cat_dog('catdog')
print cat_dog('catcat')
print cat_dog('1cat1cadodog')