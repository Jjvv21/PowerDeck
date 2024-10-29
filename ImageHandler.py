import os, shutil
from PIL import Image, ImageTk

class ImageHandler:
    folder_name = "img"
    save_path = os.getcwd() + os.sep + folder_name
    
    def loadImage(self, name):
        """
        loadImage loads an image to show in the UI.

        :name: name of an image already in the program file.
        :return: image to show.
        """
        path = os.path.join(self.folder_name, name)
        image = Image.open(path)
        return ImageTk.PhotoImage(image)

    def checkImage(self, path):
        """
        checkImage checks if a path to a selected file is a jpg or png.

        :path: path to an image anywhere in the computer.
        :return: image to show.
        """
        if path == "":
            return -1
        
        if not (path[-4:].lower() == ".png" or path[-4:].lower() == ".jpg"):
            return -2
        
        img = Image.open(path)
        if img.size[0] != 215 or img.size[1] != 330:
            return -3
        
        i = -1
        while path[i] != "/":
            i -= 1
        i += 1
        return abs(i)
    
    def loadExternalImage(self, path):
        """
        loadExternalImage loads an image to show in the UI.

        :path: path to an image anywhere in the computer.
        :return: image to show.
        """
        image = Image.open(path)
        return ImageTk.PhotoImage(image)
    
    def saveImage(self, path):
        """
        saveImage saves an image in the folder for the program.

        :path: path to an image anywhere in the computer.
        """
        shutil.copy(path, self.save_path)
