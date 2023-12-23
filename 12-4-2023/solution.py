import math

def removeWhitespace(arrayIn):
    arrayOut = []
    for element in arrayIn:
        if str.isdigit(element):
            arrayOut.append(element)
    return arrayOut

def main(fileName):
    file = open(fileName, "r")
    total = 0

    for line in file:
        cardLabelString, numbersString = line.split("\n")[0].split(":")
        winningNumbersString, playerNumbersString = numbersString.split("|")
        winningNumbersArray = winningNumbersString.split(" ")
        playerNumbersArray = playerNumbersString.split(" ")
        winningNumbersArray = removeWhitespace(winningNumbersArray)
        playerNumbersArray = removeWhitespace(playerNumbersArray)

        if debug: print("\nWinners in {0}".format(cardLabelString))

        winningCount = 0
        for playerNumber in playerNumbersArray:
            if playerNumber in winningNumbersArray:
                winningCount += 1
                if debug: print("{0}".format(playerNumber),end=" ")
        
        if debug: print("Count: {0}".format(winningCount))
        
        if winningCount > 0:
            subTotal = 1
            for i in range(2,winningCount + 1):
                subTotal *= 2
            total += subTotal
        if debug: print("Current Total: {0}".format(total))
    print(total)

def main2(fileName):
    # create array (countArray) with count of 1 for every card
        # Go through each index of the array
        # Get the count of winning numbers
        # for each count of winning numbers
            # increase array at "(index + currentCountIncrement) * array[index]"
            # English^: increase next array value by value of array at current index
    # After all cards, loop through countArray and add values to total

    file = open(fileName, "r")
    total = 0
    
    instances = []
    for line in file:
        instances.append(1)

    file = open(fileName, "r")
    index = 0
    for line in file:
        _, numbersString = line.split("\n")[0].split(":")
        winningNumbersString, playerNumbersString = numbersString.split("|")
        winningNumbersArray = winningNumbersString.split(" ")
        playerNumbersArray = playerNumbersString.split(" ")
        winningNumbersArray = removeWhitespace(winningNumbersArray)# i.e. [83, 12]
        playerNumbersArray = removeWhitespace(playerNumbersArray)  # i.e. [83, 86, 11]

        winningCount = 0
        for playerNumber in playerNumbersArray:
            if playerNumber in winningNumbersArray:
                winningCount += 1
        if debug: print("\nCard {0} Win Count: {1}".format(index, winningCount))

        for j in range(1, winningCount + 1):
            if index + j < len(instances):
                instances[index + j] += instances[index]
        index += 1

    total = 0
    for i in range(len(instances)):
        total += instances[i]
        if debug: print("Card {0} Instance Total: {1}".format(i, instances[i]))

    print(total)



debug=0
# main(".\\12-4-2023\\input.txt")
main2(".\\12-4-2023\\input.txt")