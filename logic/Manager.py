import pickle

class Manager:
    data = []
    save_file = ""

    def __init__(self, save_file):
        """
        Constructor that intializes the manager by setting the save file.

        :save_file: path to the save file.
        """
        self.save_file = save_file

    def save(self):
        """
        save saves the data list in the file.
        """
        with open(self.save_file, "wb") as file:
            pickle.dump(self.data, file)

    def getSaveFile(self):
        return self.save_file

    def addData(self, data):
        self.data.append(data)

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data