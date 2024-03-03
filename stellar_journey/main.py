from Game import Game
from menu import Menu
class main:
    game=Game()
    menu= Menu(game)
    menu.start()

if __name__ == "__main__":
    main()