def addHallway(entrance_dir, anchors, grid):
    anchor1y = anchors[0][0]
    anchor1x = anchors[0][1]
    anchor2y = anchors[2][0]
    anchor2x = anchors[2][1]
    print(anchor1x, anchor1y)
    print(anchor2x, anchor2y)
    hallway_length = 7
    for squares in range(hallway_length):
        grid[anchor1y + squares][anchor1x] = 1
        grid[anchor2y + squares][anchor2x] = 1
    return grid