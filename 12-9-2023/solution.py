def GetNextReadingValue(inputArray):
    if IsArrayZeros(inputArray):
        return 0
    
    # Create difAry
    difAry = []
    for index in range(len(inputArray) - 1):
        difference = inputArray[index + 1] - inputArray[index]
        difAry.append(difference)
    nextDifference = GetNextReadingValue(difAry)

    # Get next value, add to array
    nextValue = inputArray[len(inputArray) - 1] + nextDifference

    return nextValue

def IsArrayZeros(inputArray):
    for value in inputArray:
        if value != 0: return False
    return True

def main(fileName, part):
    # Setup
    file = open(fileName, "r")
    summation = 0
    nextReadings = []

    # Find next reading for each line
    for line in file:
        # Read in line data
        readingsDirty = line.split()
        readings = []

        # Convert data to integers
        for reading in readingsDirty:
            readings.append(int(reading))

        if part == 2: readings.reverse()

        nextReadings.append(GetNextReadingValue(readings))

    # Add next reading values together
    for nextReading in nextReadings:
        summation += nextReading

    # Show solution
    print("Sum of values: {0}".format(summation))

debug=1
main(".\\12-9-2023\\input.txt", 2)

# Recursive Algorithm GetNextReading(inputArray):
    # Base case: If inputArray is all 0's, return 0
    # Recursive Case: 
        # Create array of differences "difAry"
        # Call GetNextReading(difAry)
        # Return next value using result of ^ and last value of inputArray

# Part 2:
    # Just reverse the readings Array before computing next values