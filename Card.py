from datetime import date
import uuid

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
    nameID = ""
    varID = ""

    def __init__(self, name, desc, var, main, race, rarity, image, turn_power, bonus_power, nameID):
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
        generated = uuid.uuid4().hex
        if nameID == "":
            self.nameID = "C-" + generated[12: 24]
        else:
            self.nameID = nameID
        self.varID = "V-" + generated[0: 12]

    def setStats(self, stats):
        if len(stats) == 26:
            self.stats = stats
            for i in range(0, 25):
                self.total_power += self.stats[i]
            self.last_modification = date.today()
            
    def getName(self):
        return self.name
    
    def getVarName(self):
        return self.variant_name
    
    def getRace(self):
        return self.race
    
    def getRarity(self):
        return self.rarity
    
    def gameActive(self):
        return self.game_active
    
    def pullActive(self):
        return self.pull_active
    
    def getID(self):
        return self.nameID + "-" + self.varID
    
    def lastMod(self):
        return self.last_modification
    
    def getImage(self):
        return self.image
    
    def isMain(self):
        return self.main