from datetime import date
from KeyGeneration import generateKey

class Deck:
    name = ""
    cards = []
    creation_date = ""
    id = ""

    def __init__(self, name, cards):
        self.name = name

        self.creation_date = date.today
        id = "D-" + generateKey()

        self.addCards(cards)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def getCreationDate(self):
        return self.creation_date

    def addCards(self, cards):
        self.cards = cards

    def getCards(self):
        return self.cards

    def isValid(self):
        for i in self.cards:
            if not i.gameActive():
                return False
        return True