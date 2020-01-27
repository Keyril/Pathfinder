import sys


def aStar(grid, start, end):
    finish, wall = 'X', 'W'
    width, height = len(grid), len(grid[0])
    s1, s2 = start
    h = (end[0] - s1) ** 2 + (end[1] - s2) ** 2  # getting the first value
    open_list = [[s1, s2, h, 0, h, None]]  # assigning start to open list, f = h, g=0
    seen = []
    seen_coords = []
    while open_list:
        candidate = sys.maxsize
        node = None
        for i in range(len(open_list)):
            if open_list[i][2] < candidate:
                candidate = open_list[i][2]
                node = open_list[i]
        if (node[0], node[1]) == end:
            path = []
            while node[5] is not None and node[5] != -1:
                path.append([node[0], node[1]])
                node = seen[node[5]]
            path.reverse()
            return seen_coords, path
        seen.append(node)
        seen_coords.append([node[0], node[1]])
        open_list.remove(node)
        x, y = node[0], node[1]
        for x1, y1 in (x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1), (
                x, y + 1), (x, y - 1):
            if 0 <= x1 < width and 0 <= y1 < height and grid[x1][y1] != wall and [x1, y1] not in seen_coords:
                n1 = findInList(open_list, x1, y1)
                f, g, h = FGH(start, (x1, y1), end)
                current_index = getSeenIndex(seen, x, y)
                if n1:
                    i = open_list.index(n1)
                    if g < open_list[i][3]:
                        open_list[i] = [x1, y1, f, g, h, current_index]
                else:
                    open_list.append([x1, y1, f, g, h, current_index])


def FGH(start, node, end):
    x, y = node
    g = (start[0] - x) ** 2 + (start[1] - y) ** 2
    h = (end[0] - x) ** 2 + (end[1] - y) ** 2
    f = g + h
    return [f, g, h]


def findInList(open_list, x, y):
    for i in range(len(open_list)):
        if open_list[i][0] == x and open_list[i][1] == y:
            return open_list[i]
    return 0


def getSeenIndex(seen, x, y):
    for i in range(len(seen)):
        if seen[i][0] == x and seen[i][1] == y:
            return i
    return -1
