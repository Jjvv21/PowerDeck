from logic.Manager import *

class UserManager(Manager):

    def __init__(self, save_file):
        """
        Constructor that intializes the user manager by setting the save file.

        :save_file: path to the save file.
        """
        Manager.__init__(self, save_file)

    def checkPassword(self, password):
        """
        checkPassword checks every character in a password to verify that there is at least 
        one alphabetic character and one numeric character the new user and adds it to the list,
        then returns the index for the created user.
        
        :password: string with the password to check.
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
    
    def exists(self, mail):
        """
        exists checks if a given mail corresponds to any mail
        in the saved users.

        :mail: string with the mail to search.
        :return: -1 if the mail is not found, index for the location of the player otherwise.
        """
        users = self.getData()
        for i in range(0, len(users)):
            if users[i].getMail() == mail:
                return i
        return -1