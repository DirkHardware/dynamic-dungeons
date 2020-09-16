import random
x = 99


class Structure(object):

    # Psuedocode: STRUCTURES
    """
        args(self, layout, compass_axis[i.e. North-South, West-East)
        attributes:
        layout: a matrix that the subclass will return to the grid, which the grid
        will use to build the structure.
        area: the amount of space taken up by the matrix
        volume: the total amount of movable squares used in the structure. This might be
        used to lend weight to certain structures. Perhaps a grid sector needs at least one room of a
        certain volume so it's not just constantly building halls?

        returns a new set of anchor for the grid to operate on.

        structure subclasses
    """

    def __init__(self, name=None, compass_axis=None, layout=None, area=None, volume=None, anchor=None):
        self.name = name
        self.axis = compass_axis
        self.layout = layout
        self.area = area
        self.volume = volume
        self.anchor = anchor

    def check_attributes(self):
        print(self.volume, self.area, self.anchor)
        return [self.volume, self.area, self.anchor]

    def blueprint(self):
        print(self.layout)
        return self.layout

    def __str__(self):
        return "{0.layout}, {0.anchor}".format(self)


class ShortHallway(Structure):

    # Okay that problem you had earlier where you were getting too many
    # arguments? The way is that the __init__ at the top takes all the position arguments
    # you feed to the method, while the super().__init__ takes all the ones you want to hardcode
    # Together they combine to assign all the properties laid out in the superclss.
    def __init__(self, compass_axis):
        # super().__init__(name=name)
        super().__init__(name='Short Hallway', layout=[
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1],
        ], volume=15, area=15, anchor=[0, 0])


class TeeHall(Structure):
    def __init__(self, compass_axis):
        super().__init__(name='Tee Hall', layout=[
            [x, 1, 0, 1, x],
            [x, 1, 0, 1, x],
            [x, 1, 0, 1, x],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1]
        ], volume=9, area=24, anchor=[0, 1])
