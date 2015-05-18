def checkio(data):
    my_list = data
    for item in my_list:
        if data.count(item) == 1:
            my_list.remove(item)

    return my_list

print checkio([1, 2, 3, 4, 5])