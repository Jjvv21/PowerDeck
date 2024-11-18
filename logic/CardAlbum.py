from logic.Manager import *

from logic.Card import *
from logic.CardResult import *

class CardAlbum(Manager):

    def __init__(self):
        """
        Constructor that intializes the card album by opening the file and trying to add the cards in the
        file to its list.
        """
        Manager.__init__(self, "gamedata/cards.txt")
        with open(self.getSaveFile(), "rb") as file:
            try:
                self.setData(pickle.load(file))
            except:
                print("no cards found")

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
            return CardResult.NAME_LENGTH.value
        
        if len(var) < 5:
            return CardResult.VARIANT_NAME_LENGTH.value
        
        cards = self.getData()
        nameID = ""
        if len(cards) > 0:
            for i in cards:
                if i.getName() == name:
                    nameID = i.getID()[0: 14]
                    if i.getVariantName() == var:
                        return CardResult.DUPLICATE.value
        
        if image == "noImage.jpg":
            return CardResult.NO_IMAGE.value
        
        if race == "":
            return CardResult.NO_RACE.value
        
        if rarity == "":
            return CardResult.NO_RARITY.value
        
        if turn_power_str == "":
            return CardResult.INVALID_TURN_POWER.value
        turn_power = int(turn_power_str)
        if turn_power > 100:
            return CardResult.INVALID_TURN_POWER.value
        
        if bonus_power_str == "":
            return CardResult.INVALID_BONUS_POWER.value
        bonus_power = int(bonus_power_str)
        if bonus_power > 100:
            return CardResult.INVALID_BONUS_POWER.value

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
            return CardResult.INVALID_STAT.value
        
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
        self.addData(newCard)
        self.setData(self.sort(self.getData()))
        self.save()
        if nameID == "":
            return CardResult.CREATED_MAIN.value
        else:
            return CardResult.CREATED_VARIANT.value

    def sort(self, cards):
        """
        sorts adds all cards names in lowercase to a list to use python's sort, 
        then checks the name of the cards to place them in the order obtained with 
        the sort and updates the album list.

        :cards: list with the cards to sorted.        
        :return: list with the sorted cards.
        """
        order = []
        for i in cards:
            name = i.getName().lower()
            var = i.getVariantName().lower()
            order.append(name + var)
        order.sort()
    	
        sorted_cards = []
        for j in range(0, len(order)):
            for k in cards:
                name = k.getName().lower()
                var = k.getVariantName().lower()
                if (name + var) == order[j]:
                    sorted_cards.append(k)

        return sorted_cards

    def getCards(self):
        return self.getData()
        