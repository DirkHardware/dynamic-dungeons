import turtle
import random
import structures
from exceptions import SpillOverError

"""Perhaps if we want to partition Grid into sectors to make life easier,
we can make the sectors a subclass of grid, so that way they can keep track
of their own anchors and available space. """



class Grid(object):

    @staticmethod
    def _test_anchor(y, x, direction):
        print("Created a {0} anchor @ Y:{1} X:{2}".format(direction, y, x,))

    @staticmethod
    def _print_square(current_y, current_x):
        print("Drew square @ Y: {0}, X: {1}".format(str(current_y), str(current_x)))

    @staticmethod
    def _test_negative(index):
        try:
            if index < 0:
                raise SpillOverError
        except SpillOverError:
            print("SpillOverError at {}".format(index))

    def __init__(self, width, height, starting_anchor):
        self.__width = width
        self.__height = height
        # We don't need entrance dirs because we can just use entrance
        # dirs to set our first anchors instead.
        self.current_structure = structures.TeeHall()
        self.all_structures = [structures.ShortHallway(), structures.TeeHall(), structures.CircleRoom7x6()]
        self.valid_structures = [structures.ShortHallway(), structures.TeeHall()]
        # The below values are just for test purposes, remember to set
        # them back to a blank list when you are done.
        self.anchors = [starting_anchor]
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
                    break
        self.anchors[0][1] += offset
        # print(self.anchors)
        print("Offset Anchor: {}".format(self.anchors[0]))
        return self.anchors

    def offset_alternate(self, anchor):
        offset = 0
        offset_found = False
        while not offset_found:
            for column in self.current_structure.layout[0]:
                if column == structures.x:
                    offset -= 1
                    # print(offset)
                else:
                    offset_found = True
                    break
        anchor[1] += offset
        # print(self.anchors)
        print("Offset Anchor: {}".format(anchor))
        return anchor

    def create_anchor(self, y, x, square, anchor_direction):
        # South facing is the default structure direction, so there is no need
        # to change anchor facing
        # I've figured out what the problem is with rotation here. Rotation is not taking into account the the x and
        # y changes of the anchor, and so while the next structure built is facing the right way, it's doing it from
        # the old anchor position.
        if anchor_direction == "S":
            if square == "S":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
            elif square == "N":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
            elif square == "E":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
            elif square == "W":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
        # N's anchor creation merely duplicates the initial anchor, this must
        # be addressed.
        # I think I see what I did here. I merely changed the facing of the anchor
        # without taking into account where it would be placed.
        if anchor_direction == "N":
            if square == "S":
                self.anchors.append([y - self.current_structure.height, x, "N"])
                self._test_anchor(y, x, square)
            elif square == "N":
                self.anchors.append([y - self.current_structure.height, x, "S"])
                self._test_anchor(y - (self.current_structure.height + 1), x, "S")
            elif square == "E":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
            elif square == "W":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
        if anchor_direction == "E":
            if square == "S":
                self.anchors.append([y, x, "E"])
                self._test_anchor(y, x, "E")
            elif square == "N":
                self.anchors.append([y, x, "W"])
                self._test_anchor(y, x, "W")
            elif square == "E":
                self.anchors.append([y, x, "N"])
                self._test_anchor(y, x, "N")
            elif square == "W":
                self.anchors.append([y, x, "S"])
                self._test_anchor(y, x, "S")
        if anchor_direction == "W":
            if square == "S":
                self.anchors.append([y, x, "W"])
                self._test_anchor(y, x, "W")
            elif square == "N":
                self.anchors.append([y, x, "E"])
                self._test_anchor(y, x, "E")
            elif square == "E":
                self.anchors.append([y, x, "S"])
                self._test_anchor(y, x, "S")
            elif square == "W":
                self.anchors.append([y, x, "N"])
                self._test_anchor(y, x, "N")

    def create_anchor_alternate(self, y, x, square, anchor_direction, structure):
        # South facing is the default structure direction, so there is no need
        # to change anchor facing
        # I've figured out what the problem is with rotation here. Rotation is not taking into account the the x and
        # y changes of the anchor, and so while the next structure built is facing the right way, it's doing it from
        # the old anchor position.
        if anchor_direction == "S":
            if square == "S":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
            elif square == "N":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
            elif square == "E":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
            elif square == "W":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
        # N's anchor creation merely duplicates the initial anchor, this must
        # be addressed.
        # I think I see what I did here. I merely changed the facing of the anchor
        # without taking into account where it would be placed.
        if anchor_direction == "N":
            if square == "S":
                self.anchors.append([y - structure.height, x, "N"])
                self._test_anchor(y, x, square)
            elif square == "N":
                self.anchors.append([y - structure.height, x, "S"])
                self._test_anchor(y - (structure.height + 1), x, "S")
            elif square == "E":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
            elif square == "W":
                self.anchors.append([y, x, square])
                self._test_anchor(y, x, square)
        if anchor_direction == "E":
            if square == "S":
                self.anchors.append([y, x, "E"])
                self._test_anchor(y, x, "E")
            elif square == "N":
                self.anchors.append([y, x, "W"])
                self._test_anchor(y, x, "W")
            elif square == "E":
                self.anchors.append([y, x, "N"])
                self._test_anchor(y, x, "N")
            elif square == "W":
                self.anchors.append([y, x, "S"])
                self._test_anchor(y, x, "S")
        if anchor_direction == "W":
            if square == "S":
                self.anchors.append([y, x, "W"])
                self._test_anchor(y, x, "W")
            elif square == "N":
                self.anchors.append([y, x, "E"])
                self._test_anchor(y, x, "E")
            elif square == "E":
                self.anchors.append([y, x, "S"])
                self._test_anchor(y, x, "S")
            elif square == "W":
                self.anchors.append([y, x, "N"])
                self._test_anchor(y, x, "N")

    def build(self, structure):
        print("Building from original anchor: {}".format(self.anchors[0]))
        self.anchors = self.offset()
        anchor_direction = self.anchors[0][2]
        anchors = self.anchors
        if anchor_direction == "S":
            layout = structure.layout
            layout_y = 0
            current_y = self.anchors[0][0]
            current_x = self.anchors[0][1]
            while layout_y < len(layout):
                for square in layout[layout_y]:
                    if square == 1:
                        self._test_negative(current_x)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_x, current_y)
                        current_x += 1
                    elif isinstance(square, str):
                        self.create_anchor(current_y, current_x, square, anchor_direction)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_x, current_y)
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
                        self._print_square(current_x, current_y)
                        current_x += 1
                    elif isinstance(square, str):
                        self.create_anchor(current_y, current_x, square, anchor_direction)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_x, current_y)
                        current_x += 1
                    else:
                        current_x += 1
                layout_y -= 1
                current_y += 1
                current_x = self.anchors[0][1]
        elif anchor_direction == "E":
            layout = self.current_structure.layout
            layout_y = 0
            current_y = self.anchors[0][1]
            current_x = self.anchors[0][0]
            while layout_y < len(layout):
                for square in layout[layout_y]:
                    if square == 1:
                        self.squares[current_y][current_x] = square
                        self._print_square(current_x, current_y)
                        current_y += 1
                    elif isinstance(square, str):
                        # print(square)
                        self.create_anchor(current_y, current_x, square, anchor_direction)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_x, current_y)
                        current_y += 1
                    else:
                        current_y += 1
                layout_y += 1
                current_x += 1
                current_y = self.anchors[0][1]
        elif anchor_direction == "W":
            layout = self.current_structure.layout
            layout_y = 0
            current_y = self.anchors[0][1]
            current_x = self.anchors[0][0]
            while layout_y < len(layout):
                for square in reversed(layout[layout_y]):
                    if square == 1:
                        self.squares[current_y][current_x] = square
                        self._print_square(current_x, current_y)
                        current_y += 1
                    elif isinstance(square, str):
                        self.create_anchor(current_y, current_x, square, anchor_direction)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_x, current_y)
                        current_y += 1
                    else:
                        current_y += 1
                layout_y += 1
                current_x -= 1
                current_y = self.anchors[0][1]
            del self.anchors[0]
            print("Anchors are now {}".format(self.anchors))

    def build_alternate(self, structure, anchor):
        print("Building from original anchor: {}".format(anchor))
        anchor = self.offset_alternate(anchor)
        anchor_direction = anchor[2]
        layout = structure.layout
        if anchor_direction == "S":
            layout_y = 0
            current_y = anchor[0]
            current_x = anchor[1]
            while layout_y < len(layout):
                for square in layout[layout_y]:
                    if square == 1:
                        self._test_negative(current_x)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_y, current_x)
                        current_x += 1
                    elif isinstance(square, str):
                        self.create_anchor_alternate(current_y, current_x, square, anchor_direction, structure)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_y, current_x)
                        current_x += 1
                    else:
                        current_x += 1
                layout_y += 1
                current_y += 1
                current_x = anchor[1]
        # Rooms anchored north to south flip now.
        elif anchor_direction == "N":
            layout_y = len(layout) - 1
            current_y = anchor[0]
            current_x = anchor[1]
            while layout_y > -1:
                for square in layout[layout_y]:
                    if square == 1:
                        self._test_negative(current_x)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_y, current_x)
                        current_x += 1
                    elif isinstance(square, str):
                        self.create_anchor_alternate(current_y, current_x, square, anchor_direction, structure)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_y, current_x)
                        current_x += 1
                    else:
                        current_x += 1
                layout_y -= 1
                current_y += 1
                current_x = anchor[1]
        elif anchor_direction == "E":
            layout_y = 0
            current_y = anchor[1]
            current_x = anchor[0]
            while layout_y < len(layout):
                for square in layout[layout_y]:
                    if square == 1:
                        self.squares[current_y][current_x] = square
                        self._print_square(current_y, current_x)
                        current_y += 1
                    elif isinstance(square, str):
                        # print(square)
                        self.create_anchor_alternate(current_y, current_x, square, anchor_direction, structure)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_y, current_x)
                        current_y += 1
                    else:
                        current_y += 1
                layout_y += 1
                current_x += 1
                current_y = anchor[1]
        elif anchor_direction == "W":
            layout_y = 0
            current_y = anchor[1]
            current_x = anchor[0]
            while layout_y < len(layout):
                for square in reversed(layout[layout_y]):
                    if square == 1:
                        self.squares[current_y][current_x] = square
                        self._print_square(current_y, current_x)
                        current_y += 1
                    elif isinstance(square, str):
                        self.create_anchor_alternate(current_y, current_x, square, anchor_direction, structure)
                        self.squares[current_y][current_x] = square
                        self._print_square(current_y, current_x)
                        current_y += 1
                    else:
                        current_y += 1
                layout_y += 1
                current_x -= 1
                current_y = anchor[1]
            del self.anchors[0]
            print("Anchors are now {}".format(self.anchors))

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

    def single_build_test(self):
        self.current_structure = self.all_structures[1]
        grid.build()
        del grid.anchors[0]
        # hallway = structures.ShortHallway(0)
        # hallway.check_attributes()

    def multiple_build_test(self):
        for structure in self.all_structures:
            print("Building {}".format(structure))
            grid.build(structure)
            del grid.anchors[0]


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
    grid = Grid(20, 20, [8, 8, "S"])
    # grid.single_build_test()
    grid.build_alternate(grid.all_structures[0], grid.anchors[0])
    print(grid.anchors)
    grid.build_alternate(grid.all_structures[1], grid.anchors[1])
    # grid.build(grid.all_structures[1])
    # print(grid.anchors)

    # hallway = structures.ShortHallway(0)
    # hallway.check_attributes()
    # hallway.blueprint()
    #
    # potential_classes = [Duck(), Dog(), Frog()]
    # pet = potential_classes[random.randint(0, 2)]
    # pet.speak()
    # grid = Grid(16, 16)
    # print(grid.squares)


    # def multi_build_test():

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