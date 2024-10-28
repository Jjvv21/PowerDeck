import pickle

from Player import *

class PlayerManager:
    players = []
    save_file = "player_accounts.txt"

    def load(self):
        file = open(self.save_file, "rb")
        self.players.extend(pickle.load(file))
        file.close()

    def save(self):
        file = open(self.save_file, "wb")
        pickle.dump(self.cards, file)
        file.close()

    def add(self, name, username, password, mail, country, image):
        if len(name) < 5:
            return -1
        
        if len(username) < 5:
            return -2
        
        if len(self.players) > 0:
            for i in self.players:
                if i.getUser() == username:
                    return -3
        
        if password == "":
            return -4
        
        if mail == "":
            return -5
        
        if country == "":
            return -5
        
        newPlayer = Player()
        newPlayer.setName(name)
        newPlayer.setUser(username)
        newPlayer.setPassword(password)
        newPlayer.setMail(mail)
        newPlayer.setCountry(country)
        self.players.append(newPlayer)
        return 0
    
    def exists(self, mail):
        for i in range(0, len(self.players)):
            if self.players[i].getMail() == mail:
                return i
        return -1

    def getPlayer(self, index):
        return self.players[index]
        