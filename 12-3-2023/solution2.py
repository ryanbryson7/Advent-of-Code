class Part:
    number = ""
    def __init__(self, number):
         self.number = number

def createGrid(file):
    grid = []
    for line in file:
        row = []
        part = None
        for char in line:
            if str.isdigit(char):
                if part == None:
                    part = Part(char)
                else:
                    part.number = part.number + char
                row.append(part)
            elif char != "\n":
                part = None
                row.append(char)
        grid.append(row)

    return grid

def getGearRatio(grid, rowIndex, cellIndex):
    gearRatio = 0

    prevRowIndex = rowIndex - 1
    nextRowIndex = rowIndex + 1
    prevCellIndex = cellIndex - 1
    nextCellIndex = cellIndex + 1

    rowIndicies = [prevRowIndex, rowIndex, nextRowIndex]
    cellIndicies = [prevCellIndex, cellIndex, nextCellIndex]

    neighbors = set()
    for rowIndicie in rowIndicies:
        for cellIndicie in cellIndicies:
            if 0 <= rowIndicie < len(grid) and 0 <= cellIndicie < len(grid[rowIndicie]):
                cell = grid[rowIndicie][cellIndicie]
                if isinstance(cell, Part):
                    neighbors.add(cell)

    if len(neighbors) == 2:
        if debug: print("Valid Gear found: {0} and {1}".format(neighbors[0].number, neighbors[1].number))
        gearRatio = 1
        for part in neighbors:
            gearRatio *= int(part.number)

    return gearRatio

def main(fileName):
    file = open(fileName, "r")
    grid = createGrid(file)
    total = 0

    for rowIndex in range(0, len(grid)):
        for cellIndex in range(1, len(grid[rowIndex])):
            cell = grid[rowIndex][cellIndex]
            gearRatio = 0
            if cell == "." or isinstance(cell, Part): continue
            elif not str.isalnum(cell):
                # check all neighbors
                gearRatio = getGearRatio(grid, rowIndex, cellIndex)
            else:
                print("Unidentified character: {0}".format(cell))
            total += gearRatio
    
    print("Total: {0}".format(total))

debug=0
main(".\\12-3-2023\\input.txt")

# Set up grid:
# Go through every cell
    # If cell is a number 
        # If it's a new part number, 
            # create a part number string
            # Create a Part object and set the grid at that location to this new object
        # If not, 
            # append it to the current running part number
            # Create a Part object and set the grid at that location to this new object

# Calculate Gear Ratios:
# Go through every cell
    # If cell is a symbol (not a '.')
        # Check it's eight neighbors
        # if there are exactly TWO neighbors, and those neighbors aren't the same Part object, 
            # gearRatio = part1 * part2
    # Total += gearRatio
