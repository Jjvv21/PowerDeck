from datetime import date
from KeyGeneration import generateKey

class Card:
    name = ""
    description = ""
    main = True
    variant_name = ""
    creation_date = None
    last_modification = None
    race = ""
    rarity = ""
    image = ""
    game_active = True
    pull_active = True
    turn_power = 0
    bonus_power = 0
    stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    total_power = 0
    name_id = ""
    var_id = ""

    def __init__(self, name, desc, var, main, race, rarity, image, turn_power, bonus_power, name_id):
        self.name = name
        self.description = desc
        self.main = main
        self.variant_name = var
        self.creation_date = date.today()
        self.last_modification = self.creation_date
        self.race = race
        self.rarity = rarity
        self.image = image
        self.turn_power = turn_power
        self.bonus_power = bonus_power
        if name_id == "":
            self.name_id = "C-" + generateKey()
        else:
            self.name_id = name_id
        self.var_id = "V-" + generateKey()

    def setStats(self, stats):
        if len(stats) == 26:
            self.stats = stats
            for i in range(0, 25):
                self.total_power += self.stats[i]
            self.last_modification = date.today()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setVariantName(self, variant_name):
        self.variant_name = variant_name

    def getVariantName(self):
        return self.variant_name

    def setRace(self, race):
        self.race = race

    def getRace(self):
        return self.race

    def setRarity(self, rarity):
        self.race = rarity

    def getRarity(self):
        return self.rarity
    
    def gameActive(self):
        return self.game_active
    
    def pullActive(self):
        return self.pull_active
    
    def getID(self):
        return self.name_id + "-" + self.var_id
    
    def lastMod(self):
        return self.last_modification
    
    def getImage(self):
        return self.image
    
    def isMain(self):
        return self.main