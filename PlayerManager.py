import pickle, random

from Player import *
from CardAlbum import *
from DeckBuilder import *

class PlayerManager:
    players = []
    save_file = "gamedata\player_accounts.txt"
    album = CardAlbum()

    def __init__(self):
        """
        Constructor that intializes the player manager by opening the file and trying to add the players in the
        file to its list.
        """
        file = open(self.save_file, "rb")
        try:
            self.players.extend(pickle.load(file))
        except:
            print("no player accounts found")
        finally:
            file.close()

    def save(self):
        """
        save saves the player list in the file.
        """
        file = open(self.save_file, "wb")
        pickle.dump(self.players, file)
        file.close()

    def add(self, name, username, password, mail, country, image):
        """
        add receives a list with the player info, checks if the values are valid, returning with
        a diferent negative number when it finds an error, if all data is acceptable creates.

        :return: Negative number corresponding to an error, index of the created player otherwise.
        """
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
        """
        checkPassword receives a string with a password, checks every character in the password
        to verify that theres is at least one alphabetic character and one numeric character 
        the new player and adds it to the list, then returns the index for the created player.

        :return: True if there are both alphabetic and numeric charaters, False otherwise.
        """
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
        maxs = deck_builder.getMaxCards()
        max_cards = maxs[0]
        max_urs = maxs[1]
        max_mrs = maxs[2]
        max_rs = maxs[3]
        max_ns = maxs[4]
        max_bs = maxs[5]

        cards_to_give = []
        urs = 0
        mrs = 0
        rs = 0
        ns = 0
        bs = 0
        min_index = 1
        max_index = 100
        while len(cards_to_give) < max_cards:
            rng = random.randint(min_index, max_index)
            if rng <= 5 and urs < max_urs:
                cards_to_give.append(URs.pop(0))
                urs += 1
            elif rng <= 17 and mrs < max_mrs:
                cards_to_give.append(MRs.pop(0))
                mrs += 1
            elif rng <= 35 and rs < max_rs:
                cards_to_give.append(Rs.pop(0))
                rs += 1
            elif rng <= 60 and ns < max_ns:
                    cards_to_give.append(Ns.pop(0))
                    ns += 1
            else:
                if bs < max_bs:
                    cards_to_give.append(Bs.pop(0))
                    bs += 1

        for j in cards_to_give:
            player.receiveCard(j)
    
    def exists(self, mail):
        for i in range(0, len(self.players)):
            if self.players[i].getMail() == mail:
                return i
        return -1

    def getPlayer(self, index):
        return self.players[index]
        