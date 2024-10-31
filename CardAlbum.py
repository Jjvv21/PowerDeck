import pickle

from Card import *

class CardAlbum:
    cards = []
    save_file = "gamedata\cards.txt"

    def __init__(self):
        file = open(self.save_file, "rb")
        try:
            self.cards.extend(pickle.load(file))
            file.close()
        except:
            print("no cards found")
            file.close()

    def save(self):
        file = open(self.save_file, "wb")
        pickle.dump(self.cards, file)
        file.close()

    def add(self, name, desc, var, race, rarity, image, turn_power_str, bonus_power_str, stats_strs):
        if len(name) < 5:
            return -1
        
        if len(var) < 5:
            return -2
        
        nameID = ""
        isVar = False
        if len(self.cards) > 0:
            for i in self.cards:
                if i.getName() == name:
                    isVar = True
                    nameID = i.getID()[0: 14]
                    if i.getVariantName() == var:
                        return -3
        
        if image == "noImage.jpg":
            return -4
        
        if race == "":
            return -5
        
        if rarity == "":
            return -6
        
        if turn_power_str == "":
            return -7
        turn_power = int(turn_power_str)
        if turn_power > 100:
            return -8
        
        if bonus_power_str == "":
            return -9
        bonus_power = int(bonus_power_str)
        if bonus_power > 100:
            return -10

        stats = []
        i = 0
        while i < 26:
            stat_str = stats_strs[i]
            if stat_str == "-" or stat_str == "":
                break
            stat = int(stat_str)
            if abs(stat) > 100:
                i += 26
                break
            stats.append(stat)
            i += 1
        if len(stats) < 26:
            return -11 - i
        
        newCard = Card(name, desc, var, not isVar, race, rarity, image, turn_power, bonus_power, nameID)
        newCard.setStats(stats)
        self.cards.append(newCard)
        self.sort()
        if not isVar:
            return 0
        else:
            return 1

    def sort(self):
        order = []
        for i in self.cards:
            name = i.getName().lower()
            var = i.getVariantName().lower()
            order.append(name + var)
        order.sort()

        sorted_cards = []
        for j in range(0, len(order)):
            for k in self.cards:
                name = k.getName().lower()
                var = k.getVariantName().lower()
                if (name + var) == order[j]:
                    sorted_cards.append(k)

        self.cards = sorted_cards
        self.save()

    def getCards(self):
        return self.cards
        