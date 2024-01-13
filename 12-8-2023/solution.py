import re


class Node:
    name = ""
    left = ""
    right = ""
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

def getNodeWithName(nodeSet, nodeName):
    for node in nodeSet:
        if node.name == nodeName:
            return node

def main(fileName):
    file = open(fileName, "r")
    stepCount = 0
    instructions = ""
    nodeSet = set()

    for line in file:
        if instructions == "": 
            instructions = " ".join(re.findall("[a-zA-Z]+", line))
        else:
            labels = " ".join(re.findall("[a-zA-Z]+", line))
            if labels == "": continue
            else:
                label1, label2, label3 = labels.split()
                if debug: print("Words = \"{0}\" \"{1}\" \"{2}\"".format(label1, label2, label3))

                node = Node(label1, label2, label3)
                nodeSet.add(node)
                
                # Set up first node
                if label1 == "AAA": currentNode = node

    while currentNode.name != "ZZZ":
        currentInstruction = instructions[(stepCount) % len(instructions)]
        stepCount += 1

        if currentInstruction == "L":
            nextLabel = currentNode.left
        elif currentInstruction == "R":
            nextLabel = currentNode.right
        currentNode = getNodeWithName(nodeSet, nextLabel)

    print("# of Steps: {0}".format(stepCount))


debug=0
main(".\\12-8-2023\\input.txt")