from enum import Enum

class numberWords(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

def findWordLocations(string, word):
    arr = []
    done = False
    location = 0
    while(not done):
        done = True
        location = string.find(word, location)
        if location != -1: 
            done = False
            arr.append(location)
            location += 1

    return arr

def main(fileName):
    file = open(fileName, "r")
    sum = 0

    for ogRow in file:
        numArr = []
        newRow = ogRow
        wordArr = {}

        # Go through string and check for each numberWord
        # Replace starting char of numberWord with number
        for number in numberWords:
            wordArr = findWordLocations(ogRow, number.name.lower())
            for index in wordArr:
                newRow = newRow[:index] + str(number.value) + newRow[index + 1:]
        if debug: print(newRow)
        for char in newRow:
            if char.isdigit():
                numArr.append(char)
        sum += int(numArr[0] + numArr[len(numArr) - 1])
    print("Total: {}".format(sum))

debug=0
main(".\\12-1-2023\\input.txt")