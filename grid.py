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

    def offset(self):
        offset = 0
        offset_found = False
        while not offset_found:
            for column in self.current_structure.layout[0]:
                if column == structures.x:
                    offset -= 1
                else:
                    offset_found = True
        self.anchor[1] += offset
        return self.anchor

    def build(self):
        # print(self.current_structure)
        self.anchor = self.offset()
        for column in self.current_structure.layout:
            print(column)



# Grid starts by randomly generating anchor
# Structure classes a distinct signature shape expressable as a matrix that the grid class
# can read an apply to itself. These signatures must be rotatable by compass direction.
# Does the grid need to know the direction of all of its anchor points?
# What does the grid do apart from creating and exporting itself, along with
# keeping track of anchor points.
# Is it grids job to keep track of what structures it should or shouldn't be building?


if __name__ == '__main__':
    grid = Grid(16, 16)
    grid.offset()
    grid.build()
    # grid.build()
    # hallway = structures.ShortHallway(0)
    # hallway.check_attributes()
    # hallway.blueprint()
    #
    # potential_classes = [Duck(), Dog(), Frog()]
    # pet = potential_classes[random.randint(0, 2)]
    # pet.speak()
    # grid = Grid(16, 16)
    # print(grid.squares)
