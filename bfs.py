import collections


def bfs(grid, start):
    finish, wall = 'X', 'W'
    width, height = len(grid), len(grid[0])
    queue = collections.deque([[start]])
    seen = [start]
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[x][y] == finish:
            return path, seen
        for x1, y1 in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if 0 <= x1 < width and 0 <= y1 < height and grid[x1][y1] != wall and (x1, y1) not in seen:
                queue.append(path + [(x1, y1)])
                seen.append((x1, y1))
