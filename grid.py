import turtle
import random
import structures


class Grid(object):

    def __init__(self, width, height):
        self.__setX = width
        self.__setY = height
        # We don't need entrance dirs because we can just use entrance
        # dirs to set our first anchors instead.
        self.valid_structures = []
        # The below values are just for test purposes, remember to set
        # them back to a blank list when you are done.
        self.anchors = [[0, 7], [0, 9]]
        self.squares = [[]]
        for columns in range(0, self.__setX):
            self.squares[0].append(0)

        for rows in range(0, self.__setY):
            row = []
            for columns in range(0, self.__setX):
                row.append(0)
            self.squares.append(row)


class Duck(object):

    def speak(self):
        print("quack")


class Dog(object):

    def speak(self):
        print("woof")


class Frog(object):

    def speak(self):
        print('ribbit')




# Grid starts by randomly generating anchors
# Structure classes a distinct signature shape expressable as a matrix that the grid class
# can read an apply to itself. These signatures must be rotatable by compass direction.
# Does the grid need to know the direction of all of its anchor points?
# What does the grid do apart from creating and exporting itself, along with
# keeping track of anchor points.
# Is it grids job to keep track of what structures it should or shouldn't be building?

# Psuedocode: STRUCTURES
"""
    args(self, grid.squares, anchors, compass_axis[i.e. North-South, West-East)
    attributes:
    layout: a matrix that the subclass will use to operate on the grid and
    build itself out from the anchors provided. 
    area: the amount of space taken up by the matrix
    volume: the total amount of movable squares used in the structure. This might be 
    used to lend weight to certain structures. Perhaps a grid sector needs at least one room of a 
    certain volume so it's not just constantly building halls?
    
    returns a new set of anchors for the grid to operate on. 
    
    structure subclasses 
"""


if __name__ == '__main__':
    grid = Grid(16, 16)
    # print(grid.anchors)
    hallway = structures.ShortHallway("SH-1", grid.anchors, grid.squares)
    # structure = structures.ShortHallway(grid.squares, grid.anchors, 0)
    print(hallway)

    # potential_classes = [Duck(), Dog(), Frog()]
    # pet = potential_classes[random.randint(0, 2)]
    # pet.speak()
    # grid = Grid(16, 16)
    # print(grid.squares)