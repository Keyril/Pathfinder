import sys
import math
import timeit

def aStar(grid, start, end):
    finish, wall = 'X', 'W'
    width, height = len(grid), len(grid[0])
    s1, s2 = start
    d = math.sqrt((end[0] - s1) ** 2 + (end[1] - s2) ** 2)
    open_list = [[s1, s2, d, d, 0, None]]  # gridx, gridy, total val, distance to end(guessed), distance to start
    seen = []
    seen_coords = []
    startTime = timeit.default_timer()
    while open_list:
        candidate = sys.maxsize
        node = None
        for i in range(len(open_list)):
            if open_list[i][2] < candidate:
                candidate = open_list[i][2]
                node = open_list[i]
        if (node[0], node[1]) == end:
            stopTime = timeit.default_timer()
            path = []
            cost = seen[node[5]][4]
            # print('A* cost: ', seen[node[5]][4])
            # print('A* time: ', stopTime - startTime)
            while node[5] is not None and node[5] != -1:
                path.append([node[0], node[1]])
                node = seen[node[5]]
            path.reverse()
            return (stopTime-startTime), cost
            # return seen_coords, path
        seen.append(node)
        seen_coords.append([node[0], node[1]])
        open_list.remove(node)
        x, y = node[0], node[1]
        for x1, y1 in (x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1), (
                x, y + 1), (x, y - 1):
            if 0 <= x1 < width and 0 <= y1 < height and grid[x1][y1] != wall and [x1, y1] not in seen_coords:
                n1 = findInList(open_list, x1, y1)
                d = getDistance((x1, y1), end)
                ds = 0
                if grid[x1][y1] not in ['X', 'W', 'S']:
                    ds = int(grid[x1][y1]) + node[4]
                current_index = getSeenIndex(seen, x, y)
                if n1:
                    i = open_list.index(n1)
                    if ds < open_list[i][4]:
                        open_list[i] = [x1, y1, d + ds, d, ds, current_index]
                else:
                    open_list.append([x1, y1, d + ds, d, ds, current_index])


def getDistance(node, end):
    x, y = node
    temp1, temp2 = 0, 50
    tempw = temph = 10
    xend, yend = end[0] * tempw, end[1] * temph
    rangeval = (temp1 + temp2) / 2
    xdist = x / tempw * rangeval * tempw
    ydist = y / temph * rangeval * temph
    # return ((xend - xdist) ** 2) + ((yend - ydist) ** 2)
    return math.sqrt((end[0] - x) ** 2 + (end[1] - y) ** 2) * 5
    # returning a valuable distance value to the end node is the most important part of the algorithm's effeciency
    # where a low value will be very ineffecient, and a high value will result in fast runtime but poor pathfinding
    # sqrt * 7 is generally a good value for 10x10-20x20 grids. An optimized function is being worked on now.


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
