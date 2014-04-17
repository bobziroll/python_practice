def get_map():
    my_map = []

    with open('map.txt') as f:
        for line in f:
            row = []
            for char in line:
                if char != '\n':
                    row.append(char)
            my_map.append(row)
    return my_map

def get_user_input(debugMode=False):
    if debugMode:
        return 3, 5, 'S'

    x = raw_input("Enter an x coordinate: ")
    y = raw_input("Enter a y coordinate: ")
    c = raw_input("Enter a character to fill with: ")

    return x, y, c

def fill_map(map, x, y, fill_char, old_char):
    if map[y][x] != old_char:
        return
    map[y][x] = fill_char
    if x < len(map):
        fill_map(map, x + 1, y, fill_char, old_char)
    if x > 0:
        fill_map(map, x - 1, y, fill_char, old_char)
    if y < len(map[x]):
        fill_map(map, x, y + 1, fill_char, old_char)
    if y > 0:
        fill_map(map, x, y - 1, fill_char, old_char)



def print_map(map):
    for line in map:
        print ''.join(line)

### Eventually I'd like to make it so that there are coordinates that show up on the top and left of the map for reference ###

map = get_map()
x, y, c = get_user_input(debugMode=True)
fill_map(map, x, y, c, map[y][x])
print_map(map)
