import aStarNums
import dijktra
import random
import csv


def BruteTest():
    d = [5, 10, 15, 20, 25, 30, 40, 50]
    v = [5, 10, 20, 50, 100, 500, 1000]
    with open('Results.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Grid', 'Range', 'Avg_Accuracy', 'Lowest Accuracy', 'Avg_Faster'])
        for i in d:
            for j in d:
                for r in v:
                    sval = aval = 0
                    amin = 100
                    for _ in range(10):
                        grid = makeGrid(1, r, i, j)
                        grid[j-1][i-1] = 'X'
                        Atime, Acost = aStarNums.aStar(grid, (0, 0), (j-1, i-1))
                        Dtime, Dcost = dijktra.dijkstra(grid, (0, 0), (j-1, i-1))
                        accuracy = getAccuracy(Acost, Dcost)
                        speed = getSpeed(Atime, Dtime)
                        sval += speed
                        aval += accuracy
                        if accuracy < amin:
                            amin = accuracy
                        # print(i,'x', j, ' grid: 1 - ', r, 'Range: Faster by: ', speed, '% : ', accuracy, '% accuracy')
                    filewriter.writerow([str(i) + 'x' + str(j), '1 - ' + str(r), str(round(aval/10, 3)) + '%', str(amin)
                                         + '%', str(round(sval/10, 3)) + '%'])
    csvfile.close()


def getSpeed(t1, t2):
    return round(t2 / t1 * 100, 3)


def getAccuracy(a1, a2):
    return round(a2 / a1 * 100, 3)


def makeGrid(range1, range2, gridx, gridy):
    grid = [[[0] for _ in range(gridx)] for _ in range(gridy)]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            num = random.randint(range1, range2)
            grid[i][j] = num
    return grid


def Brute20Test():
    d = [15, 20, 25]
    v = [5, 10, 20, 50, 100, 500, 1000]
    with open('Results20.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Grid', 'Range', 'Avg_Accuracy', 'Lowest Accuracy', 'Avg_Faster'])
        for i in d:
            for j in d:
                for r in v:
                    sval = aval = 0
                    amin = 100
                    for _ in range(10):
                        grid = makeGrid(1, r, i, j)
                        grid[j - 1][i - 1] = 'X'
                        Atime, Acost = aStarNums.aStar(grid, (0, 0), (j - 1, i - 1))
                        Dtime, Dcost = dijktra.dijkstra(grid, (0, 0), (j - 1, i - 1))
                        accuracy = getAccuracy(Acost, Dcost)
                        speed = getSpeed(Atime, Dtime)
                        sval += speed
                        aval += accuracy
                        if accuracy < amin:
                            amin = accuracy
                        # print(i,'x', j, ' grid: 1 - ', r, 'Range: Faster by: ', speed, '% : ', accuracy, '% accuracy')
                    filewriter.writerow(
                        [str(i) + 'x' + str(j), '1 - ' + str(r), str(round(aval / 10, 3)) + '%', str(amin)
                         + '%', str(round(sval / 10, 3)) + '%'])
    csvfile.close()

# BruteTest()
Brute20Test()
