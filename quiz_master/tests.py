from question_repo import question_repo
import unittest
from question import Question
class Test_question_repo(unittest.TestCase):
    def test_load_file__works_okay__existing_file(self):
        file_name="load_questions_test.txt"
        self.questions=question_repo(file_name)
        self.questions.load_questions()
        assert len(self.questions.question_repo)== 3
    def test__load_file__throws_exception__non_existing_file(self):
        try:
            file_name="acasa"
            self.questions = question_repo(file_name)
            self.questions.load_questions()
        except IOError and ValueError as ve:
            assert str(ve )== "The file could not be opened!"

    def test_transform_line__returns_a_type_question_from_the_line_input__good_input(self):
        id="3"
        text="Which number is prime"
        answear1="2"
        answear2="32"
        answear3="9"
        correct_answear="2"
        difficulty='hard'
        file_name = "load_questions_test.txt"
        self.questions =question_repo(file_name)
        new_question=self.questions.transform_line("3;Which number is prime;2;32;9;2;hard")
        a_question=Question(id,text,answear1,answear2,answear3,correct_answear,difficulty)
        print(new_question.get_id ,a_question.get_id)
        assert new_question.get_id == a_question.get_id and new_question.get_difficulty == a_question.get_difficulty and new_question.get_text == a_question.get_text
        assert new_question.answear1 == a_question.answear1 and new_question.get_answear2 == a_question.get_answear2 and new_question.get_answear3==a_question.get_answear3

    """
    def test__save_file__works_okay__good_input(self):
        file_name = "load_questions_test.txt"
        self.questions = question_repo(file_name)
        self.questions.load_questions()
        assert len(self.questions.question_repo) == 3
    """

