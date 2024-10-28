from MainWindow import *

def main():
    root = tk.Tk()
    root.title("PowerDeck")
    root.resizable(width = tk.NO, height = tk.NO)
    main = MainWindow(root)
    main.run()

if __name__ == "__main__":
    main()