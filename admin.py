from UI.AdminUI import *

def main():
    root = tk.Tk()
    root.title("Administración")
    root.resizable(width = tk.NO, height = tk.NO)
    main = AdminUI(root)
    main.run()

if __name__ == "__main__":
    main()