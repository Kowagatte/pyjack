from enum import Enum
import random

class Suit(Enum):
    spade = 'S'
    club = 'C'
    heart = 'H'
    diamond = 'D'

class Value(Enum):
    king = 'K'
    queen = 'Q'
    jack = 'J'
    ten = 'T'
    nine = '9'
    eight = '8'
    seven = '7'
    six = '6'
    five = '5'
    four = '4'
    three = '3'
    two = '2'
    ace = 'A'

class Game:
    def __init__(self, house, player):
        self.house = house
        self.player = player
        self.deck = deck

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def chooseRandSuit():
    list = [index for index in Suit]
    x = random.randint(0, 3)
    return list[x]

def chooseRandValue():
    list = [index for index in Value]
    x = random.randint(0, 12)
    return list[x]

def drawCard():
    suit = chooseRandSuit()
    value = chooseRandValue()
    return Card(suit, value)

def getValue(card):
    value = card.value
    if(value == Value.ace):
        return -1
    elif(value == Value.two):
        return 2
    elif(value == Value.three):
        return 3
    elif(value == Value.four):
        return 4
    elif(value == Value.five):
        return 5
    elif(value == Value.six):
        return 6
    elif(value == Value.seven):
        return 7
    elif(value == Value.eight):
        return 8
    elif(value == Value.nine):
        return 9
    elif(value == Value.ten):
        return 10
    elif(value == Value.jack):
        return 10
    elif(value == Value.queen):
        return 10
    elif(value == Value.king):
        return 10
    else:
        return 0

def settingUpDeck():
    deck = []
    suits = [suit for suit in Suit]
    values = [value for value in Value]
    for s in suits:
        for v in values:
            deck.append(Card(s, v))
    return deck

def printDeck():
    deck = settingUpDeck()
    for card in deck:
        print(card.suit.value + card.value.value)

def askforInput():
    x = True
    command = input("hit or stay: ")
    while x:
        if(command == "hit"):
            x = False
            break
        if(command == "stay"):
            x = False
            break
        command = input("hit or stay: ")
    return command
        
def printHand(list):
    hand = []
    for card in list:
        s = card.suit.value + card.value.value
        hand.append(s)
    return hand

def printGame():
    print()
    print("House:", printHand(house))
    print("The house's hand is worth", str(calculateHand(house)))
    print("You:", printHand(player))
    print("your hand is worth", str(calculateHand(player)))
    print()

def calculateHand(hand):
    totalHandValue = 0
    for card in hand:
        value = getValue(card)
        if(value >= 0):
            totalHandValue = totalHandValue + value
    for card in hand:
        value = getValue(card)
        if(value == -1):
            if((totalHandValue + 11) > 21):
                totalHandValue = totalHandValue + 1
            else:
                totalHandValue = totalHandValue + 11
    return totalHandValue

house = []
player = []
gameOver = False

def judgeGame():
    global gameOver
    houseScore = calculateHand(house)
    playerScore = calculateHand(player)
    if(playerScore < 21):
        if((houseScore <= 21) and (houseScore > playerScore)):
            print("House wins!")
            gameOver = True
            return
        if(houseScore > 21):
            print("Bust. You win!")
            gameOver = True
            return
        if(houseScore == 21):
            print("Blackjack. House wins!")
            gameOver = True
            return
    if(playerScore == 21):
        if(houseScore == 21):
            print("Push.")
            gameOver = True
            return
        if(houseScore > 21):
            print("Bust. You win!")
            gameOver = True
            return
    if(playerScore > 21):
        print("Bust. House wins!")
        gameOver = True
        return

def blackJack():
    global gameOver
    houseScore = calculateHand(house)
    playerScore = calculateHand(player)
    if(playerScore == 21):
        house.append(drawCard())
        houseScore = calculateHand(house)
        if(houseScore == 21):
            print("Push.")
            gameOver = True
            return
        else:
            print("Blackjack. You win!")
            gameOver = True
            return

def setupGame():
    house.append(drawCard())
    player.append(drawCard())
    player.append(drawCard())
    printGame()

def gameLoop():
    setupGame()
    blackJack()
    if(gameOver):
        return
    command = askforInput()
    while (command == "hit"):
        player.append(drawCard())
        printGame()
        judgeGame()
        if(gameOver or (calculateHand(player) == 21)):
            command = "stay"
            break
        command = askforInput()
    if(not gameOver):
        while (not gameOver):
            house.append(drawCard())
            printGame()
            judgeGame()
        return

def start():
    global house
    global player
    global gameOver
    house = []
    player = []
    gameOver = False
    gameLoop()
