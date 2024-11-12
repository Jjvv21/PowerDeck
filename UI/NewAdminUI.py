import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class NewAdminUI:

    def __init__(self, window, caller, admin_manager, player_manager):
        """
        Constructor that intializes and places the widgets of the UI.

        :window: Toplevel container for the widgets.
        :caller: UI that called this one.
        :admin_manager: manager for the admins accounts info.
        """
        self.caller = caller
        self.admin_manager = admin_manager
        self.player_manager = player_manager
        self.window = window
        self.canvas = tk.Canvas(self.window, width = 550, height = 450, bg = "#78a090")
        self.canvas.pack()

        self.canvas.create_text(10, 50, anchor = tk.NW, text = "Nombre: ")
        self.name_entry = tk.Entry(self.canvas, width = 30)
        self.name_entry.place(x = 60, y = 50)   
        self.name_entry.bind('<KeyPress>', self.nameCharCount)
        self.name_entry.bind('<KeyRelease>', self.nameCharCount)     

        self.canvas.create_text(10, 70, anchor = tk.NW, text = "Correo: ")
        self.mail_entry = tk.Entry(self.canvas, width = 30)
        self.mail_entry.place(x = 60, y = 70)

        vcmd = (self.window.register(self.checkPassword), '%P')
        self.canvas.create_text(10, 90, anchor = tk.NW, text = "Contraseña: ")
        self.password_entry = tk.Entry(self.canvas, show = "*", width = 8, validate = "key", validatecommand = vcmd)
        self.password_entry.place(x = 150, y = 90)

        self.canvas.create_text(10, 110, anchor = tk.NW, text = "Confirmar Contraseña: ")
        self.confirm_password_entry = tk.Entry(self.canvas, show = "*", width = 8, validate = "key", validatecommand = vcmd)
        self.confirm_password_entry.place(x = 150, y = 110)

        self.canvas.create_text(10, 130, anchor = tk.NW, text = "Rol: ")
        self.rol_combo = ttk.Combobox(self.canvas, state = "readonly",values = ["Juego", "Control"], width = 7)
        self.rol_combo.place(x = 60, y = 150)

        self.back_button = tk.Button(self.canvas, text = "Crear", command = self.createAdmin)
        self.back_button.place(x = 50, y = 320)

        self.back_button = tk.Button(self.canvas, text = "Volver", command = self.back)
        self.back_button.place(x = 490, y = 330)

    def nameCharCount(self, event):
        """
        nameCharCount limits the amount of characters for the name entry.

        :event: event that triggers the check.
        """
        count = len(self.name_entry.get())
        if count >= 30 and event.keysym not in {'BackSpace', 'Delete'}:
            return 'break'
        
    def checkPassword(self, P):
        """
        checkPassword limits the characters to alphanumeric, which are the only ones usable for passwords.

        :P: string to check.
        :return: True if the string is valid, False otherwise.
        """
        if P == "":
            return True
        elif len(P) <= 8:
            if str.isalnum(P):
                return True
            else:
                return False
        else:
            return False

    def createAdmin(self):
        """
        createAdmin gets the information from the entries, checks if the two passwords are the same
        and if so, tries to have the admin_manager create the admin with the info, notifying the result.
        """
        admin_info = []
        admin_info.append(self.name_entry.get())
        admin_info.append(self.mail_entry.get())

        admin_info.append(self.password_entry.get())
        password_confirmation = self.confirm_password_entry.get()
        if admin_info[2] != password_confirmation:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return
        
        admin_info.append(self.rol_combo.get())

        result = self.admin_manager.add(admin_info, self.player_manager)
        match result:
            case -1:
                messagebox.showerror("Error", "El nombre debe tener entre 5 y 30 caracteres")
            case -2:
                messagebox.showerror("Error", "Ingrese un correo")
            case -3:
                messagebox.showerror("Error", "El correo ya se encuentra en uso")
            case -4:
                messagebox.showerror("Error", "Ingrese una contraseña entre 6 y 8 caracteres")
            case -5:
                messagebox.showerror("Error", "Contraseña inválida, debe ser alfanumérica")
            case -6:
                messagebox.showerror("Error", "Seleccione un rol")
            case _:
                admin = self.admin_manager.getAdmin(result)
                messagebox.showinfo("Éxito", f"Administrador de  {admin_info[1]} creado \n \n")
                self.admin_manager.save()
                self.back()
        
    def run(self):
        """
        run runs the main loop of the UI.
        """
        self.window.mainloop()

    def back(self):
        """
        back returns to the UI that called this one.
        """
        self.window.destroy()
        self.caller.window.deiconify()