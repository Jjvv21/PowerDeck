from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import shutil

from functions import loadImage
from Card import *

class AddWindow:
    img = "noImg.jpg"
    path = ""
    savePath = os.getcwd() + os.sep + "img"
    races = ["Raza1", "Raza2", "Raza3", "Raza4", "Raza5"]
    rarities = ["Ultra-Rara", "Muy Rara", "Rara", "Normal", "Básica"]

    def __init__(self, window, caller):
        self.caller = caller
        self.window = window
        self.canvas = Canvas(self.window, width = 800, height = 600)
        self.canvas.pack()

        self.canvas.create_text(200, 5, anchor = NW, text = "Crear Carta")
        
        self.canvas.create_text(10, 50, anchor = NW, text = "Nombre: ")
        self.NameEntry = Entry(self.canvas, width = 30)
        self.NameEntry.place(x = 60, y = 50)   
        self.NameEntry.bind('<KeyPress>', self.nameCharCount)
        self.NameEntry.bind('<KeyRelease>', self.nameCharCount)     

        self.canvas.create_text(10, 70, anchor = NW, text = "Variante: ")
        self.VarEntry = Entry(self.canvas, width = 30)
        self.VarEntry.place(x = 60, y = 70)
        self.VarEntry.bind('<KeyPress>', self.varCharCount)
        self.VarEntry.bind('<KeyRelease>', self.varCharCount) 

        self.isVar = BooleanVar(self.canvas)
        self.VarCheck = ttk.Checkbutton(self.canvas, text= "Variante", variable = self.isVar)
        self.VarCheck.place(x = 160, y = 90)

        self.canvas.create_text(10, 90, anchor = NW, text = "Raza: ")
        self.race = ttk.Combobox(self.canvas, state = "readonly", values = self.races, width = 10)
        self.race.place(x = 60, y = 90)

        self.canvas.create_text(10, 110, anchor = NW, text = "Rareza: ")
        self.rarity = ttk.Combobox(self.canvas, state = "readonly", values = self.rarities, width = 10)
        self.rarity.place(x = 60, y = 110)

        self.canvas.create_text(250, 50, anchor = NW, text = "Descripción: ")
        self.DescText = Text(self.canvas, width = 50, height = 5)
        self.DescText.place(x = 320, y = 50)
        self.DescText.bind('<KeyPress>', self.descCharCount)
        self.DescText.bind('<KeyRelease>', self.descCharCount)
        self.scroll = Scrollbar(self.canvas)
        self.scroll.place(height = 5, x = 750, y = 50)
        self.scroll.config(command = self.DescText.yview)

        vcmd = (self.window.register(self.checkNum), '%P')
        self.canvas.create_text(10, 150, anchor = NW, text = "Poder: ")
        self.PwrEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.PwrEntry.place(x = 90, y = 150)        

        self.canvas.create_text(10, 170, anchor = NW, text = "Velocidad: ", fill = "#000000")
        self.SpdEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.SpdEntry.place(x = 90, y = 170)

        self.canvas.create_text(10, 190, anchor = NW, text = "Magia: ", fill = "#000000")
        self.MgcEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.MgcEntry.place(x = 90, y = 190)

        self.canvas.create_text(10, 210, anchor = NW, text = "Defensa: ", fill = "#000000")
        self.DefEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.DefEntry.place(x = 90, y = 210)

        self.canvas.create_text(10, 230, anchor = NW, text = "Inteligencia: ", fill = "#000000")
        self.SpdEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.SpdEntry.place(x = 90, y = 230)

        self.canvas.create_text(10, 250, anchor = NW, text = "Altura: ", fill = "#000000")
        self.HeightEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.HeightEntry.place(x = 90, y = 250)

        self.canvas.create_text(10, 270, anchor = NW, text = "Fuerza: ", fill = "#000000")
        self.StrEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.StrEntry.place(x = 90, y = 270)

        self.canvas.create_text(10, 290, anchor = NW, text = "Agilidad: ", fill = "#000000")
        self.AglEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.AglEntry.place(x = 90, y = 290)

        self.canvas.create_text(10, 310, anchor = NW, text = "Salto: ", fill = "#000000")
        self.JmpEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.JmpEntry.place(x = 90, y = 310)

        self.canvas.create_text(130, 150, anchor = NW, text = "Resistencia: ", fill = "#000000")
        self.ResEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.ResEntry.place(x = 210, y = 150)        

        self.canvas.create_text(130, 170, anchor = NW, text = "Flexibilidad: ", fill = "#000000")
        self.FlxEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.FlxEntry.place(x = 210, y = 170)

        self.canvas.create_text(130, 190, anchor = NW, text = "Explosividad: ", fill = "#000000")
        self.ExplEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.ExplEntry.place(x = 210, y = 190)

        self.canvas.create_text(130, 210, anchor = NW, text = "Carisma: ", fill = "#000000")
        self.ChrsEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.ChrsEntry.place(x = 210, y = 210)

        self.canvas.create_text(130, 230, anchor = NW, text = "Habilidad: ", fill = "#000000")
        self.AblEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.AblEntry.place(x = 210, y = 230)

        self.canvas.create_text(130, 250, anchor = NW, text = "Balance: ", fill = "#000000")
        self.BlcEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.BlcEntry.place(x = 210, y = 250)

        self.canvas.create_text(130, 270, anchor = NW, text = "Sabiduría: ", fill = "#000000")
        self.WsdEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.WsdEntry.place(x = 210, y = 270)

        self.canvas.create_text(130, 290, anchor = NW, text = "Suerte: ", fill = "#000000")
        self.LckEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.LckEntry.place(x = 210, y = 290)

        self.canvas.create_text(130, 310, anchor = NW, text = "Coordinación: ", fill = "#000000")
        self.CordEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.CordEntry.place(x = 210, y = 310)

        self.canvas.create_text(250, 150, anchor = NW, text = "Amabilidad: ", fill = "#000000")
        self.ResEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.ResEntry.place(x = 330, y = 150)        

        self.canvas.create_text(250, 170, anchor = NW, text = "Lealtad: ", fill = "#000000")
        self.FlxEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.FlxEntry.place(x = 330, y = 170)

        self.canvas.create_text(250, 190, anchor = NW, text = "Disciplina: ", fill = "#000000")
        self.ExplEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.ExplEntry.place(x = 330, y = 190)

        self.canvas.create_text(250, 210, anchor = NW, text = "Liderazgo: ", fill = "#000000")
        self.ChrsEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.ChrsEntry.place(x = 330, y = 210)

        self.canvas.create_text(250, 230, anchor = NW, text = "Prudencia: ", fill = "#000000")
        self.AblEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.AblEntry.place(x = 330, y = 230)

        self.canvas.create_text(250, 250, anchor = NW, text = "Confianza: ", fill = "#000000")
        self.BlcEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.BlcEntry.place(x = 330, y = 250)

        self.canvas.create_text(250, 270, anchor = NW, text = "Percepción: ", fill = "#000000")
        self.WsdEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.WsdEntry.place(x = 330, y = 270)

        self.canvas.create_text(250, 290, anchor = NW, text = "Valentía: ", fill = "#000000")
        self.LckEntry = Entry(self.canvas, width = 4, validate="key", validatecommand=vcmd)
        self.LckEntry.place(x = 330, y = 290)

        self.selectedImg = loadImage("noImage.jpg")
        self.canvas.create_image(450, 180, anchor = NW, image = self.selectedImg, tags = "selection")

        self.SelectImgButton = Button(self.canvas, text = "Seleccionar Imagen", command = self.getImage)
        self.SelectImgButton.place(x = 500, y = 150)

        self.AddButton = Button(self.canvas, text = "Agregar Carta", command = self.addCard)
        self.AddButton.place(x = 70, y = 380)

        
        self.BackButton = Button(self.canvas, text = "Atrás", command = self.back)
        self.BackButton.place(x = 760, y = 500)

    def run(self):
        self.window.mainloop()

    def nameCharCount(self, event):
        count = len(self.NameEntry.get())
        if count >= 30 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'
        
    def varCharCount(self, event):
        count = len(self.VarEntry.get())
        if count >= 5 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'

    def descCharCount(self, event):
        count = len(self.DescText.get('1.0', 'end-1c'))
        if count >= 1000 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'
        
    def checkNum(self, P):
        if P == "":
            return True
        elif len(P) == 1:
            if str.isdigit(P) or P == "-":
                return True
            else:
                return False
        elif len(P) <= 4:
            if str.isdigit(P[1:]):
                return True
            else:
                return False
        else:
            return False

    def getImage(self):
        self.path = filedialog.askopenfilename()
        if self.path[-4:].lower() == ".png" or self.path[-4:].lower() == ".jpg":
            i = -1
            while self.path[i] != "/":
                i -= 1
            self.img = self.path[i + 1:]
            img = Image.open(self.path)
            if img.size[0] != 215 or img.size[1] != 330:
                self.path = ""
                self.img = "noImg.jpg"
                messagebox.showerror("Error", "Tamaño de imagen incorrecto")
            else:
                messagebox.showinfo("Éxito", "Imagen cargada")
                self.selectedImg = loadImage(img)
                self.canvas.itemconfig("selection", image = self.selectedImg)
        else:
            self.path = ""
            messagebox.showerror("Error", "Seleccione una imagen (png o jpg)")

    def addCard(self):
        name = self.NameEntry.get()
        var = self.VarEntry.get()
        if len(name) < 5:
            messagebox.showerror("Error", "El nombre de la carta debe tener entre 5 y 30 caracteres")
        elif len(var) < 5:
            messagebox.showerror("Error", "El nombre de variante de la carta debe tener entre 5 y 30 caracteres")
        else:
            self.caller.cards.append(Card(name, self.img))
            self.NameEntry.delete(0, END)
            if self.img != "noImage.jpg":
                shutil.copy(self.path, self.savePath)
                self.img = "noImage.jpg"
                self.path = ""
            self.listbox.insert(END, name)
            messagebox.showinfo("Éxito", f"Carta {name} agregada")

    def back(self):
        self.window.destroy()
        self.caller.saveCards()
        self.caller.window.deiconify()