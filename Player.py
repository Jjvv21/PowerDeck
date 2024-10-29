from datetime import date
from KeyGeneration import generateKey

class Player:
    name = ""
    username = ""
    password = ""
    mail = ""
    country = ""
    avatar = ""
    registration_date = ""
    player_id = ""
    username_id = ""
    exp = 0
    owned_cards = []
    decks = []

    def __init__(self):
        self.registration_date = date.today()
        self.player_id = "J-" + generateKey() 
        self.username_id = "A-" + generateKey()

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setUser(self, username):
        self.username = username

    def getUser(self):
        return self.username
    
    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password
    
    def setMail(self, mail):
        self.mail = mail

    def getMail(self):
        return self.mail

    def setCountry(self, country):
        self.country = country

    def getCountry(self):
        return self.country
    
    def setAvatar(self, image):
        self.avatar = image

    def getCountry(self):
        return self.avatar
    