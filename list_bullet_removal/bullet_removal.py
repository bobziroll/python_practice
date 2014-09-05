def get_list():
    my_list = []

    with open('list.txt') as f:
        for line in f:
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            my_list.append(row)
    return my_list


def remove_numbers(list):
    with open('list.txt') as f:
        pass