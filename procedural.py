# Pixel Art - http://www.101computing.net/pixel-art-in-python/

import turtle
import random
import rooms

myPen = turtle.Turtle()
# myPen.tracer(0)
myPen.speed(0)
myPen.color("#000000")

setX = 16
setY = 16

grid = [[]]
for columns in range(0, setX):
    grid[0].append(0)

for rows in range(0, setY):
    row = []
    for columns in range(0, setX):
        row.append(0)
    grid.append(row)

# entrance_dir = random.randint(0, 4)
entrance_dir = 0
# 0 = North, 1 = East, 2 = South, 3 = West


def setEntrance(entrance_dir = entrance_dir, grid = grid):
    if entrance_dir == 0:
        entrance_side0 = [0, (setX // 2) - 1]
        entrance_side1 = [0, (setX // 2)]
        entrance_side2 = [0, (setX // 2) + 1]
        grid[0][setX // 2] = 1
        grid[0][(setX // 2) - 1] = 1
        grid[0][(setX // 2) + 1] = 1
        return [entrance_side0, entrance_side1, entrance_side2]
    elif entrance_dir == 1:
        entrance_side0 = [(setY // 2) - 1, -1]
        entrance_side1 = [(setY // 2), -1]
        entrance_side2 = [(setY // 2) + 1, -1]
        grid[setY // 2][-1] = 1
        grid[(setY // 2) - 1][-1] = 1
        grid[(setY // 2) + 1][-1] = 1
        return [entrance_side0, entrance_side1, entrance_side2]
    elif entrance_dir == 2:
        entrance_side0 = [-1, (setX // 2) - 1]
        entrance_side1 = [-1, (setX // 2)]
        entrance_side2 = [-1, (setX // 2) + 1]
        grid[-1][setX // 2] = 1
        grid[-1][(setX // 2) - 1] = 1
        grid[-1][(setX // 2) + 1] = 1
        return [entrance_side0, entrance_side1, entrance_side2]
    else:
        entrance_side0 = [(setY // 2) - 1, 0]
        entrance_side1 = [(setY // 2), 0]
        entrance_side2 = [(setY // 2) + 1, 0]
        grid[setY // 2][0] = 1
        grid[(setY // 2) - 1][0] = 1
        grid[(setY // 2) + 1][0] = 1
        return [entrance_side0, entrance_side1, entrance_side2]


entrance_bounds = setEntrance()
print(entrance_bounds)


# def addHallway(entrance_dir = entrance_dir, anchor = entrance_bounds):
#     anchor1y = anchor[0][0]
#     anchor1x = anchor[0][1]
#     anchor2y = anchor[2][0]
#     anchor2x = anchor[2][1]
#     print(anchor1x, anchor1y)
#     print(anchor2x, anchor2y)
#     hallway_length = 7
#     for squares in range(hallway_length):
#         grid[anchor1y + squares][anchor1x] = 1
#         grid[anchor2y + squares][anchor2x] = 1


grid = rooms.addHallway(entrance_dir, entrance_bounds, grid)



# This function draws a box by drawing each side of the square and using the fill function
def emptyGrid(intDim):
    # myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    # myPen.end_fill()
    myPen.setheading(0)


def fillGrid(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

boxSize = 10
# Position myPen in top left area of the screen
myPen.penup()
# Below var was originally -100 I think.
myPen.forward(-(len(grid)*3.5))
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if grid[i][j] == 0:
            emptyGrid(boxSize)
            # print("Printing grid row {0}".format(i))
        else:
            fillGrid(boxSize)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.pendown()
    myPen.setheading(270)
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180)
    myPen.forward(boxSize * len(grid[i]))
    myPen.setheading(0)
    myPen.pendown()

myPen.getscreen().update()
turtle.done()