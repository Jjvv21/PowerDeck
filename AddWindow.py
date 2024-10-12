from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os, shutil

from functions import loadImage
from Card import *

class AddWindow:
    img = "noImage.jpg"
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
        self.scroll.place(height = 10, x = 750, y = 50)
        self.scroll.config(command = self.DescText.yview)

        self.placeStatEntries(10, 150)

        self.selectedImg = loadImage("noImage.jpg")
        self.canvas.create_image(450, 180, anchor = NW, image = self.selectedImg, tags = "selection")

        self.SelectImgButton = Button(self.canvas, text = "Seleccionar Imagen", command = self.getImage)
        self.SelectImgButton.place(x = 500, y = 150)

        self.AddButton = Button(self.canvas, text = "Agregar Carta", command = self.addCard)
        self.AddButton.place(x = 70, y = 380)

        
        self.BackButton = Button(self.canvas, text = "Atrás", command = self.back)
        self.BackButton.place(x = 760, y = 500)

    def placeStatEntries(self, posX, posY):
        vcmd = (self.window.register(self.checkNum), '%P')
        self.canvas.create_text(posX, posY, anchor = NW, text = "Poder: ")
        self.PowerEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.PowerEntry.place(x = posX + 80, y = posY)        

        self.canvas.create_text(posX, posY + 20, anchor = NW, text = "Velocidad: ")
        self.SpeedEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.SpeedEntry.place(x = posX + 80, y = posY + 20)

        self.canvas.create_text(posX, posY + 40, anchor = NW, text = "Magia: ")
        self.MagicEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.MagicEntry.place(x = posX + 80, y = posY + 40)

        self.canvas.create_text(posX, posY + 60, anchor = NW, text = "Defensa: ")
        self.DefEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.DefEntry.place(x = posX + 80, y = posY + 60)

        self.canvas.create_text(posX, posY + 80, anchor = NW, text = "Inteligencia: ")
        self.IntEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.IntEntry.place(x = posX + 80, y = posY + 80)

        self.canvas.create_text(posX, posY + 100, anchor = NW, text = "Altura: ")
        self.HeightEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.HeightEntry.place(x = posX + 80, y = posY + 100)

        self.canvas.create_text(posX, posY + 120, anchor = NW, text = "Fuerza: ")
        self.StrEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.StrEntry.place(x = posX + 80, y = posY + 120)

        self.canvas.create_text(posX, posY + 140, anchor = NW, text = "Agilidad: ")
        self.AglEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.AglEntry.place(x = posX + 80, y = posY + 140)

        self.canvas.create_text(posX, posY + 160, anchor = NW, text = "Salto: ")
        self.JumpEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.JumpEntry.place(x = posX + 80, y = posY + 160)

        self.canvas.create_text(posX + 120, posY, anchor = NW, text = "Resistencia: ")
        self.ResEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.ResEntry.place(x = posX + 200, y = posY)        

        self.canvas.create_text(posX + 120, posY + 20, anchor = NW, text = "Flexibilidad: ")
        self.FlexEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.FlexEntry.place(x = posX + 200, y = posY + 20)

        self.canvas.create_text(posX + 120, posY + 40, anchor = NW, text = "Explosividad: ")
        self.ExplEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.ExplEntry.place(x = posX + 200, y = posY + 40)

        self.canvas.create_text(posX + 120, posY + 60, anchor = NW, text = "Carisma: ")
        self.ChrsEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.ChrsEntry.place(x = posX + 200, y = posY + 60)

        self.canvas.create_text(posX + 120, posY + 80, anchor = NW, text = "Habilidad: ")
        self.AblEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.AblEntry.place(x = posX + 200, y = posY + 80)

        self.canvas.create_text(posX + 120, posY + 100, anchor = NW, text = "Balance: ")
        self.BlcEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.BlcEntry.place(x = posX + 200, y = posY + 100)

        self.canvas.create_text(posX + 120, posY + 120, anchor = NW, text = "Sabiduría: ")
        self.WsdEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.WsdEntry.place(x = posX + 200, y = posY + 120)

        self.canvas.create_text(posX + 120, posY + 140, anchor = NW, text = "Suerte: ")
        self.LckEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.LckEntry.place(x = posX + 200, y = posY + 140)

        self.canvas.create_text(posX + 120, posY + 160, anchor = NW, text = "Coordinación: ")
        self.CoordEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.CoordEntry.place(x = posX + 200, y = posY + 160)

        self.canvas.create_text(posX + 240, posY, anchor = NW, text = "Amabilidad: ")
        self.AmaEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.AmaEntry.place(x = posX + 320, y = posY)        

        self.canvas.create_text(posX + 240, posY + 20, anchor = NW, text = "Lealtad: ")
        self.LoyaltyEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.LoyaltyEntry.place(x = posX + 320, y = posY + 20)

        self.canvas.create_text(posX + 240, posY + 40, anchor = NW, text = "Disciplina: ")
        self.DscpEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.DscpEntry.place(x = posX + 320, y = posY + 40)

        self.canvas.create_text(posX + 240, posY + 60, anchor = NW, text = "Liderazgo: ")
        self.LdrEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.LdrEntry.place(x = posX + 320, y = posY + 60)

        self.canvas.create_text(posX + 240, posY + 80, anchor = NW, text = "Prudencia: ")
        self.PrdcEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.PrdcEntry.place(x = posX + 320, y = posY + 80)

        self.canvas.create_text(posX + 240, posY + 100, anchor = NW, text = "Confianza: ")
        self.TrustEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.TrustEntry.place(x = posX + 320, y = posY + 100)

        self.canvas.create_text(posX + 240, posY + 120, anchor = NW, text = "Percepción: ")
        self.PercEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.PercEntry.place(x = posX + 320, y = posY + 120)

        self.canvas.create_text(posX + 240, posY + 140, anchor = NW, text = "Valentía: ")
        self.CrgEntry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.CrgEntry.place(x = posX + 320, y = posY + 140)
    
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
        
    def checkStats(self):
        strStats = []
        strStats.append(self.PowerEntry.get())
        strStats.append(self.SpeedEntry.get())
        strStats.append(self.MagicEntry.get())
        strStats.append(self.DefEntry.get())
        strStats.append(self.IntEntry.get())
        strStats.append(self.HeightEntry.get())
        strStats.append(self.StrEntry.get())
        strStats.append(self.AglEntry.get())
        strStats.append(self.JumpEntry.get())
        strStats.append(self.ResEntry.get())
        strStats.append(self.FlexEntry.get())
        strStats.append(self.ExplEntry.get())
        strStats.append(self.ChrsEntry.get())
        strStats.append(self.AblEntry.get())
        strStats.append(self.BlcEntry.get())
        strStats.append(self.WsdEntry.get())
        strStats.append(self.LckEntry.get())
        strStats.append(self.CoordEntry.get())
        strStats.append(self.AmaEntry.get())
        strStats.append(self.LoyaltyEntry.get())
        strStats.append(self.DscpEntry.get())
        strStats.append(self.LdrEntry.get())
        strStats.append(self.PrdcEntry.get())
        strStats.append(self.TrustEntry.get())
        strStats.append(self.PercEntry.get())
        strStats.append(self.CrgEntry.get())
        checking = []
        checking.append("Poder")
        checking.append("Velocidad")
        checking.append("Magia")
        checking.append("Defensa")
        checking.append("Inteligencia")
        checking.append("Altura")
        checking.append("Fuerza")
        checking.append("Agilidad")
        checking.append("Salto")
        checking.append("Resistencia")
        checking.append("Flexibilidad")
        checking.append("Explosividad")
        checking.append("Carisma")
        checking.append("Habilidad")
        checking.append("Balance")
        checking.append("Sabiduría")
        checking.append("Suerte")
        checking.append("Coordinación")
        checking.append("Amabilidad")
        checking.append("Lealtad")
        checking.append("Disciplina")
        checking.append("Liderazgo")
        checking.append("Prudencia")
        checking.append("Confianza")
        checking.append("Percepción")
        checking.append("Valentía")
        stats = []
        for i in range(0, 25):
            try: 
                stat = int(strStats[i])
                if abs(stat) > 100:
                    messagebox.showerror("Error", f"El valor de {checking[i]} debe estar entre -100 y 100")
                else:
                    stats.append(stat)
            except:
                messagebox.showerror("Error", f"Valor inválido para {checking[i]}")
        return stats

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
        if len(name) < 5:
            messagebox.showerror("Error", "El nombre de la carta debe tener entre 5 y 30 caracteres")
            return
        desc = self.DescText.get('1.0', 'end-1c')
        var = self.VarEntry.get()
        isMain = not self.isVar.get()
        if not isMain and len(var) < 5:
            messagebox.showerror("Error", "El nombre de variante de la carta debe tener entre 5 y 30 caracteres")
            return
        race = self.race.get()
        if race == "":
            messagebox.showerror("Error", "Seleccione una raza para la carta")
            return
        rarity = self.rarity.get()
        if rarity == "":
            messagebox.showerror("Error", "Seleccione una rareza para la carta")
            return
        image = self.img
        stats = self.checkStats()
        if len(stats) < 26:
            return
        else:
            self.caller.cards.append(Card(name, self.img))
            self.NameEntry.delete(0, END)
            if self.img != "noImage.jpg":
                shutil.copy(self.path, self.savePath)
                self.img = "noImage.jpg"
                self.path = ""
            messagebox.showinfo("Éxito", f"Carta {name} agregada")

    def back(self):
        self.window.destroy()
        self.caller.window.deiconify()