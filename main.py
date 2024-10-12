from MainWindow import *

def main():
    root = Tk()
    root.title("PowerDeck")
    root.resizable(width = NO, height = NO)
    main = MainWindow(root)
    main.run()

if __name__ == "__main__":
    main()