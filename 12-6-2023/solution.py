class Race:
    Time = 0
    Record = 0
    Successess = 0
    def __init__(self, Time):
        self.Time = Time

def main(fileName):
    races = extractRacesInfo(fileName)
    if races == "":
        print("Could not load races")
        return
    
    for race in races:
        for holdTime in range(race.Time):
            distance = holdTime * (race.Time - holdTime)
            if distance > race.Record:
                race.Successess += 1
    
    total = 1
    for race in races:
        total *= race.Successess
    
    print("Total: {0}".format(total))
    
    return

def extractRacesInfo(fileName):
    file = open(fileName, "r")
    races = []

    for line in file:
        lineSplit = str.split(line)
        if str.find(lineSplit[0], "Time") != -1:
            for i in range(1, len(lineSplit)):
                race = Race(int(lineSplit[i]))
                races.append(race)
        elif str.find(lineSplit[0], "Distance") != -1:
            for i in range(1, len(lineSplit)):
                races[i - 1].Record = int(lineSplit[i])
        else:
            print("Error: Could not read line")
            return ""
        
    return races


debug=0
main(".\\12-6-2023\\input.txt")