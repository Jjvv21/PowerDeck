import pickle, random

from Player import *
from CardAlbum import *
from DeckBuilder import *

class PlayerManager:
    players = []
    save_file = "gamedata\player_accounts.txt"
    album = CardAlbum()

    def __init__(self):
        file = open(self.save_file, "rb")
        try:
            self.players.extend(pickle.load(file))
            file.close()
        except:
            print("no player accounts found")
            file.close()

    def save(self):
        file = open(self.save_file, "wb")
        pickle.dump(self.players, file)
        file.close()

    def add(self, name, username, password, mail, country, image):
        if len(name) < 5:
            return -1
        
        if len(username) < 5:
            return -2
        
        if mail == "":
            return -3
        
        if len(self.players) > 0:
            for i in self.players:
                if i.getUser() == username:
                    return -4
                if i.getMail() == mail:
                    return -5
        
        if len(password) < 6:
            return -6

        if not self.checkPassword(password):
            return -7        
        
        if country == "":
            return -8
        
        newPlayer = Player()
        newPlayer.setName(name)
        newPlayer.setUser(username)
        newPlayer.setPassword(password)
        newPlayer.setMail(mail)
        newPlayer.setCountry(country)
        newPlayer.setAvatar(image)
        self.startingCards(newPlayer)
        self.players.append(newPlayer)
        return len(self.players) - 1
    
    def checkPassword(self, password):
        alpha = False
        num = False
        for char in password:
            if str.isalpha(char):
                alpha = True
            elif str.isnumeric(char):
                num = True
            if alpha and num:
                break
        return alpha and num
    
    def startingCards(self, player):
        cards = self.album.getCards()
        random.shuffle(cards)
        URs = []
        MRs = []
        Rs = []
        Ns = []
        Bs = []
        for i in cards:
            if i.isMain() and i.gameActive() and i.pullActive():
                rarity = i.getRarity()
                match rarity:
                    case "Ultra-Rara":
                        URs.append(i)
                    case "Muy Rara":
                        MRs.append(i)
                    case "Rara":
                        Rs.append(i)
                    case "Normal":
                        Ns.append(i)
                    case "Básica":
                        Bs.append(i)
        
        deck_builder = DeckBuilder()
        max_cards = deck_builder.getMaxCards()
        for j in range(0, max_cards):
            rng = random.randint(1, 100)
            if rng <= 5:
                player.receiveCard(URs.pop(0))
            elif rng <= 17:
                player.receiveCard(MRs.pop(0))
            elif rng <= 35:
                player.receiveCard(Rs.pop(0))
            elif rng <= 60:
                player.receiveCard(Ns.pop(0))
            else:
                player.receiveCard(Bs.pop(0))
    
    def exists(self, mail):
        for i in range(0, len(self.players)):
            if self.players[i].getMail() == mail:
                return i
        return -1

    def getPlayer(self, index):
        return self.players[index]
        