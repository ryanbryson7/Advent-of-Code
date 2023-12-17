from enum import Enum

class direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class node:
    directions = []
    shape = ""
    row = 0
    column = 0
    def __init__(self, shapeIn, directionsIn, rowIn, columnIn):
        self.shape = shapeIn
        self.directions = directionsIn
        self.row = rowIn
        self.column = columnIn
    def __str__(self):
        return self.shape

def createNodes():
    file = open(".\\12-16-2023\\input.txt", "r")
    nodes = []
    rowCount = 0
    for row in file:
        # Create row
        newRow = []
        columnCount = 0
        for square in row:
            # Create node
            newNode = node(square, [0, 0, 0, 0], rowCount, columnCount)
            # newNode.shape=square
            # for i in range(0,4):
            #     newNode.directions.append(0)
            # newNode.row = rowCount
            # newNode.column = columnCount

            newRow.append(newNode)
            columnCount += 1

            if debug: print(newNode,end="")
        nodes.append(newRow)
        rowCount += 1
    if debug: print("",end="\n")
    return nodes

def evaluateNode(nodes,nodeIn, directionIn, count):
    direction1, node1, direction2, node2 = getNextMove(nodes,nodeIn, directionIn)
    # If node/direction exist and haven't occurred before, evaluate
    if node1 != None and direction1 != None and not nodeIn.directions[direction1.value]:
        if not hasNodeBeenSeen(nodeIn): 
            count += 1
            if debug == 1: print("ding1: '{0}'".format(nodeIn.shape))
        nodeIn.directions[direction1.value] += 1
        count = evaluateNode(nodes, node1, direction1, count)
    if node2 != None and direction2 != None and not nodeIn.directions[direction2.value]:
        if not hasNodeBeenSeen(nodeIn): 
            count += 1
            if debug == 1: print("ding2: '{0}'".format(nodeIn.shape))
        nodeIn.directions[direction2.value] += 1
        count = evaluateNode(nodes, node2, direction2, count)

    return count

def getNextMove(nodes,nodeIn, directionIn):
    node1 = None
    node2 = None
    direction1 = None
    direction2 = None

    if nodeIn.shape == '\\':
        # If even clockwise
        if (directionIn.value % 2):
            direction1 = direction((directionIn.value + 1) % 4)  # Clockwise
        else: 
            direction1 = direction((directionIn.value - 1) % 4)  # Counter-clockwise
        node1 = getNextNode(nodes, nodeIn, direction1)
    elif nodeIn.shape == '/':
        # If even counterclockwise
        if (directionIn.value % 2):
            direction1 = direction((directionIn.value - 1) % 4)  # Counter-clockwise
        else: 
            direction1 = direction((directionIn.value + 1) % 4)  # Clockwise
        node1 = getNextNode(nodes, nodeIn, direction1)
    elif nodeIn.shape == '-' or nodeIn.shape == '|':
        # Pass-through case
        if (nodeIn.shape == '-' and (directionIn == direction.RIGHT or directionIn == direction.LEFT)) or (nodeIn.shape == '|' and (directionIn == direction.UP or directionIn == direction.DOWN)):
            node1 = getNextNode(nodes, nodeIn, directionIn)
            direction1 = directionIn
        # Perpendicular case
        else:
            direction1 = direction((directionIn.value + 1) % 4)  # Clockwise
            direction2 = direction((directionIn.value - 1) % 4)  # Counter-clockwise
            node1 = getNextNode(nodes, nodeIn, direction1)
            node2 = getNextNode(nodes, nodeIn, direction2)
    elif nodeIn.shape == '.':
        node1 = getNextNode(nodes, nodeIn, directionIn)
        direction1 = directionIn

    return direction1, node1, direction2, node2

def getNextNode(nodes,nodeIn, directionIn):
    row = nodeIn.row
    column = nodeIn.column
    if directionIn == direction.UP:
        row += -1
    if directionIn == direction.DOWN:
        row += 1
    if directionIn == direction.RIGHT:
        column += 1
    if directionIn == direction.LEFT:
        column += -1
    try:
        return nodes[row][column]
    except:
        return None
    
def hasNodeBeenSeen(node):
    return node.directions[0] or node.directions[1] or node.directions[2] or node.directions[3]

def main():
    nodes = createNodes()
    startingNode = nodes[0][0]
    startingDirection = direction.RIGHT
    count = 0

    count = evaluateNode(nodes, startingNode, startingDirection, count)
    print(count)

debug=0
main()