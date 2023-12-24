class Map:
    conversions = []
    def __init__(self):
        self.conversions = []

class Conversion:
    destinationRangeStart = 0
    destinationRangeEnd = 0
    sourceRangeStart = 0
    sourceRangeEnd = 0
    rangeLength = 0
    def __init__(self, destinationRangeStart, sourceRangeStart, rangeLength):
        self.destinationRangeStart = destinationRangeStart
        self.destinationRangeEnd = destinationRangeStart + rangeLength
        self.sourceRangeStart = sourceRangeStart
        self.sourceRangeEnd = sourceRangeStart + rangeLength
        self.rangeLength = rangeLength


def main(fileName):
    file = open(fileName, "r")
    maps = []
    currentMap = None
    seeds = None

    for line in file:
        if str.find(line, "seeds") != -1:
            seeds = line.split(": ")[1].split("\n")[0].split(" ")
        elif str.find(line, "map") != -1:
            currentMap = Map()
        elif line == "\n":
            if currentMap != None:
                maps.append(currentMap)
            currentMap = None
            continue
        else:
            currentConversion = None
            values = line.split("\n")[0].split(" ")
            currentConversion = Conversion(int(values[0]), int(values[1]), int(values[2]))
            currentMap.conversions.append(currentConversion)
    maps.append(currentMap)

    finalCoordinates = []
    for seed in seeds:
        seedCoordinate = int(seed)
        for map in maps:
            for conversion in map.conversions:
                if seedCoordinate in range(conversion.sourceRangeStart, conversion.sourceRangeEnd):
                    spacing = seedCoordinate - conversion.sourceRangeStart
                    seedCoordinate = conversion.destinationRangeStart + spacing
                    break
        finalCoordinates.append(seedCoordinate)
                
    if debug: print(finalCoordinates)
    print(min(finalCoordinates))

debug=0
main(".\\12-5-2023\\input.txt")

    # Load seeds into arrays
    # Load maps into arrays (in order)
    # Map class:
        # destinationStart
        # destinationEnd
        # sourceStart
        # sourceEnd
        # range

    # for each seed:
        # For each map
            # check each conversion to see if currentCoordinate is between sourceStart and sourceEnd
            # If there is a conversion
                # Set currentConversion (destinationStart + (sourceStart - currentCoordinate))
            # If no conversion contain the currentCoordinate, do nothing

    # Coordinates
    # [destinationStart, sourceStart, range]
    # destinationEnd = destinationStart + range
    # sourceEnd = sourceStart + range