from question import Question
class Quiz:
    def __init__(self,file_name):
       self.file_name=file_name
       self.quiz_repo=[]
       self.score=0

    def load_quiz(self,file_name):
        """
        Function to load the quiz from the file
        :param file_name: the name of the file from where we will take the questions
        :return:
        """
        try:
            file=open(file_name,"r")
        except IOError:
            raise ValueError("The file could not be opened!")
        line=file.readline()
        while line!="":
            new_question=self.transform_line(line)
            self.quiz_repo.append(new_question)
            line=file.readline()
        file.close()

    def save_quiz_to_file(self,file_name):
        """
        Function to save the new created quiz to  file
        :param file_name: the file where we will save the quiz
        """
        try:
            file=open(file_name,"w")
        except IOError :
            raise ValueError("The file can not be opened!")
        for question in self.quiz_repo:
            sentence=""
            sentence+= question.get_id +";"+question.get_text +";"+question.get_answear1 +";"+question.get_answear2 + ";" + question.get_answear3 + ";"+question.get_correct_answear + ";"+ question.get_difficulty
            file.write(sentence + "\n")
        file.close()


    def transform_line(self,line):
        """
        Function to transform the line read from the file into a question
        :param line: the line read from a file
        :return: a parameter of type Question
        """
        list=line.strip().split(";")
        if len(list)!=7:
               raise ValueError("The question is not in the correct format!")
        id=list[0]
        text=list[1]
        answear1=list[2]
        answear2=list[3]
        answear3=list[4]
        correct_answear=list[5]
        difficulty=list[6]
        new_question=Question(id,text,answear1,answear2,answear3,correct_answear,difficulty)
        return new_question


    def start_quiz(self,file_name):
        """
        Function to start the quiz
        :param file_name: the name of the file from where we will load the quiz
        """
        self.load_quiz(file_name)
        self.quiz_repo.sort(key= lambda question: question.get_difficulty)
        for question in self.quiz_repo:
            print("Question: " + question.get_text)
            print("Possible answears: "  + question.get_answear1 + " or " + question.get_answear2 + " or " + question.get_answear3 )
            user_answear=input("What do you choose? ")
            while user_answear !=question.get_answear1 and user_answear!= question.get_answear2 and user_answear!=question.get_answear3:
                print("ERROR: You can only choose from these!")
                print("Question: " + question.get_text)
                print("Possible answears: " + question.get_answear1 + " or " + question.get_answear2 + " or " + question.get_answear3)
                user_answear = input("What do you choose? ")
            if user_answear == question.get_correct_answear:
                print("Your answear is correct!" + "\n")
                if question.get_difficulty == "easy":
                    self.score +=1
                elif question.get_difficulty=="medium":
                    self.score+=2
                else:
                    self.score+=3
            else:
                print("Sorry , wrong answear! The correct one is: " + question.get_correct_answear + "\n")

        print("You finished the quiz! Your score is: " + str(self.score))


