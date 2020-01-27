# Pathfinder
NOTE: This is a personal project for learning more about pathfinding and optimization and not a complete application - there will definetely be bugs. Although watching the pathfinding algorithm simulation is interesting, there are visual improvements that can be made to the rest of the GUI


A GUI created to for visualizing pathfinding algorithms with both weighted/unweighted nodes. Written in Python3 with tkinter.


CONTENTS:

grid.py - The root of the program, used to build grids and access pathfinding algorithms

bfs.py - Simple breadth first search algorithm (does not move diagonally - this was mostly a test function for the grid)

aStar.py - A* pathfinding algorithm, particularly useful when dealing with walls

dijkstra.py - brute force search for shortest path from start to end node using dijksta's algorithm

aStarNums.py - A* algorithm, but used for dealing with weighted nodes/paths. By adjusting the function declares value of a node based on its distance to the end node, can be very accurate and more effecient that dijkstras.

HOW TO RUN:

1. run grid.py to start the program

2. Choose your board dimensions

3. Choose to draw a board that has weighted nodes (Board with Values) or not (Make Board)

4. Choose your start and end points by clicking on grid (blue = start, red = end)

5. You can place walls that will block certain nodes by selecting the "Walls" button

6. Choose a pathfinding algorithm to run:
  i. for unweighted nodes: BFS or A*
  ii. for weighted nodes: Dijkstra or A*Nums
