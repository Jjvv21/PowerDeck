from datetime import date

class Card:
    name = ""
    description = ""
    isMain = True
    variant_name = ""
    creation_date = None
    last_modification = None
    race = ""
    rarity = ""
    image = ""
    active_in_game = True
    active_in_pulls = True
    turn_power = 0
    bonus_power = 0
    stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_power = 0
    ID = 0

    def __init__(self, name, desc, var, isMain, race, rarity, image, turn_power, bonus_power):
        self.name = name
        self.description = desc
        self.isMain = isMain
        self.variant_name = var
        self.creation_date = date.today()
        self.last_modification = self.creation_date
        self.race = race
        self.rarity = rarity
        self.image = image
        self.turn_power = turn_power
        self.bonus_power = bonus_power

    def setStats(self, stats):
        if len(stats) == 26:
            self.stats = stats
            for i in range(0, 25):
                self.total_power += self.stats[i]
            self.last_modification = date.today()
            
    def getName(self):
        return self.name