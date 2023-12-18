from enum import Enum

class Color(Enum):
    RED = 12
    GREEN = 13
    BLUE = 14

class Game:
    id = 0
    minRedCount = 0
    minGreenCount = 0
    minBlueCount = 0

def IsGameColorsValid(colors):
    for color in colors:
        colorSplit = color.split(" ")
        colorCount = colorSplit[0]
        colorName = colorSplit[1]
        for color in Color:
            if (colorName == color.name.lower()):
                if int(colorCount) > color.value: return False
    return True

def main(fileName):
    file = open(fileName, "r")
    sum = 0
    for line in file:
        gameID = line.split(': ')[0].split(" ")[1]
        subGames = line.split(": ")[1].split("; ")
        isValid = True

        for subGame in subGames:
            colors = subGame.split(", ")
            if not IsGameColorsValid(colors): 
                isValid = False
        if isValid:
            sum += int(gameID)
            if debug: print(gameID)
    print("Total: {0}".format(sum))
            

debug=0
main(".\\12-2-2023\\input.txt")