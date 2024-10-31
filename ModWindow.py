#self.scroll.place(height = 352, x = 275, y = 50)
#self.scroll = Scrollbar(self.canvas, bg = "#9194A7")
#self.listbox = Listbox(self.canvas, height = 18, width = 30, font = ("Consolas", 12), fg = "#ffffff", bg = "#901800", selectbackground = "#D05020", yscrollcommand = self.scroll.set)
#self.listbox.place(x = 1, y = 50)
#self.scroll.config(command = self.listbox.yview)
#for i in self.caller.cards:
#self.listbox.insert(END, i.name)

#self.canvas.create_text(310, 5, anchor = NW, text = "Seleccionado", font = ("Consolas", 20), fill = "#ffffff")
#self.selectedImg = loadImage(self.caller.cards[self.caller.selected].image)
#self.canvas.create_image(350, 50, anchor = NW, image = self.selectedImg, tags = "pilotimage")
#self.canvas.create_text(350, 150, anchor = NW, text = self.caller.cards[self.caller.selected].name, font = ("Consolas", 12), fill = "#ffffff", tags = "pilotname")

#self.canvas.create_text(290, 195, anchor = NW, text = "Editar Pilotos", font = ("Consolas", 20), fill = "#ffffff")

#self.ChangeButton = Button(self.canvas, text = "Modificar", bg = "#D05020", command = self.changeName)
#self.ChangeButton.place(x = 400, y = 280)

#    def selectPilot(self):
#        try:
#            self.caller.selected = self.listbox.curselection()[0]
#            self.updateSelection()
#        except:
#            messagebox.showerror("Error", "Seleccione un piloto")

#def updateSelection(self):
#        self.selectedImg = loadImage(self.caller.cards[self.caller.selected].image)
#        self.canvas.itemconfig("pilotimage", image = self.selectedImg)
#        self.canvas.itemconfig("pilotname", text = self.caller.cards[self.caller.selected].name)

#    def changeName(self):
#        try:
#            i = self.listbox.curselection()[0]
#            name = self.NameEntry.get()
#            self.NameEntry.delete(0, END)
#            self.caller.cards[i].name = name
#            self.listbox.delete(i)
#            self.listbox.insert(i, name)
#            self.updateSelection()
#            messagebox.showinfo("Exito", "Nombre cambiado")
#        except:
#            messagebox.showerror("Error", "Seleccione el piloto al que desea cambiar")

#def deletePilot(self):
#        try:
#            i = self.listbox.curselection()[0]
#            if len(self.caller.cards) > 1:
#                name = self.caller.cards[i].name
#                self.caller.cards.pop(i)
#                if self.caller.selected >= i:
#                    if i > 0:
#                        self.caller.selected -= 1
#                    else:
#                        self.caller.selected = 0
#                    self.updateSelection()
#                self.listbox.delete(i)
#                messagebox.showinfo("Exito", f"Piloto {name} eliminado")
#            else:
#                messagebox.showerror("Error", "Unico piloto disponible")
#        except:
#            messagebox.showerror("Error", "Seleccione el piloto que desea eliminar")


