import os
from PIL import Image, ImageTk

def loadImage(name):
    path = os.path.join("img", name)
    image = Image.open(path)
    return ImageTk.PhotoImage(image)