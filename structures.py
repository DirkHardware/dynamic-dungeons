import random
x = None


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

        returns a new set of anchors for the grid to operate on.

        structure subclasses

        80's are anchors points; 80 is a north to south ("S") anchors, 81 is an east to west anchor ("W"),
        82 is a south to north anchor ("N"), 83 is a west to east anchor ("E")
    """

    def __init__(self, name=None, layout=None, area=None,
                 volume=None, width=None, height=None, offset=0):
        self.name = name
        self.layout = layout
        self.area = area
        self.width = width
        self.height = height
        self.offset = offset

    def blueprint(self):
        print(self.layout)
        return self.layout

    def __str__(self):
        return "{0.layout}, {0.anchor}".format(self)

    def apply_offset(self, anchor):
        anchor_direction = anchor[2]
        anchor_y = anchor[0]
        anchor_x = anchor[1]
        if anchor_direction == "N" or anchor_direction == "S":
            print("{0} Received anchor: {1}".format(self.name, anchor))
            print("Applying N/S offset of {}".format(self.offset))
            anchor_x += self.offset
            anchor = [anchor_y, anchor_x, anchor_direction]
            print("Returning anchor: {}".format(anchor))
            return anchor
        else:
            print("{0} Received anchor: {1}".format(self.name, anchor))
            print("Applying E/W offset of {}".format(self.offset))
            anchor_y += self.offset
            anchor = [anchor_y, anchor_x, anchor_direction]
            print("Returning anchor: {}".format(anchor))
            return anchor




class ShortHallway(Structure):

    # Okay that problem you had earlier where you were getting too many
    # arguments? The way is that the __init__ at the top takes all the position arguments
    # you feed to the method, while the super().__init__ takes all the ones you want to hardcode
    # Together they combine to assign all the properties laid out in the superclass.
    def __init__(self):
        super().__init__(name='Short Hallway', layout=[
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 0, 1],
            ["S", 0, 0, 1],
        ], volume=15, area=15, width=4, height=5)


class TeeHall(Structure):
    def __init__(self):
        super().__init__(name='Tee Hall', layout=[
            [x, 1, 0, 0, 1, x],
            [x, 1, 0, 0, 1, x],
            [x, 1, 0, 0, 1, x],
            [x, 1, 0, 0, 1, x],
            ["W", 1, 0, 0, 1, "E"],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1]
        ], volume=9, area=24, width=6, height=7, offset=-1)


class ThreeHall(Structure):
    def __init__(self):
        super().__init__(name = "Three Hall", layout=[
            [x, 1, 0, 0, 1, x],
            [x, 1, 0, 0, 1, x],
            [x, 1, 0, 0, 1, x],
            [1, 1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            ["W", 0, 0, 0, 0, "E"],
            [x, 0, 0, 0, 0, x],
            [x, "S", 0, 0, 1, x],
        ], offset=-1)


class CircleRoom7x6(Structure):
    def __init__(self):
        super().__init__(name="Circle Room 7x6", layout=[
            [x, x, 1, 0, 0, 1, x, x],
            [x, 1, 0, 0, 0, 0, 1, x],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [x, 1, 0, 0, 0, 0, 1, x],
            [x, x, 1, 0, 0, 1, x, x],
            [x, x, x, 1, 1, x, x, x],
        ], volume=26, area=38, height=7, width=8, offset=-2)
