import random
x = None


class Structure(object):

    def __init__(self, name=None, layout=None, area=None,
                 volume=None, width=None, height=None, offset=0):
        self.name = name
        self.layout = layout
        self.area = area
        self.width = width
        self.height = height
        # This value is used to center the structure during building
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

    # This method must be used when rotating a structure westward.
    # It swaps the position of the anchor with it's neighbor 1 square on the other side of the exit. Otherwise
    # structures building from that anchor will be off.
    def swap_anchors(self, anchors=[[]], swaps=[[]]):
        i = 0
        for anchor in anchors:
            anchor_y = anchor[0]
            anchor_x = anchor[1]
            anchor_type = anchor[2]
            swap = swaps[i]
            swap_y = swap[0]
            swap_x = swap[1]
            print("Swapping anchor @ Y:{0} X: {1} --> Y:{2} X:{3}".format(anchor_y, anchor_x, swap_y, swap_x))
            self.layout[swap_y][swap_x] = anchor_type
            self.layout[anchor_y][anchor_x] = 1
            i += 1


class DeadEnd(Structure):
    def __init__(self):
        super().__init__(name="Dead End", layout=[
            [1, 0, 0, 1],
            [1, 1, 1, 1]
        ], area=8, width=4, height=4)

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

    def swap_anchors(self):
        super().swap_anchors(anchors=[[4, 0, "W"], [4, 5, "E"]], swaps=[[7, 0], [7, 5]])


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


class JCircleRoom7x6(Structure):
    def __init__(self):
        super().__init__(name="Circle Room 7x6", layout=[
            [x, 1, 0, 0, 1, x, x],
            [1, 0, 0, 0, 0, 1, x],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1],
            ["W", 0, 0, 0, 0, 1, x],
            [x, 1, 0, 0, 1, x, x],
            [x, x, 1, 1, x, x, x],
        ], volume=26, area=38, height=7, width=8, offset=-1)
