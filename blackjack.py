import random


#delcare varibles
cardsDrawn = []
playerCards = []
dealerCards = []

#Stack of Cards
cardStack = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,"Jack","Jack","Jack","Jack","Queen","Queen","Queen","Queen","King","King","King","King","ace","ace","ace","ace"]

def drawingCards():
    #Draws One Card based on random
    from random import randint

    x = randint(0,51)
    cardsDrawn.append(cardStack[x])
    cardStack.pop(x)

def checkOver21(list):
#Checks if the user hand is over 21
    sum = 0 # sum of cards
    for card in list:
        sum = sum + card
    
    if sum >> 21:
        return True
        
    else:
        return False
        print("X")

def StartofGame():
    #draws cards for player
    drawingCards()
    drawingCards()

def Game():
     StartofGame()
     print(cardsDrawn)
Game()
