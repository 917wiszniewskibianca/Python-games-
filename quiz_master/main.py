from question_repo import question_repo
from Controller import Controller
class main:
    question_repo=question_repo("questions1.txt")
    question_repo.load_questions()
    controller= Controller(question_repo)
    controller.handle_user_options()