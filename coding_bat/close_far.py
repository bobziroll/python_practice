def close_far(a, b, c):
    if abs(b - a) <= 1:
        if abs(c - a) >= 2 and abs(c - b) >= 2:
            return True
    if abs(c - a) <= 1:
        if (abs(b - a) >= 2) or (abs(b - c) >= 2):
            return True
    return False


print close_far(1, 2, 3)