from Deck import *

class DeckBuilder:
    max_cards = 15
    max_urs = round(max_cards*0.1)
    max_mrs = round(max_cards*0.15)
    max_rs = round(max_cards*0.2)
    max_ns = round(max_cards*0.25)
    max_bs = round(max_cards*0.3)

    def __init__(self):
        """
        Constructor that intializes the deck builder, it checks if the calculated maximum
        for each rarity exceeds or is less than the number of cards needed for a deck, and
        if so it changes the basic maximum to fix this.
        """
        totals = self.max_urs + self.max_mrs + self.max_rs + self.max_ns + self.max_bs
        if totals < self.max_cards:
            self.max_bs += self.max_cards - totals
        elif totals > self.max_cards:
            self.max_bs -= totals - self.max_cards

    def getMaxCards(self):
        """
        getMaxCards adds the total number of cards and the maximum number for each
        rarity to a list to return it.

        :return: list with the maximum number of cards, ultrarares, veryrares, rares, normals and basics.
        """
        maxs = [self.max_cards, self.max_urs, self.max_mrs, self.max_rs, self.max_ns, self.max_bs]
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
        if len(player.showDecks()) >= 15:
            return -1

        urs = 0
        mrs = 0
        rs = 0
        ns = 0
        bs = 0
        for i in cards:
            for j in cards:
                if i.getName() == j.getName() and not (i is j):
                    return -2
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
                case "Básica":
                    bs += 1

        if urs > self.max_urs:
            return -3
        if mrs > self.max_mrs:
            return -4
        if rs > self.max_rs:
            return -5
        if ns > self.max_ns:
            return -6
        if bs > self.max_bs:
            return -7
        
        newDeck = Deck(name, cards)
        return player.addDeck(newDeck)