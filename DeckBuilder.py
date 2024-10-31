from Deck import *

class DeckBuilder:
    max_cards = 15
    max_urs = round(max_cards*0.1)
    max_mrs = round(max_cards*0.15)
    max_rs = round(max_cards*0.2)
    max_ns = round(max_cards*0.25)
    max_bs = round(max_cards*0.3)

    def __init__(self):
        totals = self.max_urs + self.max_mrs + self.max_rs + self.max_ns + self.max_bs
        if totals < self.max_cards:
            self.max_bs += self.max_cards - totals
        elif totals > self.max_cards:
            self.max_bs -= totals - self.max_cards

    def getMaxCards(self):
        maxs = [self.max_cards, self.max_urs, self.max_mrs, self.max_rs, self.max_ns, self.max_bs]
        return maxs
    
    def createDeck(self, player, name, cards):
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