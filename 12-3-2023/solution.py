def createGrid(file):
    grid = []
    rowCount = 0
    for line in file:
        row = []
        columnCount = 0
        for char in line:
            if char != "\n":
                row.append(char)
                columnCount += 1
        rowCount += 1
        grid.append(row)

    return grid

def updateAllNeighbors(grid, rowIndex, cellIndex):
    didUpdate = False
    didUpdate = updateHorizontalNeighbors(grid, rowIndex, cellIndex) or didUpdate
    result, upRowIndex, downRowIndex = updateVerticalNeighbors(grid, rowIndex, cellIndex)
    didUpdate = result or didUpdate

    if 0 <= upRowIndex:
        didUpdate = updateHorizontalNeighbors(grid, upRowIndex, cellIndex) or didUpdate
    if downRowIndex < len(grid): 
        didUpdate = updateHorizontalNeighbors(grid, downRowIndex, cellIndex) or didUpdate

    return didUpdate

def updateHorizontalNeighbors(grid, rowIndex, cellIndex):
    leftCellIndex = cellIndex - 1
    rightCellIndex = cellIndex + 1
    didUpdate = False

    if 0 <= leftCellIndex:
        if (str.isdigit(grid[rowIndex][leftCellIndex])):
            grid[rowIndex][leftCellIndex] = "n"
            didUpdate = True
    if rightCellIndex < len(grid[rowIndex]):
        if (str.isdigit(grid[rowIndex][rightCellIndex])):
            grid[rowIndex][rightCellIndex] = "n"
            didUpdate = True
    
    return didUpdate

def updateVerticalNeighbors(grid, rowIndex, cellIndex):
    upRowIndex = rowIndex - 1
    downRowIndex = rowIndex + 1
    didUpdate = False

    if 0 <= upRowIndex:
        if (str.isdigit(grid[upRowIndex][cellIndex])):
            grid[upRowIndex][cellIndex] = "n"
            didUpdate = True
    if downRowIndex < len(grid):
        if (str.isdigit(grid[downRowIndex][cellIndex])):
            grid[downRowIndex][cellIndex] = "n"
            didUpdate = True

    return didUpdate, upRowIndex, downRowIndex

def main(fileName):
    file = open(fileName, "r")
    originalGrid = createGrid(file)
    file = open(fileName, "r")
    nGrid = createGrid(file)
    didUpdate = True
    cycles = 0

    while (didUpdate):
        cycles += 1
        if debug: print("Cycle #{0}".format(cycles))
        didUpdate = False
        for rowIndex in range(0, len(nGrid)):
            for cellIndex in range(1, len(nGrid[rowIndex])):
                cell = nGrid[rowIndex][cellIndex]
                if cell == "." or str.isdigit(cell): continue
                elif not str.isalnum(cell):
                    # check all neighbors
                    didUpdate = updateAllNeighbors(nGrid, rowIndex, cellIndex) or didUpdate
                elif cell == "n":
                    # check horizontal neighbors
                    didUpdate = updateHorizontalNeighbors(nGrid, rowIndex, cellIndex) or didUpdate
                else:
                    print("Unidentified character: {0}".format(cell))

    total = 0
    for rowIndex in range(0, len(nGrid)):
        currentNumber = ""
        for cellIndex in range(0, len(nGrid[rowIndex])):
            if nGrid[rowIndex][cellIndex] == 'n': 
                currentNumber += originalGrid[rowIndex][cellIndex]
            elif currentNumber != "": 
                if debug: print(currentNumber)
                total += int(currentNumber)
                currentNumber = ""
        if currentNumber != "":
            if debug: print(currentNumber)
            total += int(currentNumber)


    print("Total: {0}".format(total))

            

debug=0
main(".\\12-3-2023\\input.txt")
# Total input with input = 

    # load input into two grids (original, n-indexed)
    # iterate through every cell in the original grid
    # If the cell is a symbol
        # update neighbors (8 surrounding cells)
            # if neighbor is a number, convert it to an "n" in the n-indexed grid
    # if the cell is an "n"
        # update neighbors (2 horizontal cells)
            # if neighbor is a number, convert it to an "n" in the n-indexed grid

    # Iterate through every cell n-indexed grid
    # If cell is a symbol or "."
        # Interpret current number and add to total
    # If cell = "n"
        # Append original cell value to current number