from grid import Grid
import random


class Structure(object):

    def __init__(self, name, grid, anchors, compass_axis):
        self.name = name
        self.axis = compass_axis
        self.anchor1y = anchors[0][0]
        self.anchor1x = anchors[0][1]
        self.anchor2y = anchors[2][0]
        self.anchor2x = anchors[2][1]
        self.grid = grid
        self.layout = None
        self.area = None
        self.volume = None


class ShortHallway(sturcture):


    def __init__(self, name):
        super().__init__(name='Short Hallway')