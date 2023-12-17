

def main(fileName):
    file = open(fileName, "r")
    sum = 0
    for row in file:
        numArr = []
        for char in row:
            if char.isdigit():
                numArr.append(char)
        sum += int(numArr[0] + numArr[len(numArr) - 1])
    print("Total: {}".format(sum))

debug=0
main(".\\12-1-2023\\input.txt")