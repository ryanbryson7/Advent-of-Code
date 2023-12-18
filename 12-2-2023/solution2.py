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
    def __init__(self, idIn):
        self.id = idIn

def updateMinimums(colors, game):
    for color in colors:
        colorSplit = color.split(" ")
        colorCount = int(colorSplit[0])
        colorName = colorSplit[1]
        if (colorName.find(Color.RED.name.lower()) != -1):
            game.minRedCount = max(game.minRedCount, colorCount)
        elif (colorName.find(Color.GREEN.name.lower()) != -1):
            game.minGreenCount = max(game.minGreenCount, colorCount)
        elif (colorName.find(Color.BLUE.name.lower()) != -1):
            game.minBlueCount = max(game.minBlueCount, colorCount)
    return game

def main(fileName):
    file = open(fileName, "r")
    total = 0
    for line in file:
        gameID = line.split(': ')[0].split(" ")[1]
        subGames = line.split(": ")[1].split("; ")
        game = Game(gameID)

        for subGame in subGames:
            colors = subGame.split(", ")
            game = updateMinimums(colors, game)
        
        gamePower = game.minRedCount * game.minGreenCount * game.minBlueCount
        total += gamePower
        
        if debug:
            print("Min Red: {0}, Min Green: {1}, Min Blue: {2}, POWER: {3}".format(game.minRedCount, game.minGreenCount, game.minBlueCount, gamePower))
            
    print("Total: {0}".format(total))
            

debug=0
main(".\\12-2-2023\\input.txt")
# Total on input.txt = 59795