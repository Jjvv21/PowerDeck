from datetime import date

class Card:
    name = ""
    description = ""
    variant_name = ""
    main = True
    creation_date = None
    last_modification = None
    race = ""
    rarity = ""
    image = ""
    active_in_game = True
    active_in_pulls = True
    turn_power = 0
    power_bonus = 0
    attributes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ID = 0

    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.creation_date = date.today()
        self.last_modification = self.creation_date
