from Sentence_repo import Sentence_repo
from Game import Game
from menu import Menu

class main():
    """
    The class witch is responsible for starting the application and passing the needed parameters
    """
    sentence_repo=Sentence_repo("sentences.txt")
    game= Game(sentence_repo)
    menu= Menu(sentence_repo,game)
    menu.handle_menu_option()


if __name__ == "__main__":
    main()

