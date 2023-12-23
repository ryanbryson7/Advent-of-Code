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

debug=0
main(".\\12-4-2023\\input.txt")