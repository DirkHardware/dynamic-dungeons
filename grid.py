import turtle
import random
import structures


class Grid(object):

    """
    Fuck it. From now on Grid is going to handle building itself to maintain
    single source of truth. Structure objects merely return layouts and the build
    method for grid will be used to determine its own anchor points.
    """

    def __init__(self, width, height):
        self.__setX = width
        self.__setY = height
        # We don't need entrance dirs because we can just use entrance
        # dirs to set our first anchor instead.
        self.current_structure = structures.TeeHall(0)
        self.valid_structures = []
        # The below values are just for test purposes, remember to set
        # them back to a blank list when you are done.
        self.anchor = [0, 7]
        self.squares = [[]]
        for columns in range(0, self.__setX):
            self.squares[0].append(0)

        for rows in range(0, self.__setY):
            row = []
            for columns in range(0, self.__setX):
                row.append(0)
            self.squares.append(row)

    # Do we actually need this method?
    def offset(self):
        offset = 0
        offset_found = False
        while not offset_found:
            for column in self.current_structure.layout[0]:
                if column == structures.x:
                    offset -= 1
                    # print(offset)
                else:
                    offset_found = True
                    # print(offset)
        self.anchor[1] += offset
        # print(self.anchor)
        # print(offset)
        return self.anchor

    def build(self):
        # print(self.current_structure)
        # THIS SHOULD BE USED FOR NORTH TO SOUTH STRUCTURES ONLY
        # self.anchor = self.offset()
        current_y = self.anchor[0]
        current_x = self.anchor[1]
        while current_y < len(self.current_structure.layout[0]) + 1:
            for square in self.current_structure.layout[current_y]:
                if square is not structures.x:
                    grid.squares[current_y][current_x] = square
                    current_x += 1
                else:
                    current_x += 1
                    pass
            current_y += 1
            current_x = self.anchor[1]
        print(self.squares)
        # print("Current X:{0}, Current Y: {1}".format(current_x, current_y))


# Grid starts by randomly generating anchor
# Structure classes a distinct signature shape expressable as a matrix that the grid class
# can read an apply to itself. These signatures must be rotatable by compass direction.
# Does the grid need to know the direction of all of its anchor points?
# What does the grid do apart from creating and exporting itself, along with
# keeping track of anchor points.
# Is it grids job to keep track of what structures it should or shouldn't be building?

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

if __name__ == '__main__':
    grid = Grid(16, 16)
    grid.offset()
    grid.build()
    # hallway = structures.ShortHallway(0)
    # hallway.check_attributes()
    # hallway.blueprint()
    #
    # potential_classes = [Duck(), Dog(), Frog()]
    # pet = potential_classes[random.randint(0, 2)]
    # pet.speak()
    # grid = Grid(16, 16)
    # print(grid.squares)
    myPen = turtle.Turtle()
    # myPen.tracer(0)
    myPen.speed(0)
    myPen.color("#000000")

    boxSize = 10
    # Position myPen in top left area of the screen
    myPen.penup()
    # Below var was originally -100 I think.
    myPen.forward(-(len(grid.squares)*3.5))
    myPen.setheading(90)
    myPen.forward(100)
    myPen.setheading(0)

    for i in range(0, len(grid.squares)):
        for j in range(0, len(grid.squares[i])):
            if grid.squares[i][j] == 0:
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
        myPen.forward(boxSize * len(grid.squares[i]))
        myPen.setheading(0)
        myPen.pendown()

    myPen.getscreen().update()
    turtle.done()