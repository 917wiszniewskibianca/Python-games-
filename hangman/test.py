import unittest
from Sentence_repo import Sentence_repo
from Game import Game
class test_sentence_repository(unittest.TestCase):
    def test_add_new_sentence__good_sentence__sentence_added_to_the_repo(self):
       sentence_repository= Sentence_repo()
       sentence_repository.sentence_repo = ["Ana merge langa mare"]
       sentence_repository.add_sentence("Mergem frumos")
       assert sentence_repository.sentence_repo == ["Ana merge langa mare", "Mergem frumos"]

    def test_add_new_sentence__existing_sentence__throws_exception(self):
        try:
            sentence_repository = Sentence_repo()
            sentence_repository.sentence_repo = ["Ana merge langa mare"]
            sentence_repository.add_sentence("Ana merge langa mare")
        except IndexError as ve:
            assert str(ve) == "The sentence you are trying to add to the repository already exists!"

    def test_add_new_sentence__too_short_words__throws_exception(self):
        try:
            sentence_repository = Sentence_repo()
            sentence_repository.sentence_repo = ["Ana merge langa mare"]
            sentence_repository.add_sentence("Ana merge la mare")
        except IndexError as ve:
            assert str(ve) == "The sentence is incorrect!"

    def test_add_new_sentence__no_sentence__thwors_exception(self):
        try:
            sentence_repository = Sentence_repo()
            sentence_repository.sentence_repo = ["Ana merge langa mare"]
            sentence_repository.add_sentence("")
        except IndexError as ve:
            assert str(ve) == "The sentence should have at least a word!"

class test_game_create_sentence_to_display(unittest.TestCase):
    def test_create_sentence_to_display__good_sentence__shows_sentence_in_hangman_style(self):
        sentence_repository = Sentence_repo()
        game=Game(sentence_repository)
        game._sentence = "Maria"
        game.create_sentence_to_display()
        sentence = game.sentence_to_display
        assert sentence == ['M', ' ', 'a', ' ', 'r', ' ', 'i', ' ', 'a', ' ']

class test_game_check_if_guess_is_correct(unittest.TestCase):
    def test_check_if_guess_if_corect__returns_true__correct_guess(self):
        sentence_repository = Sentence_repo()
        game = Game(sentence_repository)
        game._sentence = "Maria"
        assert  game.check_if_guess_is_correct('a') == True

    def test_check_if_guess_if_corect__returns_none__wrong_guess(self):
        sentence_repository = Sentence_repo()
        game = Game(sentence_repository)
        game._sentence = "Maria"
        assert game.check_if_guess_is_correct('z') == None

class test_game_check_if_the_user_has_already_guessd_this_letter(unittest.TestCase):
    def test_check_if_the_user_has_already_guessed_this__returns_true__letter_already_guessed(self):
        sentence_repository = Sentence_repo()
        game = Game(sentence_repository)
        game._sentence = "Maria"
        game.users_guesses=['a']
        assert game.check_if_the_user_already_guessed_this('a') == True
    def test_check_if_the_user_has_already_guessed_this__returns_false__letter_not_already_guessed(self):
        sentence_repository = Sentence_repo()
        game = Game(sentence_repository)
        game._sentence = "Maria"
        game.users_guesses=['a']
        assert game.check_if_the_user_already_guessed_this('z') == False


class test_game_sentence_is_not_complete(unittest.TestCase):
    def test_sentence_is_not_complete__returns_true__sentence_not_complete(self):
       sentence_repository = Sentence_repo()
       game = Game(sentence_repository)
       game._sentence = "Maria"
       game.sentence_to_display=['M', ' ', '_', ' ', 'r', ' ', 'i', ' ', 'a', ' ']
       assert game.sentence_is_not_complete() == True

    def test_sentence_is_not_complete__returns_false__sentence_complete(self):
       sentence_repository = Sentence_repo()
       game = Game(sentence_repository)
       game._sentence = "Maria"
       game.sentence_to_display=['M', ' ', 'a', ' ', 'r', ' ', 'i', ' ', 'a', ' ']
       assert game.sentence_is_not_complete() ==False



