from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os, shutil

from functions import *
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
        self.name_entry = Entry(self.canvas, width = 30)
        self.name_entry.place(x = 60, y = 50)   
        self.name_entry.bind('<KeyPress>', self.nameCharCount)
        self.name_entry.bind('<KeyRelease>', self.nameCharCount)     

        self.canvas.create_text(10, 70, anchor = NW, text = "Variante: ")
        self.var_entry = Entry(self.canvas, width = 30)
        self.var_entry.place(x = 60, y = 70)
        self.var_entry.bind('<KeyPress>', self.varCharCount)
        self.var_entry.bind('<KeyRelease>', self.varCharCount) 

        self.isVar = BooleanVar(self.canvas)
        self.var_check = ttk.Checkbutton(self.canvas, text= "Variante", variable = self.isVar)
        self.var_check.place(x = 160, y = 90)

        self.canvas.create_text(10, 90, anchor = NW, text = "Raza: ")
        self.race_combo = ttk.Combobox(self.canvas, state = "readonly", values = self.races, width = 10)
        self.race_combo.place(x = 60, y = 90)

        self.canvas.create_text(10, 110, anchor = NW, text = "Rareza: ")
        self.rarity_combo = ttk.Combobox(self.canvas, state = "readonly", values = self.rarities, width = 10)
        self.rarity_combo.place(x = 60, y = 110)

        self.canvas.create_text(250, 50, anchor = NW, text = "Descripción: ")
        self.desc_text = Text(self.canvas, width = 50, height = 5)
        self.desc_text.place(x = 320, y = 50)
        self.desc_text.bind('<KeyPress>', self.descCharCount)
        self.desc_text.bind('<KeyRelease>', self.descCharCount)
        self.scroll = Scrollbar(self.canvas)
        self.scroll.place(height = 10, x = 750, y = 50)
        self.scroll.config(command = self.desc_text.yview)
    	
        vcmd = (self.window.register(self.checkNum), '%P')
        self.canvas.create_text(10, 140, anchor = NW, text = "Turno de Poder: ")
        self.turn_power_entry = Entry(self.canvas, width = 3, validate = "key", validatecommand = vcmd)
        self.turn_power_entry.place(x = 100, y = 140)

        self.canvas.create_text(10, 160, anchor = NW, text = "Bonus de Poder: ")
        self.bonus_power_entry = Entry(self.canvas, width = 3, validate = "key", validatecommand = vcmd)
        self.bonus_power_entry.place(x = 100, y = 160)

        self.placeStatEntries(10, 200)

        self.selected_img = loadImage("noImage.jpg")
        self.canvas.create_image(450, 180, anchor = NW, image = self.selected_img, tags = "selection")

        self.select_img_button = Button(self.canvas, text = "Seleccionar Imagen", command = self.getImage)
        self.select_img_button.place(x = 500, y = 150)

        self.add_button = Button(self.canvas, text = "Agregar Carta", command = self.addCard)
        self.add_button.place(x = 70, y = 380)
        
        self.back_button = Button(self.canvas, text = "Atrás", command = self.back)
        self.back_button.place(x = 760, y = 500)

    def placeStatEntries(self, posX, posY):
        vcmd = (self.window.register(self.checkStatNum), '%P')
        self.canvas.create_text(posX, posY, anchor = NW, text = "Poder: ")
        self.power_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.power_entry.place(x = posX + 80, y = posY)        

        self.canvas.create_text(posX, posY + 20, anchor = NW, text = "Velocidad: ")
        self.speed_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.speed_entry.place(x = posX + 80, y = posY + 20)

        self.canvas.create_text(posX, posY + 40, anchor = NW, text = "Magia: ")
        self.magic_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.magic_entry.place(x = posX + 80, y = posY + 40)

        self.canvas.create_text(posX, posY + 60, anchor = NW, text = "Defensa: ")
        self.defense_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.defense_entry.place(x = posX + 80, y = posY + 60)

        self.canvas.create_text(posX, posY + 80, anchor = NW, text = "Inteligencia: ")
        self.intelligence_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.intelligence_entry.place(x = posX + 80, y = posY + 80)

        self.canvas.create_text(posX, posY + 100, anchor = NW, text = "Altura: ")
        self.height_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.height_entry.place(x = posX + 80, y = posY + 100)

        self.canvas.create_text(posX, posY + 120, anchor = NW, text = "Fuerza: ")
        self.strenght_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.strenght_entry.place(x = posX + 80, y = posY + 120)

        self.canvas.create_text(posX, posY + 140, anchor = NW, text = "Agilidad: ")
        self.agility_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.agility_entry.place(x = posX + 80, y = posY + 140)

        self.canvas.create_text(posX, posY + 160, anchor = NW, text = "Salto: ")
        self.jump_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.jump_entry.place(x = posX + 80, y = posY + 160)

        self.canvas.create_text(posX + 120, posY, anchor = NW, text = "Resistencia: ")
        self.resistance_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.resistance_entry.place(x = posX + 200, y = posY)        

        self.canvas.create_text(posX + 120, posY + 20, anchor = NW, text = "Flexibilidad: ")
        self.flexibility_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.flexibility_entry.place(x = posX + 200, y = posY + 20)

        self.canvas.create_text(posX + 120, posY + 40, anchor = NW, text = "Explosividad: ")
        self.explosiveness_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.explosiveness_entry.place(x = posX + 200, y = posY + 40)

        self.canvas.create_text(posX + 120, posY + 60, anchor = NW, text = "Carisma: ")
        self.charisma_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.charisma_entry.place(x = posX + 200, y = posY + 60)

        self.canvas.create_text(posX + 120, posY + 80, anchor = NW, text = "Habilidad: ")
        self.ability_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.ability_entry.place(x = posX + 200, y = posY + 80)

        self.canvas.create_text(posX + 120, posY + 100, anchor = NW, text = "Balance: ")
        self.balance_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.balance_entry.place(x = posX + 200, y = posY + 100)

        self.canvas.create_text(posX + 120, posY + 120, anchor = NW, text = "Sabiduría: ")
        self.wisdom_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.wisdom_entry.place(x = posX + 200, y = posY + 120)

        self.canvas.create_text(posX + 120, posY + 140, anchor = NW, text = "Suerte: ")
        self.luck_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.luck_entry.place(x = posX + 200, y = posY + 140)

        self.canvas.create_text(posX + 120, posY + 160, anchor = NW, text = "Coordinación: ")
        self.coordination_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.coordination_entry.place(x = posX + 200, y = posY + 160)

        self.canvas.create_text(posX + 240, posY, anchor = NW, text = "Amabilidad: ")
        self.kindness_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.kindness_entry.place(x = posX + 320, y = posY)        

        self.canvas.create_text(posX + 240, posY + 20, anchor = NW, text = "Lealtad: ")
        self.loyalty_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.loyalty_entry.place(x = posX + 320, y = posY + 20)

        self.canvas.create_text(posX + 240, posY + 40, anchor = NW, text = "Disciplina: ")
        self.discipline_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.discipline_entry.place(x = posX + 320, y = posY + 40)

        self.canvas.create_text(posX + 240, posY + 60, anchor = NW, text = "Liderazgo: ")
        self.leadership_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.leadership_entry.place(x = posX + 320, y = posY + 60)

        self.canvas.create_text(posX + 240, posY + 80, anchor = NW, text = "Prudencia: ")
        self.prudence_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.prudence_entry.place(x = posX + 320, y = posY + 80)

        self.canvas.create_text(posX + 240, posY + 100, anchor = NW, text = "Confianza: ")
        self.trust_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.trust_entry.place(x = posX + 320, y = posY + 100)

        self.canvas.create_text(posX + 240, posY + 120, anchor = NW, text = "Percepción: ")
        self.perception_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.perception_entry.place(x = posX + 320, y = posY + 120)

        self.canvas.create_text(posX + 240, posY + 140, anchor = NW, text = "Valentía: ")
        self.courage_entry = Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.courage_entry.place(x = posX + 320, y = posY + 140)
    
    def run(self):
        self.window.mainloop()

    def nameCharCount(self, event):
        count = len(self.name_entry.get())
        if count >= 30 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'
        
    def varCharCount(self, event):
        count = len(self.var_entry.get())
        if count >= 30 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'

    def descCharCount(self, event):
        count = len(self.desc_text.get('1.0', 'end-1c'))
        if count >= 1000 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'

    def checkNum(self, P):
        if P == "":
            return True
        elif len(P) <= 3:
            if str.isdigit(P):
                return True
            else:
                return False
        else:
            return False
                
    def checkStatNum(self, P):
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
        str_stats = []
        str_stats.append(self.power_entry.get())
        str_stats.append(self.speed_entry.get())
        str_stats.append(self.magic_entry.get())
        str_stats.append(self.defense_entry.get())
        str_stats.append(self.intelligence_entry.get())
        str_stats.append(self.height_entry.get())
        str_stats.append(self.strenght_entry.get())
        str_stats.append(self.agility_entry.get())
        str_stats.append(self.jump_entry.get())
        str_stats.append(self.resistance_entry.get())
        str_stats.append(self.flexibility_entry.get())
        str_stats.append(self.explosiveness_entry.get())
        str_stats.append(self.charisma_entry.get())
        str_stats.append(self.ability_entry.get())
        str_stats.append(self.balance_entry.get())
        str_stats.append(self.wisdom_entry.get())
        str_stats.append(self.luck_entry.get())
        str_stats.append(self.coordination_entry.get())
        str_stats.append(self.kindness_entry.get())
        str_stats.append(self.loyalty_entry.get())
        str_stats.append(self.discipline_entry.get())
        str_stats.append(self.leadership_entry.get())
        str_stats.append(self.prudence_entry.get())
        str_stats.append(self.trust_entry.get())
        str_stats.append(self.perception_entry.get())
        str_stats.append(self.courage_entry.get())
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
        for i in range(0, 26):
            try: 
                stat = int(str_stats[i])
                if abs(stat) > 100:
                    messagebox.showerror("Error", f"El valor de {checking[i]} debe estar entre -100 y 100")
                    break
                else:
                    stats.append(stat)
            except:
                messagebox.showerror("Error", f"Valor inválido para {checking[i]}")
                break
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
                self.selected_img = loadExternalImage(self.path)
                self.canvas.itemconfig("selection", image = self.selected_img)
        else:
            self.path = ""
            messagebox.showerror("Error", "Seleccione una imagen (png o jpg)")

    def clearEntries(self):
        self.name_entry.delete(0, END)
        self.var_entry.delete(0, END)
        self.desc_text.delete(0, END)
        self.turn_power_entry.delete(0, END)
        self.bonus_power_entry.delete(0, END)
        self.power_entry.delete(0, END)
        self.speed_entry.delete(0, END)
        self.magic_entry.delete(0, END)
        self.defense_entry.delete(0, END)
        self.intelligence_entry.delete(0, END)
        self.height_entry.delete(0, END)
        self.strenght_entry.delete(0, END)
        self.agility_entry.delete(0, END)
        self.jump_entry.delete(0, END)
        self.resistance_entry.delete(0, END)
        self.flexibility_entry.delete(0, END)
        self.explosiveness_entry.delete(0, END)
        self.charisma_entry.delete(0, END)
        self.ability_entry.delete(0, END)
        self.balance_entry.delete(0, END)
        self.wisdom_entry.delete(0, END)
        self.luck_entry.delete(0, END)
        self.coordination_entry.delete(0, END)
        self.kindness_entry.delete(0, END)
        self.loyalty_entry.delete(0, END)
        self.discipline_entry.delete(0, END)
        self.leadership_entry.delete(0, END)
        self.prudence_entry.delete(0, END)
        self.trust_entry.delete(0, END)
        self.perception_entry.delete(0, END)
        self.courage_entry.delete(0, END)


    def addCard(self):
        name = self.name_entry.get()
        if len(name) < 5:
            messagebox.showerror("Error", "El nombre de la carta debe tener entre 5 y 30 caracteres")
            return
        
        desc = self.desc_text.get('1.0', 'end-1c')

        isMain = not self.isVar.get()

        var = self.var_entry.get()
        if len(var) < 5:
            messagebox.showerror("Error", "El nombre de variante de la carta debe tener entre 5 y 30 caracteres")
            return
        
        race = self.race_combo.get()
        if race == "":
            messagebox.showerror("Error", "Seleccione una raza para la carta")
            return
        
        rarity = self.rarity_combo.get()
        if rarity == "":
            messagebox.showerror("Error", "Seleccione una rareza para la carta")
            return
        
        image = self.img

        str_turn_power = self.turn_power_entry.get()
        if str_turn_power == "":
            messagebox.showerror("Error", "Ingrese un valor para el turno de poder")
            return
        turn_power = int(str_turn_power)
        if turn_power > 100:
            messagebox.showerror("Error", "El valor de turno de poder debe estar entre 0 y 100")
            return
        
        str_bonus_power = self.bonus_power_entry.get()
        if str_bonus_power == "":
            messagebox.showerror("Error", "Ingrese un valor para el bonus de poder")
            return
        bonus_power = int(str_bonus_power)
        if bonus_power > 100:
            messagebox.showerror("Error", "El valor de bonus de poder debe estar entre 0 y 100")
            return

        stats = self.checkStats()
        if len(stats) < 26:
            return
        
        if len(self.caller.cards) > 0:
            for i in self.caller.cards:
                if i.getName() == name:
                    isMain = False
                    if i.getVarName() == var:
                        messagebox.showerror("Error", f"La variante {var} de la carta {name} ya existe")
                        return
        
        if image == "noImage.jpg":
            messagebox.showerror("Error", "Seleccione una imagen para la carta")
            return
        shutil.copy(self.path, self.savePath)
        self.img = "noImage.jpg"
        self.path = ""

        newCard = Card(name, desc, var, isMain, race, rarity, image, turn_power, bonus_power)
        newCard.setStats(stats)
        self.caller.cards.append(newCard)
        self.caller.saveCards()          
        messagebox.showinfo("Éxito", f"Carta {name}, variante {var} agregada")

    def back(self):
        self.window.destroy()
        self.caller.window.deiconify()