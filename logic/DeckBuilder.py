from logic.Deck import *
from logic.DeckError import *

class DeckBuilder:
    max_cards = 10

    def __init__(self):
        """
        Constructor that intializes the deck builder, it checks if the calculated maximum
        for each rarity exceeds or is less than the number of cards needed for a deck, and
        if so it changes the basic maximum to fix this.
        """
        self.max_urs = round(self.max_cards*0.1)
        self.max_mrs = round(self.max_cards*0.15)
        self.max_rs = round(self.max_cards*0.2)
        self.max_ns = round(self.max_cards*0.25)

    def getMaxCards(self):
        """
        getMaxCards adds the total number of cards and the maximum number for each
        rarity to a list to return it.

        :return: list with the maximum number of cards, ultrarares, veryrares, rares, normals and basics.
        """
        maxs = [self.max_cards, self.max_urs, self.max_mrs, self.max_rs, self.max_ns]
        return maxs
    
    def createDeck(self, player, name, cards):
        """
        createDeck checks if the player has any space for a new deck, then checks if there are any
        repeated cards (a main and a variant) and the number of cards of each rarity to verify the
        maximum of each is not surpassed, if all cards are valid the deck is created and given to 
        the player.

        :player: player that is creating the deck.
        :name: string with the name of the deck.
        :cards: list of cards to be added to the deck.
        :return: int corresponding to the result of the creation.
        """
        decks = player.showDecks()
        if len(decks) >= 15:
            return DeckError.NO_SPACE.value

        for d in decks:
            if d.getName() == name:
                return DeckError.USED_NAME.value
        urs = 0
        mrs = 0
        rs = 0
        ns = 0
        for i in cards:
            for j in cards:
                if i.getName() == j.getName() and not (i is j):
                    return DeckError.DUPLICATE_CARD.value
            rarity = i.getRarity()
            match rarity:
                case "Ultra-Rara":
                    urs += 1
                case "Muy Rara":
                    mrs += 1
                case "Rara":
                    rs += 1
                case "Normal":
                    ns += 1

        if urs > self.max_urs:
            return DeckError.TOO_MANY_URS.value
        if mrs > self.max_mrs:
            return DeckError.TOO_MANY_MRS.value
        if rs > self.max_rs:
            return DeckError.TOO_MANY_RS.value
        if ns > self.max_ns:
            return DeckError.TOO_MANY_NS.value
        
        newDeck = Deck(name, cards)
        return player.addDeck(newDeck)