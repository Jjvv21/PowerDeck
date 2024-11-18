from UI.LogInUI import *

def main():
    root = tk.Tk()
    root.title("Inicio de Sesión")
    root.resizable(width = tk.NO, height = tk.NO)
    main = LogInUI(root)
    main.run()

if __name__ == "__main__":
    main()