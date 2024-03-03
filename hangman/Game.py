class Game:
    def __init__(self, sentence_repo):
        """
        Function to initialise the game class
        :param sentence_repo: the list of sentences the programm can choose from
        """
        self.sentence_repo=sentence_repo
        self._sentence=[]
        self.sentence_to_display = []
        self.game_over_message=["h","a","n","g","m","a","n"]
        self.number_of_wrong_guesses=0
        self._word_to_display_if_game_lost=""
        self.users_guesses=[]


    def start(self):
        """
        The application start-up. The function who checks that the input from the user is okay and acts accordingly
        """
        self._sentence= self.sentence_repo.choose_sentence()
        self.create_sentence_to_display()
        while self.number_of_wrong_guesses < 7 and self.sentence_is_not_complete() == True:
         print(self.print_sentence())
         guessed_letter=input("Take a guess ")
         if self.check_if_guess_is_correct(guessed_letter) is True and self.check_if_the_user_already_guessed_this(guessed_letter) is False:
                print("You guessed correct!")
                index=-1
                for i in range(len(self._sentence)):
                    for letter in self._sentence[i]:
                        index += 1
                        if letter == guessed_letter:
                            self.sentence_to_display[index]=guessed_letter
                    index+=1
                self.users_guesses.append(guessed_letter)
         else:
                self.number_of_wrong_guesses+=1
                self._word_to_display_if_game_lost+=self.game_over_message[self.number_of_wrong_guesses-1]
                print("The guess is incorrect!")
                print(self._word_to_display_if_game_lost)
                self.users_guesses.append(guessed_letter)
        if self.sentence_is_not_complete() is False:
            print("You won!")
        else:
            print("Game over!")
            exit()

    def create_sentence_to_display(self):
        """
        The function which creates the sentence in hangman style
        :return:
        """
        for word in self._sentence:
            index=-1
            for letter in word :
                index+=1
                if index == 0 or index == len(word)-1:
                    self.sentence_to_display.append(letter)
                else:
                    self.sentence_to_display.append("_")
            self.sentence_to_display.append(" ")


    def print_sentence(self):
        """
        Funtion to create a string out of the sentence to display
        :return: the sentence to display as a string
        """
        str_value=""
        for i in range(0,len(self.sentence_to_display)):
            str_value +=self.sentence_to_display[i]
        return str_value

    def check_if_guess_is_correct(self,guess):
        """
        Function to check if the user guess is correct
        :param guess: the user's guess
        :return: true if he guessed correctly
        """
        for i in range(len(self._sentence)):
            for letter in self._sentence[i]:
                if letter == guess:
                    return True

    def sentence_is_not_complete(self):
        """
        Function to check if the user guessed all the hidden letters
        :return: true if it did, false otherwise
        """
        sentence_not_complete= False
        for i in range(len(self.sentence_to_display)):
            if self.sentence_to_display[i] == "_":
                sentence_not_complete= True
                break
        if sentence_not_complete:
            return True
        else:
            return False
    def check_if_the_user_already_guessed_this(self,guess):
        """
        Function to check if the user guessed the same letter he guessed before
        :param guess: the letter to check
        :return: true if it did, false otherwise
        """
        already_guessed= False
        for i in range(len(self.users_guesses)):
            if self.users_guesses[i] ==  guess:
                already_guessed= True
        if already_guessed== True:
            return True
        else:
            return False








