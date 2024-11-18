from logic.UserManager import *
from logic.Admin import *
from logic.AdminError import *

class AdminManager(UserManager):

    def __init__(self):
        """
        Constructor that intializes the player manager by opening the file and trying to add the players in the
        file to its list.
        """
        UserManager.__init__(self, "gamedata/admin_accounts.txt")
        with open(self.getSaveFile(), "rb") as file:
            try:
                self.setData(pickle.load(file))
            except:
                print("no admin accounts found")

    def add(self, admin_info, player_manager):
        """
        add receives a list with the admin info, checks if the values are valid, returning with
        a diferent negative number when it finds an error, if all data is acceptable creates.

        :admin_info: list with the admin's name, password, mail and role.
        :return: Negative number corresponding to an error, index of the created player otherwise.
        """
        name = admin_info[0]
        mail = admin_info[1]
        password = admin_info[2]
        role = admin_info[3]

        if len(name) < 5:
            return AdminError.NAME_LENGTH.value
        
        if mail == "":
            return AdminError.NO_MAIL.value
        
        admins = self.getData()
        if len(admins) > 0:
            for i in admins:
                if i.getMail() == mail:
                    return AdminError.USED_MAIL.value
        
        players = player_manager.getData()
        if len(players) > 0:
            for j in players:
                if j.getMail() == mail:
                    return AdminError.USED_MAIL.value
                
        if len(password) < 6:
            return AdminError.PASSWORD_LENGTH.value

        if not self.checkPassword(password):
            return AdminError.INVALID_PASSWORD.value     
        
        if role == "":
            return AdminError.NO_ROLE.value
        
        newAdmin = Admin()
        newAdmin.setName(name)
        newAdmin.setPassword(password)
        newAdmin.setMail(mail)
        newAdmin.setRole(role)
        self.addData(newAdmin)
        return len(admins) - 1
    
    def getAdmin(self, index):
        """
        getPlayer receives a string with a mail, checks if the mail corresponds to any mail
        in the saved players.

        :index: index where the desired player is.
        :return: player at the given index.
        """
        admins = self.getData()
        return admins[index]