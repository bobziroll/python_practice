class Map():
    def __init__(self, filename, x, y):
        self.map = self.read_map(filename)
        self.x = x
        self.y = y


    def print_map(self):
        # for line in map:
        #     print ''.join(line)
        pass

    def read_map(self, filename):
        my_map = []

        with open(filename) as f:
            for line in f:
                row = []
                for char in line:
                    if char != '\n':
                        row.append(char)
                my_map.append(row)
        return my_map


    def flood_fill(self, map, x, y, original_char, fill_char):

        if map[y][x] != original_char:
            return

        map[y][x] = fill_char
        if x - 1 >= 0:
            self.flood_fill(map, x - 1, y, original_char, fill_char)
        if x + 1 < len(map[y]):
            self.flood_fill(map, x + 1, y, original_char, fill_char)
        if y - 1 >= 0:
            self.flood_fill(map, x, y - 1, original_char, fill_char)
        if y + 1 < len(map):
            self.flood_fill(map, x, y + 1, original_char, fill_char)


first_map = Map("map.txt", 2, 2)
first_map.print_map()



#
#
#
# def get_map():
#     my_map = []
#
#     with open('map.txt') as f:
#         for line in f:
#             row = []
#             for char in line:
#                 if char != '\n':
#                     row.append(char)
#             my_map.append(row)
#     return my_map
#
#
# def get_user_input(debug_mode):
#     if debug_mode:
#         return 3, 5, 'S'
#
#     x = int(raw_input("Enter an x coordinate: "))
#     y = int(raw_input("Enter a y coordinate: "))
#     c = raw_input("Enter a character to fill with: ")
#
#     return x, y, c
#
# def fill_map(map, x, y, fill_char, original_char):
#     if map[y][x] != original_char:
#         return
#     map[y][x] = fill_char
#     if x-1 >= 0:
#         fill_map(map, x - 1, y, fill_char, original_char)
#     if x + 1 < len(map[y]):
#         fill_map(map, x + 1, y, fill_char, original_char)
#     if y - 1 >= 0:
#         fill_map(map, x, y - 1, fill_char, original_char)
#     if y + 1 < len(map):
#         fill_map(map, x, y + 1, fill_char, original_char)
#
#
# def print_map(map):
#     for line in map:
#         print ''.join(line)
#
#
# def main():
#     from sys import argv
#     debug_mode = False
#     if len(argv) > 1:
#         debug_mode = argv[1]
#
#     map = get_map()
#     x, y, c = get_user_input(debug_mode)
#     fill_map(map, x, y, c, map[y][x])
#     print_map(map)
#
# main()
# map1 = Map('map.txt', (3,4))
# print map1.coords[1]