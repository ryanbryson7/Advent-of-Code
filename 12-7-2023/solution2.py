from enum import Enum

class HandValue(Enum):
    HIGHCARD = "1"
    ONEPAIR = "2"
    TWOPAIR = "3"
    THREEOFAKIND = "4"
    FULLHOUSE = "5"
    FOUROFAKIND = "6"
    FIVEOFAKIND = "7"

class Letter(Enum):
    T = "10"
    J = "00"
    Q = "12"
    K = "13"
    A = "14"

class Hand:
    id = ""
    bid = 0
    handString = ""
    def __init__(self, id, bid, handString):
        self.id = id
        self.bid = bid
        self.handString = handString


def getHandID(handStringIn):
    handID = ""
    handString = getJokerFilledHand(handStringIn)

    # Get Hand Value
    uniqueCards = set(handString)
    if (len(uniqueCards) == 5):
        handID = HandValue.HIGHCARD.value
    elif (len(uniqueCards) == 4):
        handID = HandValue.ONEPAIR.value
    elif (len(uniqueCards) == 3):
        for card in uniqueCards:
            if handString.count(card) == 3:
                handID = HandValue.THREEOFAKIND.value
                continue
        if handID == "":
            handID = HandValue.TWOPAIR.value
    elif (len(uniqueCards) == 2):
        for card in uniqueCards:
            if handString.count(card) == 4:
                handID = HandValue.FOUROFAKIND.value
                continue
        if handID == "":
            handID = HandValue.FULLHOUSE.value
    elif (len(uniqueCards) == 1):
        handID = HandValue.FIVEOFAKIND.value
    
    # Append Individual Card Values
    for card in handStringIn:
        cardString = ""
        if str.isdigit(card):
            cardString = "0" + str(card)
        else:
            cardString = getattr(Letter, card).value
        handID += cardString

    return handID

def getJokerFilledHand(handStringIn):
    handString = ""
    jokerCount = 0

    # Remove "J"s from string
    for char in handStringIn:
        if char != "J":
            handString += char
        else:
            jokerCount += 1

    if jokerCount == 0 or handString == "": return handStringIn

    # Find most common letter
    cards = {}
    for i in handString:
        if i in cards:
            cards[i] += 1
        else:
            cards[i] = 1
    mostCommonLetter = max(cards, key = cards.get)

    for i in range(jokerCount):
        handString += mostCommonLetter


    if debug: print("{0} => {1}".format(handStringIn, handString))

    return handString

def main(fileName):
    file = open(fileName, "r")

    hands = []
    for line in file:
        handString, handBid = line.split()
        handID = getHandID(handString)
        hand = Hand(handID, int(handBid), handString)
        hands.append(hand)
    
    hands.sort(key=idSort)

    winnings = 0
    rank = 1
    for hand in hands:
        if debug: print("Hand: {0}, Bid: {1}, Rank: {2}, Score: {3}".format(hand.handString, hand.bid, rank, hand.bid * rank))
        winnings += hand.bid * rank
        rank += 1


    print("Winnings: {0}".format(winnings))


def idSort(hand):
    return hand.id

debug=0
main(".\\12-7-2023\\input.txt")

# Similar to part 1, only need to change handValue calculation

# Loop through all hands
# Create hand object
    # Create hand ID: HandValue + card values (all 5)
        # NEW HAND VALUE JOKER CONSIDERATION
            # If hand doesn't have a "J", score hand normally
            # Make a copy of handString to without J's
            # Make count "n" of J's
            # Find the highest occuring letter "l" in copy
            # Append "n" instances of "l" to the copy
            # Score the copy as if it's the actual hand

# Add Hand to handlist
# Sort handlist on the hand ID

# Loop through handlist
    # Decrement rank on each iteration
    # Calculate hand score (bid * rank) and add to total
# Print total