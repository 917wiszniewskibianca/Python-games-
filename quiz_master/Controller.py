from quiz import Quiz
class Controller:
     def __init__(self,question_repo):
         self.question_repo=question_repo

     def handle_user_options(self):
         """
         Function to handle the user input
         :return:
         """
         exitt= False
         while exitt == False:
           try:
             command=input("What do you want to do? ")
             list=command.split(" ")
             if list[0]=="add":
                 self.question_repo.add_question(list[1])
                 print("Question added to the repository!")
             elif list[0] == "create":
                 if len(list)!=4:
                     print(len(list))
                     raise ValueError("You are using the wrong format!")
                 if list[2].isdigit() !=True:
                     raise ValueError("The number of questions should be a digit!")
                 if list[1] != "easy" and list[1]!="hard" and list[1]!="medium":
                     raise ValueError("The difficulty should be easy, hard or medium!")
                 file_name=list[3]
                 if self.question_repo.can_create_quiz(list[1],list[2]):
                     new_quiz_repo=self.question_repo.return_quiz_repo(list[1],list[2])
                     new_quiz=Quiz(file_name)
                     new_quiz.quiz_repo=new_quiz_repo
                     new_quiz.save_quiz_to_file(file_name)
                     print("The quiz has been created!")
                 else:
                     raise ValueError("The quiz can not be created! Check the criteria and try again!")
             elif list[0]=="start":
                 file_name=list[1]
                 new_quiz=Quiz(file_name)
                 new_quiz.start_quiz(file_name)
             elif list[0] =="exit":
                 print("Bye!")
                 exit()
             else:
                 raise ValueError("The command does not exist!")
           except ValueError as ve:
             print(str(ve))









