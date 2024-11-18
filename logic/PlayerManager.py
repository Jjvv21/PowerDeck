import random

from logic.UserManager import *
from logic.Player import *
from logic.CardAlbum import *
from logic.DeckBuilder import *
from logic.PlayerError import *

class PlayerManager(UserManager):
    album = CardAlbum()
    max_starting_cards = 20

    def __init__(self):
        """
        Constructor that intializes the player manager by opening the file and trying to add the players in the
        file to its list.
        """
        UserManager.__init__(self, "gamedata/player_accounts.txt")
        with open(self.getSaveFile(), "rb") as file:
            try:
                self.setData(pickle.load(file))
            except:
                print("no player accounts found")

    def add(self, player_info, admin_manager):
        """
        add receives a list with the player info, checks if the values are valid, returning with
        a diferent negative number when it finds an error, if all data is acceptable creates.

        :player_info: list with the player's name, username, password, mail, country and image.
        :return: Negative number corresponding to an error, index of the created player otherwise.
        """
        name = player_info[0]
        username = player_info[1]
        password = player_info[2]
        mail = player_info[3]
        country = player_info[4]
        image = player_info[5]
        if len(name) < 5:
            return PlayerError.NAME_LENGTH.value
        
        if len(username) < 5:
            return PlayerError.USERNAME_LENGTH.value
        
        if mail == "":
            return PlayerError.NO_MAIL.value
        
        players = self.getData()
        if len(players) > 0:
            for i in players:
                if i.getUser() == username:
                    return PlayerError.USERNAME_TAKEN.value
                if i.getMail() == mail:
                    return PlayerError.USED_MAIL.value
                
        admins = admin_manager.getData()
        if len(admins) > 0:
            for j in admins:
                if j.getMail() == mail:
                    return PlayerError.USED_MAIL.value
        
        if len(password) < 6:
            return PlayerError.PASSWORD_LENGTH.value

        if not self.checkPassword(password):
            return PlayerError.INVALID_PASSWORD.value     
        
        if country == "":
            return PlayerError.NO_COUNTRY.value
        
        newPlayer = Player()
        newPlayer.setName(name)
        newPlayer.setUser(username)
        newPlayer.setPassword(password)
        newPlayer.setMail(mail)
        newPlayer.setCountry(country)
        newPlayer.setAvatar(image)
        self.startingCards(newPlayer)
        self.addData(newPlayer)
        return len(players)
    
    def startingCards(self, player):
        """
        startingCards gets all the game cards on a list to shuffle it, then takes all main, active cards
        and sets them in different list depending on their rarity, then gets the maximun cards for one
        deck and the quantities of different rarities allowed on a deck, using this data gives the player
        the required cards to create a deck.

        :player: player that is receiving the cards.
        """
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

        starting_cards = []
        while len(starting_cards) < self.max_starting_cards:
            rng = random.randint(1, 100)
            if rng <= 5:
                starting_cards.append(URs.pop(0))
            elif rng <= 17:
                starting_cards.append(MRs.pop(0))
            elif rng <= 35:
                starting_cards.append(Rs.pop(0))
            elif rng <= 60:
                starting_cards.append(Ns.pop(0))
            else:
                starting_cards.append(Bs.pop(0))

        for j in starting_cards:
            player.receiveCard(j, self.album)

    def getPlayer(self, index):
        """
        getPlayer receives a string with a mail, checks if the mail corresponds to any mail
        in the saved players.

        :index: index where the desired player is.
        :return: player at the given index.
        """
        players = self.getData()
        return players[index]
        