class Menu():
    def __init__(self,sentence_repo, game):
        """
        Initialising the menu
        :param sentence_repo: the repository with all the sentences the programm will choose from
        :param game: the game we implemented
        """
        self.sentence_repo=sentence_repo
        self.game=game

    def menu(self):
        print("1.Add a sentence")
        print("2. Start the game")

    def handle_menu_option(self):
        self.menu()
        game_started= False
        while game_started == False:
          try:
            option = input("What do you want to do? ")
            if option == '1':
                sentence=input("Enter a sentence: ")
                self.sentence_repo.add_sentence(sentence)
                print("The sentence was added to the repository!")
            elif option =='2':
                game_started=True
                self.game.start()
            else :
                raise IndexError("The command does not exist!")
          except IndexError as ve:
              print(str(ve))


