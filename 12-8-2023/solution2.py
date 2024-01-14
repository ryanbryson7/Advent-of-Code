import math
import re

class Node:
    name = ""
    left = ""
    right = ""
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    def __str__(self):
        return self.name
    
class Path:
    id = 0
    zPoints = []
    zPointStepCount = []
    finished = False
    def __init__(self, id, zPoints, zPointStepCount):
        self.id = id
        self.zPoints = zPoints
        self.zPointStepCount = zPointStepCount

def getNodeWithName(nodeSet, nodeName):
    for node in nodeSet:
        if node.name == nodeName:
            return node

def getNextNodeLabel(node, instruction):
    nextLabel = ""
    if instruction == "L":
        nextLabel = node.left
    elif instruction == "R":
        nextLabel = node.right
    return nextLabel

def getNextNodes(nodeSet, instruction, nodeList):
    newNodes = []
    newNodeLabels = []

    for node in nodeList:
        nextLabel = getNextNodeLabel(node, instruction)
        newNodeLabels.append(nextLabel)
    for nodeLabel in newNodeLabels:
        newNodes.append(getNodeWithName(nodeSet, nodeLabel))

    return newNodes

def tryAddZPoints(paths, nodes, instructionIndex, stepCount):
    addedNewZPoint = 0
    for i in range(len(nodes)):
        if nodes[i].name[len(nodes[i].name) - 1] == "Z":
            addedNewZPoint = 1
            instructionKey = str(instructionIndex) + nodes[i].name
            if not instructionKey in paths[i].zPoints:
                paths[i].zPoints.append(instructionKey)
                paths[i].zPointStepCount.append(stepCount)
                addedNewZPoint = 2
            else: 
                if debug: print("Finished path {0}".format(i))
                paths[i].finished = True
            addedNewZPoint = max(addedNewZPoint, 1)
    return paths

def arePathsFinished(paths):
    for path in paths:
        if not path.finished: return False
    return True

def main(fileName):
    file = open(fileName, "r")
    stepCount = 0
    instructions = ""
    nodeSet = set()
    currentNodes = []

    for line in file:
        if line == "": continue
        elif instructions == "": 
            instructions = " ".join(re.findall("[a-zA-Z0-9]+", line))
        else:
            labels = " ".join(re.findall("[a-zA-Z0-9]+", line))
            if labels == "": continue
            else:
                label1, label2, label3 = labels.split()
                if debug: print("Words = \"{0}\" \"{1}\" \"{2}\"".format(label1, label2, label3))

                node = Node(label1, label2, label3)
                nodeSet.add(node)
                
                if label1[len(label1) - 1] == "A": currentNodes.append(node)


    instructionLength = len(instructions)
    paths = []
    for i in range(len(currentNodes)):
        newPath = Path(i, [], [])
        paths.append(newPath)

    while not arePathsFinished(paths):
        instructionIndex = (stepCount) % instructionLength
        currentInstruction = instructions[(stepCount) % instructionLength]

        stepCount += 1
        currentNodes = getNextNodes(nodeSet, currentInstruction, currentNodes)
        paths = tryAddZPoints(paths, currentNodes, instructionIndex, stepCount)
    
    if debug: print("Paths calculated in {0} steps, or {1} instructions cycles".format(stepCount, stepCount / instructionLength  ))

    cycleLengths = []

    for path in paths:
        cycleLength = int(path.zPointStepCount[0] / instructionLength)
        cycleLengths.append(cycleLength)
    
    lcm = cycleLengths[0]
    for i in range(1, len(cycleLengths)):
        lcm = math.lcm(lcm, cycleLengths[i])
    totalSteps = lcm * instructionLength

    print("# of Steps: {0}".format(totalSteps))

debug=0
main(".\\12-8-2023\\input.txt")

# Note: This solution doesn't work on the example input, only the test input
# The input.txt file is unique in that each starting point only gets to a finish point at the
# very end of the instructions. So we only ever have a single cycle. However, in the example input
# path 2 hits a different "z" node every 3rd and 6th step. So the algorithm won't check all the 
# possible "z" nodes, and actually has issues if the "z" node occurs on an odd step. It's janky and
# I could add some handling easily for the odd number problems, but the multiple cycles issue is a 
# much harder fix. Regardless, I'm not going further with this since I've found the answer, sorry.