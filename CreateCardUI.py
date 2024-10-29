import tkinter as tk 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from ImageHandler import *

class CreateCardUI:
    image_name = "noImage.jpg"
    path = ""
    img_handler = ImageHandler()
    races = ["Raza1", "Raza2", "Raza3", "Raza4", "Raza5"]
    rarities = ["Ultra-Rara", "Muy Rara", "Rara", "Normal", "Básica"]

    def __init__(self, window, caller, album):
        self.caller = caller
        self.album = album
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 750, height = 550, bg = "#78a090")
        self.canvas.pack()

        self.canvas.create_text(200, 5, anchor = tk.NW, text = "Crear Carta")
        
        self.canvas.create_text(10, 50, anchor = tk.NW, text = "Nombre: ")
        self.name_entry = tk.Entry(self.canvas, width = 30)
        self.name_entry.place(x = 60, y = 50)   
        self.name_entry.bind('<KeyPress>', self.nameCharCount)
        self.name_entry.bind('<KeyRelease>', self.nameCharCount)     

        self.canvas.create_text(10, 70, anchor = tk.NW, text = "Variante: ")
        self.var_entry = tk.Entry(self.canvas, width = 30)
        self.var_entry.place(x = 60, y = 70)
        self.var_entry.bind('<KeyPress>', self.varCharCount)
        self.var_entry.bind('<KeyRelease>', self.varCharCount) 

        self.isVar = tk.BooleanVar(self.canvas)
        self.var_check = ttk.Checkbutton(self.canvas, text = "Variante", variable = self.isVar, state = tk.DISABLED)
        self.var_check.place(x = 160, y = 90)

        self.canvas.create_text(10, 90, anchor = tk.NW, text = "Raza: ")
        self.race_combo = ttk.Combobox(self.canvas, state = "readonly", values = self.races, width = 10)
        self.race_combo.place(x = 60, y = 90)

        self.canvas.create_text(10, 110, anchor = tk.NW, text = "Rareza: ")
        self.rarity_combo = ttk.Combobox(self.canvas, state = "readonly", values = self.rarities, width = 10)
        self.rarity_combo.place(x = 60, y = 110)

        self.canvas.create_text(250, 50, anchor = tk.NW, text = "Descripción: ")
        self.desc_text = tk.Text(self.canvas, width = 50, height = 5)
        self.desc_text.place(x = 320, y = 50)
        self.desc_text.bind('<KeyPress>', self.descCharCount)
        self.desc_text.bind('<KeyRelease>', self.descCharCount)
        self.scroll = tk.Scrollbar(self.canvas)
        self.scroll.place(height = 83, x = 725, y = 51)
        self.scroll.config(command = self.desc_text.yview)
    	
        vcmd = (self.window.register(self.checkNum), '%P')
        self.canvas.create_text(10, 140, anchor = tk.NW, text = "Turno de Poder: ")
        self.turn_power_entry = tk.Entry(self.canvas, width = 3, validate = "key", validatecommand = vcmd)
        self.turn_power_entry.place(x = 100, y = 140)

        self.canvas.create_text(10, 160, anchor = tk.NW, text = "Bonus de Poder: ")
        self.bonus_power_entry = tk.Entry(self.canvas, width = 3, validate = "key", validatecommand = vcmd)
        self.bonus_power_entry.place(x = 100, y = 160)

        self.placeStatEntries(10, 200)

        self.selected_img = self.img_handler.loadImage("noImage.jpg")
        self.canvas.create_image(450, 180, anchor = tk.NW, image = self.selected_img, tags = "selection")

        self.select_img_button = tk.Button(self.canvas, text = "Seleccionar Imagen", command = self.getImage)
        self.select_img_button.place(x = 500, y = 150)

        self.add_button = tk.Button(self.canvas, text = "Crear Carta", command = self.createCard)
        self.add_button.place(x = 100, y = 400)

        self.clear_button = tk.Button(self.canvas, text = "Reiniciar", command = self.clearEntries)
        self.clear_button.place(x = 100, y = 430)
        
        self.back_button = tk.Button(self.canvas, text = "Volver", command = self.back)
        self.back_button.place(x = 690, y = 520)

    def placeStatEntries(self, posX, posY):
        vcmd = (self.window.register(self.checkStatNum), '%P')
        self.canvas.create_text(posX, posY, anchor = tk.NW, text = "Poder: ")
        self.power_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.power_entry.place(x = posX + 80, y = posY)        

        self.canvas.create_text(posX, posY + 20, anchor = tk.NW, text = "Velocidad: ")
        self.speed_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.speed_entry.place(x = posX + 80, y = posY + 20)

        self.canvas.create_text(posX, posY + 40, anchor = tk.NW, text = "Magia: ")
        self.magic_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.magic_entry.place(x = posX + 80, y = posY + 40)

        self.canvas.create_text(posX, posY + 60, anchor = tk.NW, text = "Defensa: ")
        self.defense_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.defense_entry.place(x = posX + 80, y = posY + 60)

        self.canvas.create_text(posX, posY + 80, anchor = tk.NW, text = "Inteligencia: ")
        self.intelligence_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.intelligence_entry.place(x = posX + 80, y = posY + 80)

        self.canvas.create_text(posX, posY + 100, anchor = tk.NW, text = "Altura: ")
        self.height_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.height_entry.place(x = posX + 80, y = posY + 100)

        self.canvas.create_text(posX, posY + 120, anchor = tk.NW, text = "Fuerza: ")
        self.strenght_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.strenght_entry.place(x = posX + 80, y = posY + 120)

        self.canvas.create_text(posX, posY + 140, anchor = tk.NW, text = "Agilidad: ")
        self.agility_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.agility_entry.place(x = posX + 80, y = posY + 140)

        self.canvas.create_text(posX, posY + 160, anchor = tk.NW, text = "Salto: ")
        self.jump_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.jump_entry.place(x = posX + 80, y = posY + 160)

        self.canvas.create_text(posX + 120, posY, anchor = tk.NW, text = "Resistencia: ")
        self.resistance_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.resistance_entry.place(x = posX + 200, y = posY)        

        self.canvas.create_text(posX + 120, posY + 20, anchor = tk.NW, text = "Flexibilidad: ")
        self.flexibility_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.flexibility_entry.place(x = posX + 200, y = posY + 20)

        self.canvas.create_text(posX + 120, posY + 40, anchor = tk.NW, text = "Explosividad: ")
        self.explosiveness_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.explosiveness_entry.place(x = posX + 200, y = posY + 40)

        self.canvas.create_text(posX + 120, posY + 60, anchor = tk.NW, text = "Carisma: ")
        self.charisma_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.charisma_entry.place(x = posX + 200, y = posY + 60)

        self.canvas.create_text(posX + 120, posY + 80, anchor = tk.NW, text = "Habilidad: ")
        self.ability_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.ability_entry.place(x = posX + 200, y = posY + 80)

        self.canvas.create_text(posX + 120, posY + 100, anchor = tk.NW, text = "Balance: ")
        self.balance_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.balance_entry.place(x = posX + 200, y = posY + 100)

        self.canvas.create_text(posX + 120, posY + 120, anchor = tk.NW, text = "Sabiduría: ")
        self.wisdom_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.wisdom_entry.place(x = posX + 200, y = posY + 120)

        self.canvas.create_text(posX + 120, posY + 140, anchor = tk.NW, text = "Suerte: ")
        self.luck_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.luck_entry.place(x = posX + 200, y = posY + 140)

        self.canvas.create_text(posX + 120, posY + 160, anchor = tk.NW, text = "Coordinación: ")
        self.coordination_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.coordination_entry.place(x = posX + 200, y = posY + 160)

        self.canvas.create_text(posX + 240, posY, anchor = tk.NW, text = "Amabilidad: ")
        self.kindness_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.kindness_entry.place(x = posX + 320, y = posY)        

        self.canvas.create_text(posX + 240, posY + 20, anchor = tk.NW, text = "Lealtad: ")
        self.loyalty_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.loyalty_entry.place(x = posX + 320, y = posY + 20)

        self.canvas.create_text(posX + 240, posY + 40, anchor = tk.NW, text = "Disciplina: ")
        self.discipline_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.discipline_entry.place(x = posX + 320, y = posY + 40)

        self.canvas.create_text(posX + 240, posY + 60, anchor = tk.NW, text = "Liderazgo: ")
        self.leadership_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.leadership_entry.place(x = posX + 320, y = posY + 60)

        self.canvas.create_text(posX + 240, posY + 80, anchor = tk.NW, text = "Prudencia: ")
        self.prudence_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.prudence_entry.place(x = posX + 320, y = posY + 80)

        self.canvas.create_text(posX + 240, posY + 100, anchor = tk.NW, text = "Confianza: ")
        self.trust_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.trust_entry.place(x = posX + 320, y = posY + 100)

        self.canvas.create_text(posX + 240, posY + 120, anchor = tk.NW, text = "Percepción: ")
        self.perception_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.perception_entry.place(x = posX + 320, y = posY + 120)

        self.canvas.create_text(posX + 240, posY + 140, anchor = tk.NW, text = "Valentía: ")
        self.courage_entry = tk.Entry(self.canvas, width = 4, validate = "key", validatecommand = vcmd)
        self.courage_entry.place(x = posX + 320, y = posY + 140)

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
        
    def getStats(self):
        stats_strs = []
        stats_strs.append(self.power_entry.get())
        stats_strs.append(self.speed_entry.get())
        stats_strs.append(self.magic_entry.get())
        stats_strs.append(self.defense_entry.get())
        stats_strs.append(self.intelligence_entry.get())
        stats_strs.append(self.height_entry.get())
        stats_strs.append(self.strenght_entry.get())
        stats_strs.append(self.agility_entry.get())
        stats_strs.append(self.jump_entry.get())
        stats_strs.append(self.resistance_entry.get())
        stats_strs.append(self.flexibility_entry.get())
        stats_strs.append(self.explosiveness_entry.get())
        stats_strs.append(self.charisma_entry.get())
        stats_strs.append(self.ability_entry.get())
        stats_strs.append(self.balance_entry.get())
        stats_strs.append(self.wisdom_entry.get())
        stats_strs.append(self.luck_entry.get())
        stats_strs.append(self.coordination_entry.get())
        stats_strs.append(self.kindness_entry.get())
        stats_strs.append(self.loyalty_entry.get())
        stats_strs.append(self.discipline_entry.get())
        stats_strs.append(self.leadership_entry.get())
        stats_strs.append(self.prudence_entry.get())
        stats_strs.append(self.trust_entry.get())
        stats_strs.append(self.perception_entry.get())
        stats_strs.append(self.courage_entry.get())
        return stats_strs

    def getImage(self):
        self.path = filedialog.askopenfilename()
        isImage = self.img_handler.checkImage(self.path)
        match isImage:
            case -1:
                return
            case -2:
                messagebox.showerror("Error", "Seleccione una archivo .png o .jpg")
                self.path = ""
            case -3:
                messagebox.showerror("Error", "Tamaño de imagen incorrecto")
                self.path = ""
            case _:
                self.selected_img = self.img_handler.loadExternalImage(self.path)
                self.canvas.itemconfig("selection", image = self.selected_img)
                self.image_name = self.path[-isImage:]
                messagebox.showinfo("Éxito", "Imagen cargada")          

    def clearEntries(self):
        self.name_entry.delete(0, tk.END)
        self.var_entry.delete(0, tk.END)
        self.desc_text.delete('1.0', 'end-1c')
        self.turn_power_entry.delete(0, tk.END)
        self.bonus_power_entry.delete(0, tk.END)
        self.power_entry.delete(0, tk.END)
        self.speed_entry.delete(0, tk.END)
        self.magic_entry.delete(0, tk.END)
        self.defense_entry.delete(0, tk.END)
        self.intelligence_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.strenght_entry.delete(0, tk.END)
        self.agility_entry.delete(0, tk.END)
        self.jump_entry.delete(0, tk.END)
        self.resistance_entry.delete(0, tk.END)
        self.flexibility_entry.delete(0, tk.END)
        self.explosiveness_entry.delete(0, tk.END)
        self.charisma_entry.delete(0, tk.END)
        self.ability_entry.delete(0, tk.END)
        self.balance_entry.delete(0, tk.END)
        self.wisdom_entry.delete(0, tk.END)
        self.luck_entry.delete(0, tk.END)
        self.coordination_entry.delete(0, tk.END)
        self.kindness_entry.delete(0, tk.END)
        self.loyalty_entry.delete(0, tk.END)
        self.discipline_entry.delete(0, tk.END)
        self.leadership_entry.delete(0, tk.END)
        self.prudence_entry.delete(0, tk.END)
        self.trust_entry.delete(0, tk.END)
        self.perception_entry.delete(0, tk.END)
        self.courage_entry.delete(0, tk.END)

        self.image_name = "noImage.jpg"
        self.path = ""
        self.selected_img = self.img_handler.loadImage(self.image_name)
        self.canvas.itemconfig("selection", image = self.selected_img)


    def createCard(self):
        name = self.name_entry.get()
        desc = self.desc_text.get('1.0', 'end-1c')
        var = self.var_entry.get()
        race = self.race_combo.get()
        rarity = self.rarity_combo.get()
        image = self.image_name
        turn_power_str = self.turn_power_entry.get()
        bonus_power_str = self.bonus_power_entry.get()
        stats_strs = self.getStats()

        result = self.album.add(name, desc, var, race, rarity, image, turn_power_str, bonus_power_str, stats_strs)
        match result:
            case 0:
                messagebox.showinfo("Éxito", f"Carta {name}, {var} agregada")
                self.var_check.state(["!selected"])
                self.img_handler.saveImage(self.path)
            case 1:
                messagebox.showinfo("Éxito", f"Variante {name}, {var} agregada")
                self.var_check.state(["selected"])
                self.img_handler.saveImage(self.path)
            case -1:
                messagebox.showerror("Error", "El nombre de la carta debe tener entre 5 y 30 caracteres")
            case -2:
                messagebox.showerror("Error", "El nombre de variante de la carta debe tener entre 5 y 30 caracteres")
            case -3:
                messagebox.showerror("Error", f"La variante {var} de la carta {name} ya existe")
            case -4:
                messagebox.showerror("Error", "Seleccione una imagen para la carta")
            case -5:
                messagebox.showerror("Error", "Seleccione una raza para la carta")
            case -6:
                messagebox.showerror("Error", "Seleccione una rareza para la carta")
            case -7:
                messagebox.showerror("Error", "Ingrese un valor para el turno de poder")
            case -8:
                messagebox.showerror("Error", "El valor de turno de poder debe estar entre 0 y 100")
            case -9:
                messagebox.showerror("Error", "Ingrese un valor para el bonus de poder")
            case -10:
                messagebox.showerror("Error", "El valor de bonus de poder debe estar entre 0 y 100")
            case -11:
                messagebox.showerror("Error", "Valor inválido para Poder")
            case -12:
                messagebox.showerror("Error", "Valor inválido para Velocidad")
            case -13:
                messagebox.showerror("Error", "Valor inválido para Magia")
            case -14:
                messagebox.showerror("Error", "Valor inválido para Defensa")
            case -15:
                messagebox.showerror("Error", "Valor inválido para Inteligencia")
            case -16:
                messagebox.showerror("Error", "Valor inválido para Altura")
            case -17:
                messagebox.showerror("Error", "Valor inválido para Fuerza")
            case -18:
                messagebox.showerror("Error", "Valor inválido para Agilidad")
            case -19:
                messagebox.showerror("Error", "Valor inválido para Salto")
            case -20:
                messagebox.showerror("Error", "Valor inválido para Resistencia")
            case -21:
                messagebox.showerror("Error", "Valor inválido para Flexibilidad")
            case -22:
                messagebox.showerror("Error", "Valor inválido para Explosividad")
            case -23:
                messagebox.showerror("Error", "Valor inválido para Carisma")
            case -24:
                messagebox.showerror("Error", "Valor inválido para Habilidad")
            case -25:
                messagebox.showerror("Error", "Valor inválido para Balance")
            case -26:
                messagebox.showerror("Error", "Valor inválido para Sabiduría")
            case -27:
                messagebox.showerror("Error", "Valor inválido para Suerte")
            case -28:
                messagebox.showerror("Error", "Valor inválido para Coordinación")
            case -29:
                messagebox.showerror("Error", "Valor inválido para Amabilidad")
            case -30:
                messagebox.showerror("Error", "Valor inválido para Lealtad")
            case -31:
                messagebox.showerror("Error", "Valor inválido para Disciplina")
            case -32:
                messagebox.showerror("Error", "Valor inválido para Liderazgo")
            case -33:
                messagebox.showerror("Error", "Valor inválido para Prudencia")
            case -34:
                messagebox.showerror("Error", "Valor inválido para Confianza")
            case -35:
                messagebox.showerror("Error", "Valor inválido para Percepción")
            case -36:
                messagebox.showerror("Error", "Valor inválido para Valentía")
            case -37:
                messagebox.showerror("Error", "El valor de Poder debe estar entre -100 y 100")
            case -38:
                messagebox.showerror("Error", "El valor de Velocidad debe estar entre -100 y 100")
            case -39:
                messagebox.showerror("Error", "El valor de Magia debe estar entre -100 y 100")
            case -40:
                messagebox.showerror("Error", "El valor de Defensa debe estar entre -100 y 100")
            case -41:
                messagebox.showerror("Error", "El valor de Inteligencia debe estar entre -100 y 100")
            case -42:
                messagebox.showerror("Error", "El valor de Altura debe estar entre -100 y 100")
            case -43:
                messagebox.showerror("Error", "El valor de Fuerza debe estar entre -100 y 100")
            case -44:
                messagebox.showerror("Error", "El valor de Agilidad debe estar entre -100 y 100")
            case -45:
                messagebox.showerror("Error", "El valor de Salto debe estar entre -100 y 100")
            case -46:
                messagebox.showerror("Error", "El valor de Resistencia debe estar entre -100 y 100")
            case -47:
                messagebox.showerror("Error", "El valor de Flexibilidad debe estar entre -100 y 100")
            case -48:
                messagebox.showerror("Error", "El valor de Explosividad debe estar entre -100 y 100")
            case -49:
                messagebox.showerror("Error", "El valor de Carisma debe estar entre -100 y 100")
            case -50:
                messagebox.showerror("Error", "El valor de Habilidad debe estar entre -100 y 100")
            case -51:
                messagebox.showerror("Error", "El valor de Balance debe estar entre -100 y 100")
            case -52:
                messagebox.showerror("Error", "El valor de Sabiduría debe estar entre -100 y 100")
            case -53:
                messagebox.showerror("Error", "El valor de Suerte debe estar entre -100 y 100")
            case -54:
                messagebox.showerror("Error", "El valor de Coordinación debe estar entre -100 y 100")
            case -55:
                messagebox.showerror("Error", "El valor de Amabilidad debe estar entre -100 y 100")
            case -56:
                messagebox.showerror("Error", "El valor de Lealtad debe estar entre -100 y 100")
            case -57:
                messagebox.showerror("Error", "El valor de Disciplina debe estar entre -100 y 100")
            case -58:
                messagebox.showerror("Error", "El valor de Liderazgo debe estar entre -100 y 100")
            case -59:
                messagebox.showerror("Error", "El valor de Prudencia debe estar entre -100 y 100")
            case -60:
                messagebox.showerror("Error", "El valor de Confianza debe estar entre -100 y 100")
            case -61:
                messagebox.showerror("Error", "El valor de Percepción debe estar entre -100 y 100")
            case -62:
                messagebox.showerror("Error", "El valor de Valentía debe estar entre -100 y 100")

    def run(self):
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        self.caller.window.deiconify()