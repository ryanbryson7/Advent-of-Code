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

def createNodes(fileName):
    file = open(fileName, "r")
    nodes = []
    rowCount = 0
    for row in file:
        # Create row
        newRow = []
        columnCount = 0
        for square in row:
            if square != '\n':
                # Create node
                newNode = node(square, [0, 0, 0, 0], rowCount, columnCount)

                newRow.append(newNode)
                columnCount += 1

                # if debug: print(newNode,end="")
        nodes.append(newRow)
        rowCount += 1
    # if debug: print("",end="\n")
    return nodes

def evaluateNode(nodes, nodeIn, directionIn, count):
    # direction1, node1, direction2, node2 = getNextMove(nodes,nodeIn, directionIn)
    # # If node/direction exist and haven't occurred before, evaluate
    # if node1 != None and direction1 != None and not nodeIn.directions[direction1.value]:
    #     if not hasNodeBeenSeen(nodeIn): 
    #         count += 1
    #         if debug == 1: print("ding1: '{0}'".format(nodeIn.shape))
    #     nodeIn.directions[direction1.value] += 1
    #     count = evaluateNode(nodes, node1, direction1, count)
    # if node2 != None and direction2 != None and not nodeIn.directions[direction2.value]:
    #     if not hasNodeBeenSeen(nodeIn): 
    #         count += 1
    #         if debug == 1: print("ding2: '{0}'".format(nodeIn.shape))
    #     nodeIn.directions[direction2.value] += 1
    #     count = evaluateNode(nodes, node2, direction2, count)



    return count

def getNextMove(nodes, nodeIn, directionIn):
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
            # node2 = getNextNode(nodes, nodeIn, direction2)
    elif nodeIn.shape == '.':
        node1 = getNextNode(nodes, nodeIn, directionIn)
        direction1 = directionIn

    return direction1, node1, direction2, node2

def getNextNode(nodes, nodeIn, directionIn):
    row = nodeIn.row
    column = nodeIn.column
    if directionIn == direction.UP:
        row += -1
    elif directionIn == direction.DOWN:
        row += 1
    elif directionIn == direction.RIGHT:
        column += 1
    elif directionIn == direction.LEFT:
        column += -1
    
    if (0 <= row < len(nodes)) and (0 <= column < len(nodes[0])): return nodes[row][column]
    else: return None

def getNextDirections(nodes, nodeIn, directionIn):
    direction1 = None
    direction2 = None

    if nodeIn.shape == '\\':
        # If even clockwise
        if (directionIn.value % 2):
            direction1 = direction((directionIn.value + 1) % 4)  # Clockwise
        else: 
            direction1 = direction((directionIn.value - 1) % 4)  # Counter-clockwise
    elif nodeIn.shape == '/':
        # If even counterclockwise
        if (directionIn.value % 2):
            direction1 = direction((directionIn.value - 1) % 4)  # Counter-clockwise
        else: 
            direction1 = direction((directionIn.value + 1) % 4)  # Clockwise
    elif nodeIn.shape == '-' or nodeIn.shape == '|':
        # Pass-through case
        if (nodeIn.shape == '-' and (directionIn == direction.RIGHT or directionIn == direction.LEFT)) or (nodeIn.shape == '|' and (directionIn == direction.UP or directionIn == direction.DOWN)):
            direction1 = directionIn
        # Perpendicular case
        else:
            direction1 = direction((directionIn.value + 1) % 4)  # Clockwise
            direction2 = direction((directionIn.value - 1) % 4)  # Counter-clockwise
    elif nodeIn.shape == '.':
        direction1 = directionIn

    return direction1, direction2

def hasNodeBeenSeen(node):
    return node.directions[0] or node.directions[1] or node.directions[2] or node.directions[3]

def main(fileName):
    nodes = createNodes(fileName)
    startNode = nodes[0][0]
    startDir,_ = getNextDirections(nodes, startNode, direction.RIGHT)
    startNode.directions[startDir.value] = 1
    count = 0
    didUpdate = True
    cycles = 0

    while (didUpdate):
        didUpdate = False
        cycles += 1
        for rowIndex in range(0, len(nodes)):
            for nodeIndex in range(0, len(nodes[rowIndex])):
                currentNode = nodes[rowIndex][nodeIndex]
                for dir in direction:
                    if currentNode.directions[dir.value] != 0:
                        dirNode = getNextNode(nodes, currentNode, dir)
                        if dirNode != None:
                            direction1, direction2 = getNextDirections(nodes, dirNode, dir) 
                            # check if direction has been taken before
                            if dirNode.directions[direction1.value] == 0 or (direction2 != None and dirNode.directions[direction2.value] == 0):
                                didUpdate = True
                                if debug: print(dirNode.shape, end="\n")

                            dirNode.directions[direction1.value] = 1
                            if direction2 != None: dirNode.directions[direction2.value] = 1
        
    # print(cycles)
    for rowIndex in range(0, len(nodes)):
        for nodeIndex in range(0, len(nodes[rowIndex])):
            currentNode = nodes[rowIndex][nodeIndex]
            if hasNodeBeenSeen(nodes[rowIndex][nodeIndex]): count += 1
    print(count)

debug=0
main(".\\12-16-2023\\input.txt")