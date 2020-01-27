import time
from tkinter import *
import random
import bfs
import aStar
import aStarNums
import dijktra

window = Tk()
window.title('PathFinder')
boardFrame = Frame(window)
doubleFrame = Frame(window)


def createBoard(m, n):
    global running
    global startBox
    global endBox
    global seFlag
    global board
    global startX
    global startY
    global endX
    global endY
    global walls
    global numFlag
    numFlag = 0
    running = False
    startBox = endBox = startX = startY = endX = endY = None
    seFlag = 0
    walls = []
    # clear board filling
    for widget in boardFrame.winfo_children():
        widget.destroy()
    board = [[Label(boardFrame) for _ in range(m)] for _ in range(n)]
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            board[i][j] = Label(boardFrame, width=2, height=1, relief='groove')
            board[i][j].grid(row=i + 5, column=j, sticky=NSEW)
            board[i][j].bind("<Button-1>", lambda _, x=i, y=j: select(board, x, y))
    boardFrame.pack(side=BOTTOM)


def createWithValues(n, m):
    global running
    global startBox
    global endBox
    global seFlag
    global numFlag
    global board
    global startX
    global startY
    global endX
    global endY
    global walls
    running = False
    startBox = endBox = startX = startY = endX = endY = None
    seFlag = 0
    walls = []
    numFlag = 1
    # clear board filling
    for widget in boardFrame.winfo_children():
        widget.destroy()
    board = [[Label(boardFrame) for _ in range(m)] for _ in range(n)]
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            num = random.randint(1, 50)
            board[i][j] = Label(boardFrame, width=2, height=1, text=str(num), relief='groove')
            board[i][j].grid(row=i, column=j, sticky=NSEW)
            board[i][j].bind("<Button-1>", lambda _, x=i, y=j: select(board, x, y))
    boardFrame.pack(side=BOTTOM)


def select(b, x, y):
    global running
    global startBox
    global startX
    global startY
    global endBox
    global endX
    global endY
    global seFlag
    global wallFlag
    global walls
    if running:
        return
    if wallFlag:
        if [x, y] not in walls and b[x][y] is not startBox and b[x][y] is not endBox:
            walls.append([x, y])
            b[x][y].config(bg='grey')
        else:
            walls.remove([x, y])
            b[x][y].config(bg='white')
    else:
        if startBox is None and [x, y] not in walls:
            startBox = b[x][y]
            startX = x
            startY = y
            startBox.config(bg="blue")
            seFlag = 1
        elif endBox is None and b[x][y] is not startBox and [x, y] not in walls:
            endBox = b[x][y]
            endX = x
            endY = y
            endBox.config(bg="red")
            seFlag = 0
        elif b[x][y] is not startBox and b[x][y] is not endBox and seFlag == 0 and [x, y] not in walls:
            startBox.config(bg="white")
            startBox = b[x][y]
            startX = x
            startY = y
            b[x][y].config(bg="blue")
            seFlag = 1
        elif b[x][y] is not startBox and b[x][y] is not endBox and seFlag == 1 and [x, y] not in walls:
            endBox.config(bg="white")
            endBox = b[x][y]
            endX = x
            endY = y
            b[x][y].config(bg="red")
            seFlag = 0


def bfSearch():
    global endX
    global endY
    grid, x, y = buildGrid()
    path, seen = bfs.bfs(grid, (x, y))
    path.remove(path[0])
    path.remove(path[-1])
    seen.remove(seen[0])
    seen.remove((endX, endY))
    colourBoard(seen, path)


def aStarSearch():
    global endX
    global endY
    grid, x, y = buildGrid()
    seen, path = aStar.aStar(grid, (x, y), (endX, endY))
    path.remove(path[-1])
    seen.remove(seen[0])
    colourBoard(seen, path)


def aStarNumsSearch():
    global endX
    global endY
    grid, x, y = buildGrid()
    seen, path = aStarNums.aStar(grid, (x, y), (endX, endY))
    path.remove(path[-1])
    seen.remove(seen[0])
    colourBoard(seen, path)

def dijkstraSearch():
    global endX
    global endY
    grid, x, y = buildGrid()
    seen, path = dijktra.dijkstra(grid, (x, y), (endX, endY))
    path.remove(path[-1])
    seen.remove(seen[0])
    seen.remove([endX, endY])
    colourBoard(seen, path)

def buildGrid():
    global board
    global startX
    global startY
    global endX
    global endY
    global walls
    global numFlag

    grid = [[0] * len(board[0]) for _ in range(len(board))]
    if numFlag:
        for i in range(len(board)):
            for j in range(len(board[0])):
                grid[i][j] = (int(board[i][j].cget('text')))
    if startX is not None and startY is not None:
        grid[startX][startY] = 'S'
    if endX is not None and endY is not None:
        grid[endX][endY] = 'X'
    for w, z in walls:
        grid[w][z] = 'W'
    if startX is not None and startY is not None and endX is not None and endY is not None:
        return grid, startX, startY


def colourBoard(seen, path):
    global running
    running = True
    for s1, s2 in seen:
        boardFrame.update()
        time.sleep(.05)
        board[s1][s2].config(bg="orange")
    for p1, p2 in path:
        boardFrame.update()
        time.sleep(.100)
        board[p1][p2].config(bg="green")
    running = False


def SetWalls():
    global wallFlag
    if wallFlag:
        wallFlag = False
    else:
        wallFlag = True


seFlag = wallFlag = running = numFlag = 0
startBox = startX = startY = endBox = endX = endY = board = None
walls = []
inputFrame = Frame(window)
l1 = Label(inputFrame, text='Choose Board Dimensions').grid(row=0, column=0)
e1 = Entry(inputFrame, width=5)
e2 = Entry(inputFrame, width=5)
e1.insert(0, 2)
e2.insert(0, 2)
el1 = Label(inputFrame, text='x', width=1)
e1.grid(row=0, column=1)
el1.grid(row=0, column=2)
e2.grid(row=0, column=3)
b1 = Button(inputFrame, text="Make Board", command=lambda: createBoard(int(e1.get()), int(e2.get()))) \
    .grid(row=0, column=4)
b2 = Button(inputFrame, text="Walls", command=lambda: SetWalls()).grid(row=1, column=5)
b3 = Button(inputFrame, text="BFS", command=lambda: bfSearch()).grid(row=1, column=1)
b4 = Button(inputFrame, text="A*", command=lambda: aStarSearch()).grid(row=1, column=2)
b5 = Button(inputFrame, text="A*Nums", command=lambda: aStarNumsSearch()).grid(row=1, column=3)
b6 = Button(inputFrame, text="Dijkstra", command=lambda: dijkstraSearch()).grid(row=1, column=4)
b7 = Button(inputFrame, text="Board with Values", command=lambda: createWithValues(int(e1.get()), int(e2.get()))) \
    .grid(row=0, column=6)
inputFrame.pack(side=TOP)

window.mainloop()
