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

def isValidSeed(seed, seedRanges):
    for i in range(0, len(seedRanges), 2):
        startRange = int(seedRanges[i])
        endRange = startRange + int(seedRanges[i + 1])
        if seed in range(startRange, endRange):
            return True
    return False


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
    maps.reverse()

    matchFound = False
    seedLocation = 0
    seedCoordinate = 0
    while (not matchFound):
        seedLocation += 1
        seedCoordinate = seedLocation

        if debug and seedLocation % 50000 == 0:
            print("No matches by {0}".format(seedLocation))

        for map in maps:
            for conversion in map.conversions:
                if seedCoordinate in range(conversion.destinationRangeStart, conversion.destinationRangeEnd):
                    spacing = seedCoordinate - conversion.destinationRangeStart
                    seedCoordinate = conversion.sourceRangeStart + spacing
                    break
        if (isValidSeed(seedCoordinate, seeds)):
            matchFound = True
                
    print("Seed: {0}, Location: {1}".format(seedCoordinate, seedLocation))

debug=1
main(".\\12-5-2023\\input.txt")
    # Solution: 
    # Seed: 1950497840, Location: 9622622

    # Similar algorithm as part 1
    # Instead, we reverse the map order, check every location in increasing order
    # We swap our use of the source/destination to convert the location into a seed
    # We then check our list of seed ranges to see if the converted seed actually exists
    # The first seed we find that actually exists is our answer.