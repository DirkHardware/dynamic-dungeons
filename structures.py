from grid import Grid
import random


class Structure(object):

    def __init__(self, name, layout, grid, anchors, compass_axis):
        self.name = name
        self.axis = compass_axis
        # It might be easier to just use ONE anchor point
        self.anchor1y = anchors[0][0]
        self.anchor1x = anchors[0][1]
        self.anchor2y = anchors[1][0]
        self.anchor2x = anchors[1][1]
        self.grid_squares = grid
        self.layout = None
        self.area = None
        self.volume = None

    def construct(self):
        # This is assuming a northern entrance building downwards
        for rows in self.layout:
            anchor1x = self.anchor1x
            anchor1y = self.anchor1y - 1
            for column in rows:
                for square in column:
                    if grid_squares[anchor1x][anchor1y] != squares:
                        grid_squares = [anchor1x][anchor1y]
                anchor1y - 1

    def __str__(self):
        print(self.grid_squares)
        return "{0.anchor1y}, {0.anchor1x}, {0.anchor2y}, {0.anchor2x}".format(self)
        # print(self.anchor1y, self.anchor1x)
        # print(self.anchor2y, self.anchor2x)


class ShortHallway(Structure):

    def __init__(name, layout, grid, anchors, compass_axis):
        super().__init__(name='Short Hallway', layout=[
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
        ])
