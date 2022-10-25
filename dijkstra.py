import random as rand
next = []
def genGrid():

    def gridSearch():

        def addNexts(current, distance):
            if (current[1] + 1 < len(grid[current[0]])):
                next.append([[current[0], current[1] + 1], current, distance + 1])
            if (current[0] + 1 < len(grid)):
                next.append([[current[0] + 1, current[1]], current, distance + 1])
            if (current[1] - 1 >= 0):
                next.append([[current[0], current[1] - 1], current, distance + 1])
            if (current[0] - 1 >= 0):
                next.append([[current[0] - 1, current[1]], current, distance + 1])

        def tracePath(last):
            if (grid[last[0]][last[1]][0] != 0):
                nextTrace = grid[last[0]][last[1]][1]
                grid[last[0]][last[1]] = "+"
                tracePath(nextTrace)
                return
            else:
                grid[last[0]][last[1]] = "O"
                return

        if (len(next) > 0):
            last = next[0][1]
            current = next[0][0]
            distance = next[0][2]
            next.pop(0)
            #print(f"next={next}")
            #print("gridSearch current = " + str(current))
            if (grid[current[0]][current[1]] == 1):
                grid[current[0]][current[1]] = "X"
                tracePath(last)
                #print(f"Found the goal! : {last}")
            elif (grid[current[0]][current[1]] != -1):
                gridSearch()
            else:
                grid[current[0]][current[1]] = [distance, last]
                #print(f"grid[{current[0]}][{current[1]}] = [{distance}, {last}]")
                addNexts(current, distance)
                gridSearch()
        else:
            print("No path!")
            return

    def fixForDisplay():
        for row in range(length):
            for col in range(width):
                if ((type(grid[row][col]) is list and grid[row][col][0] != 0) and grid[row][col] != "X" or grid[row][col] == -1):
                    grid[row][col] = " "
                elif (type(grid[row][col]) is list and grid[row][col][0] == 0):
                    grid[row][col] = "O"
                elif (grid[row][col] == -2):
                    grid[row][col] = "B"
    def genObstacles(width, length):
        numOfObstacles = (width * length) // 4
        for i in range(numOfObstacles):
            randX = rand.randint(0,width-1)
            randY = rand.randint(0, length-1)
            grid[randY][randX] = -2

    width = rand.randint(5,20)
    length = rand.randint(5,20)
    print("width: ", width, "  length: ", length)
    source = [rand.randint(0,length-1), rand.randint(0,width-1)]
    goal = [rand.randint(0,length-1), rand.randint(0,width-1)]
    grid = [[-1 for col in range(width)] for row in range(length)]
    genObstacles(width, length)
    grid[goal[0]][goal[1]] = 1
    grid[source[0]][source[1]] = -1
    next.append([source, source, 0])
    gridSearch()
    fixForDisplay()
    for i in range(len(grid)):
        print(grid[i])

genGrid()