import turtle
import random
import structures


class Grid(object):

    """
    Fuck it. From now on Grid is going to handle building itself to maintain
    single source of truth. Structure objects merely return layouts and the build
    method for grid will be used to determine its own anchors points.
    """

    def __init__(self, width, height):
        self.__setX = width
        self.__setY = height
        # We don't need entrance dirs because we can just use entrance
        # dirs to set our first anchors instead.
        self.current_structure = structures.TeeHall(0)
        self.all_structures = [structures.ShortHallway(0), structures.TeeHall(0)]
        self.valid_structures = [structures.ShortHallway(0), structures.TeeHall(0)]
        # The below values are just for test purposes, remember to set
        # them back to a blank list when you are done.
        self.anchors = [[5, 7, "N"]]
        # self.anchors = [[4, 7, "S"]]
        self.squares = [[]]
        for columns in range(0, self.__setX):
            self.squares[0].append(0)

        for rows in range(0, self.__setY):
            row = []
            for columns in range(0, self.__setX):
                row.append(0)
            self.squares.append(row)

    # Do we actually need this method?
    # OH YEAH. WE TOTALLY NEED THIS METHOD
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
        self.anchors[0][1] += offset
        # print(self.anchors)
        # print(offset)
        return self.anchors

    def create_anchor(self, y, x, square, anchor_direction):
        # South facing is the default structure direction, so there is no need
        # to change anchor facing
        if anchor_direction == "S":
            if square == "S":
                self.anchors.append([y, x, square])
            elif square == "N":
                self.anchors.append([y, x, square])
            elif square == "E":
                self.anchors.append([y, x, square])
            elif square == "W":
                self.anchors.append([y, x, square])
        if anchor_direction == "N":
            if square == "S":
                self.anchors.append([y, x, "N"])
            elif square == "N":
                self.anchors.append([y, x, "S"])
            elif square == "E":
                self.anchors.append([y, x, square])
            elif square == "W":
                self.anchors.append([y, x, square])
        if anchor_direction == "E":
            if square == "S":
                self.anchors.append([y, x, "E"])
            elif square == "N":
                self.anchors.append([y, x, "W"])
            elif square == "E":
                self.anchors.append([y, x, "N"])
            elif square == "W":
                self.anchors.append([y, x, "S"])
        if anchor_direction == "W":
            if square == "S":
                self.anchors.append([y, x, "W"])
            elif square == "N":
                self.anchors.append([y, x, "E"])
            elif square == "E":
                self.anchors.append([y, x, "S"])
            elif square == "W":
                self.anchors.append([y, x, "N"])

    def build(self):
        # self.anchors = self.offset()
        anchor_direction = self.anchors[0][2]
        if anchor_direction == "S":
            layout = self.current_structure.layout
            layout_y = 0
            current_y = self.anchors[0][0]
            current_x = self.anchors[0][1]
            while layout_y < len(layout[0]) + 1:
                for square in layout[layout_y]:
                    if square == 1:
                        self.squares[current_y][current_x] = square
                        current_x += 1
                    elif isinstance(square, str):
                        self.create_anchor(current_y, current_x, square, anchor_direction)
                        grid.squares[current_y][current_x] = square
                        current_x += 1
                    else:
                        current_x += 1
                layout_y += 1
                current_y += 1
                current_x = self.anchors[0][1]
        # Rooms anchored north to south flip now.
        elif anchor_direction == "N":
            layout = self.current_structure.layout
            layout_y = len(layout) - 1
            current_y = self.anchors[0][0]
            current_x = self.anchors[0][1]
            while layout_y > -1:
                for square in self.current_structure.layout[layout_y]:
                    if square == 1:
                        self.squares[current_y][current_x] = square
                        current_x += 1
                    elif isinstance(square, str):
                        self.create_anchor(current_y, current_x, square, anchor_direction)
                        grid.squares[current_y][current_x] = square
                        current_x += 1
                    else:
                        current_x += 1
                layout_y -= 1
                current_y += 1
                current_x = self.anchors[0][1]
        elif anchor_direction == "W":
            layout = self.current_structure.layout
            layout_y = 0
            current_y = self.anchors[0][0]
            current_x = self.anchors[0][1]
            while layout_y < len(layout[0]) + 1:
                for square in layout[layout_y]:
                    if square == 1:
                        self.squares[current_y][current_x] = square
                        current_y += 1
                    elif isinstance(square, str):
                        print(square)
                        self.create_anchor(current_y, current_x, square, anchor_direction)
                        grid.squares[current_y][current_x] = square
                        current_y += 1
                    else:
                        current_y += 1
                layout_y += 1
                current_x += 1
                current_y = self.anchors[0][1]
        elif anchor_direction == "E":
            layout = self.current_structure.layout
            layout_y = 0
            current_y = self.anchors[0][0]
            current_x = self.anchors[0][1]
            while layout_y < len(layout[0]) + 1:
                for square in reversed(layout[layout_y]):
                    if square == 1:
                        self.squares[current_y][current_x] = square
                        current_y += 1
                    elif isinstance(square, str):
                        print(square)
                        self.create_anchor(current_y, current_x, square, anchor_direction)
                        grid.squares[current_y][current_x] = square
                        current_y += 1
                    else:
                        current_y += 1
                layout_y += 1
                current_x += 1
                current_y = self.anchors[0][1]
        print(self.squares)
        print(self.anchors)
        # print("Current X:{0}, Current Y: {1}".format(current_x, current_y))


def __str__():
    print("80 is south facing, 81 is west facing, 82 is north facing, 83 is east facing")


# Grid starts by randomly generating anchors
# Structure classes a distinct signature shape expressable as a matrix that the grid class
# can read an apply to itself. These signatures must be rotatable by compass direction.
# Does the grid need to know the direction of all of its anchors points?
# What does the grid do apart from creating and exporting itself, along with
# keeping track of anchors points.
# Is it grids job to keep track of what structures it should or shouldn't be building?

def emptyGrid(intDim):
    myPen.begin_fill()
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
    grid = Grid(40, 40)
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

    boxSize = 5
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
    for row in grid.squares:
        print(row, '\n')
