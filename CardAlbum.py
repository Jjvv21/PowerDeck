import pickle

from Card import *

class CardAlbum:
    cards = []
    save_file = "gamedata\cards.txt"

    def __init__(self):
        """
        Constructor that intializes the card album by opening the file and trying to add the cards in the
        file to its list.
        """
        file = open(self.save_file, "rb")
        try:
            self.cards.extend(pickle.load(file))
        except:
            print("no cards found")
        finally:
            file.close()

    def save(self):
        """
        save saves the cards in the album list to the file.
        """
        file = open(self.save_file, "wb")
        pickle.dump(self.cards, file)
        file.close()

    def add(self, card_info, stats_strs):
        """
        add receives two lists with the card info and card stats, checks if the values are valid,
        returning with a diferent number when it finds an error, if all data is acceptable creates 
        the new card and adds it to the list, which is sorted and saved.

        :card_info: list with name, description, variant name, race, rarity, image, turn power and bonus power.
        :stats_str: list with a string for every stat.        
        :return: Number corresponding to the result of the creation.
        """
        name = card_info[0]
        desc = card_info[1]
        var = card_info[2]
        race = card_info[3]
        rarity = card_info[4]
        image = card_info[5]
        turn_power_str = card_info[6]
        bonus_power_str = card_info[7]
        
        if len(name) < 5:
            return -1
        
        if len(var) < 5:
            return -2
        
        nameID = ""
        if len(self.cards) > 0:
            for i in self.cards:
                if i.getName() == name:
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
        
        newCard = Card(nameID)
        newCard.setName(name)
        newCard.setDescription(desc)
        newCard.setVariantName(var)
        newCard.setRace(race)
        newCard.setRarity(rarity)
        newCard.setImage(image)
        newCard.setTurnPower(turn_power)
        newCard.setBonusPower(bonus_power)
        newCard.setStats(stats)
        self.cards.append(newCard)
        self.sort()
        if name == "":
            return 0
        else:
            return 1

    def sort(self):
        """
        sorts adds all cards names in lowercase to a list to use python's sort, 
        then checks the name of the cards to place them in the order obtained with 
        the sort and updates the album list.
        """
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
        