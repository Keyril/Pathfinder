import sys
import timeit

def dijkstra(grid, start, end):
    finish, wall = 'X', 'W'
    width, height = len(grid), len(grid[0])
    s1, s2 = start
    open_list = [[s1, s2, 0, None]]  # gridx, gridy, total val, distance to end(guessed), distance to start
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
        seen.append(node)
        seen_coords.append([node[0], node[1]])
        open_list.remove(node)
        x, y = node[0], node[1]
        for x1, y1 in (x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1), (
                x, y + 1), (x, y - 1):
            if 0 <= x1 < width and 0 <= y1 < height and grid[x1][y1] != wall and [x1, y1] not in seen_coords:
                n1 = findInList(open_list, x1, y1)
                ds = 0
                if grid[x1][y1] not in ['X', 'W', 'S']:
                    ds = int(grid[x1][y1]) + node[2]
                current_index = getSeenIndex(seen, x, y)
                if n1:
                    i = open_list.index(n1)
                    if ds < open_list[i][2]:
                        open_list[i] = [x1, y1, ds, current_index]
                else:
                    open_list.append([x1, y1, ds, current_index])
    node = findInList(seen, end[0], end[1])
    if node:
        stopTime = timeit.default_timer()
        path = []
        cost = seen[node[3]][2]
        # print('Dijkstra cost: ', seen[node[3]][2])
        # print('Dijkstra time: ', stopTime - startTime)
        while node[3] is not None and node[3] != -1:
            path.append([node[0], node[1]])
            node = seen[node[3]]
        path.reverse()
        return (stopTime - startTime), cost
        # return seen_coords, path



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
