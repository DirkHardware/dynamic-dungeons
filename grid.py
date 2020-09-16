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


# Grid starts by randomly generating anchors
# Structure classes a distinct signature shape expressable as a matrix that the grid class
# can read an apply to itself. These signatures must be rotatable by compass direction.
# Does the grid need to know the direction of all of its anchor points?
# What does the grid do apart from creating and exporting itself, along with
# keeping track of anchor points.
# Is it grids job to keep track of what structures it should or shouldn't be building?


if __name__ == '__main__':
    grid = Grid(16, 16)
    hallway = structures.ShortHallway(0)
    hallway.check_attributes()
    hallway.blueprint()

    # potential_classes = [Duck(), Dog(), Frog()]
    # pet = potential_classes[random.randint(0, 2)]
    # pet.speak()
    # grid = Grid(16, 16)
    # print(grid.squares)