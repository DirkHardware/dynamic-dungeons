import turtle
import random
import structures
from exceptions import SpillOverError

"""Perhaps if we want to partition Grid into sectors to make life easier,
we can make the sectors a subclass of grid, so that way they can keep track
of their own anchors and available space. """

class Grid(object):

    @staticmethod
    def _test_negative(index):
        try:
            if index < 0:
                raise SpillOverError
        except SpillOverError:
            print("SpillOverError at {}".format(index))


    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        # We don't need entrance dirs because we can just use entrance
        # dirs to set our first anchors instead.
        self.current_structure = structures.CircleRoom7x6()
        self.all_structures = [structures.ShortHallway(), structures.TeeHall()]
        self.valid_structures = [structures.ShortHallway(), structures.TeeHall()]
        # The below values are just for test purposes, remember to set
        # them back to a blank list when you are done.
        self.anchors = [[2, 11, "N"]]
        # self.anchors = [[4, 7, "S"]]
        self.squares = [[]]
        for columns in range(0, self.__width):
            self.squares[0].append(0)

        for rows in range(0, self.__height):
            row = []
            for columns in range(0, self.__width):
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
                    print("Offset: {}".format(offset))
                    break
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
        self.anchors = self.offset()
        anchor_direction = self.anchors[0][2]
        if anchor_direction == "S":
            layout = self.current_structure.layout
            layout_y = 0
            current_y = self.anchors[0][0]
            current_x = self.anchors[0][1]
            while layout_y < len(layout):
                for square in layout[layout_y]:
                    if square == 1:
                        self._test_negative(current_x)
                        self.squares[current_y][current_x] = square
                        print("Current_x: {}".format(curre nt_x))
                        print("Current_y: {}".format(current_y))
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
                for square in layout[layout_y]:
                    if square == 1:
                        self._test_negative(current_x)
                        self.squares[current_y][current_x] = square
                        print("Current_x: {}".format(current_x))
                        print("Current_y: {}".format(current_y))
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
                        # print(square)
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

    """
    Plan 1: Unrestrained Building 
        -Entrance anchor is determined
        -Valid structures is a dictionary of keys representing different categories of rooms matched to arrays of 
        structures
        -Algorithim selects a structure from an appropriate category (hallways? junctions?)
        -A method checks to see if the structure spills out of the index. If yes: Pick a different structure, if not, 
        add the structure.
        Anchor[0], which is always the anchor we are building off of, will be deleted.
        ***This will have the effect of making the map build out as much as it can from one T-square anchor before 
        the other gets any room to do anything. Maybe this is a bad idea.***
        ***Maybe we could get around this by doing away with Anchor[0] as being the only anchor we're building off of,
        and iterate through our anchors, building structures***
        
    Plan 2: Cluster Building
        -Entrance anchor is determined
        -Valid structures is a dictionary of keys representing different categories of rooms matched to arrays of 
        structures
        -Algorithim picks an anchor point selects a structure from an appropriate category (hallways? junctions?)
        -Algorithim deletes starting anchor. Instead of unrestrained building, each anchor after the first will cause
        the algorithim to randomly generate out a collection (cluster) of structures that go together, based on what 
        category they are in and how many anchors they have (I will have to add that an attribute to structures).
        -The Algorithim checks to see if this cluster will spill out of index or onto another structure. It then checks
         the collective area of the structures. 
        -If it would cause an error, reroll. The number of other available 
         anchors will determine how numerous and large the cluster structure can be, and if it can have any open 
         anchor points.      
        -Repeat process for the next open anchor point, using a system that keeps track of available, building space to
        determine cluster size. Maybe it's not a bad idea to break up the map into sectors based on the initial 
        entrance structure. 
    """
    # def blueprint(self):
    #     for anchor in self.anchors:
    #     pass



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
