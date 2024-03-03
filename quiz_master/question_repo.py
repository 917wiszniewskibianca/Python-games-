from question import Question
class question_repo:
    def __init__(self,file_name):
        self.question_repo=[]
        self.file_name=file_name

    def load_questions(self):
        """
        Function to read the questions from the file and place them in repository
        """
        try:
            file=open(self.file_name,"r")
        except IOError:
            raise ValueError("The file could not be opened!")
        line=file.readline()
        while line!="":
            new_question=self.transform_line(line)
            self.question_repo.append(new_question)
            line=file.readline()
        file.close()

    def transform_line(self,line):
        """
        Function to transform the line in a type Question
        :param line: the line read from file
        :return: the new question
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

    def save_file(self):
        """
        Function to save the question repository to a file
        :return:
        """
        try:
            file = open(self.file_name, "w")
        except IOError:
            raise ValueError("The file can not be opened!")
        for question in self.question_repo:
            sentence = ""
            sentence += question.get_id + ";" + question.get_text + ";" + question.get_answear1 + ";" + question.get_answear2 + ";" + question.get_answear3 + ";" + question.get_correct_answear + ";" + question.get_difficulty
            file.write(sentence + "\n")
        file.close()

    def add_question(self,line):
        """
        Function to add a question to the repository
        :param line:
        :return:
        """
        new_question=self.transform_line(line)
        self.question_repo.append(new_question)
        self.save_file()

    def return_quiz_repo(self,difficulty,number_of_questions):
        """
        Function to create a new quiz which respects the given restrictions
        :param difficulty: the difficulty of the quiz
        :param number_of_questions: the number of questions in the quiz
        :return: the list of questions
        """
        list_of_questions=[]
        number_of_selected_questions=0
        if int(number_of_questions ) %2 == 0 :
         for question in self.question_repo :
          if int(number_of_selected_questions) < int(number_of_questions)//2:
            if question.get_difficulty == difficulty:
                list_of_questions.append(question)
                number_of_selected_questions+=1
        else:
            for question in self.question_repo :
             if int(number_of_selected_questions) < int(number_of_questions)//2:
                if question.get_difficulty == difficulty:
                    list_of_questions.append(question)
                    number_of_selected_questions += 1

        for question in self.question_repo:
            if question.get_difficulty != difficulty and int(number_of_selected_questions) < int(number_of_questions):
                list_of_questions.append(question)
                number_of_selected_questions += 1

        list_of_questions.sort(key= lambda question: question.get_difficulty[len(question.get_difficulty)-1] , reverse=True)
        return list_of_questions

    def can_create_quiz(self,difficulty,number_of_questions):
        """
        Function to check if a quiz with the given criteria can be created
        :param difficulty: the difficulty of the quiz
        :param number_of_questions: the number of questions in the quiz
        :return: true if the quiz can be created and false otherwise
        """
        if self.check_difficulty_and_number_of_questions_is_correct(difficulty,number_of_questions):
            return True
        else:
            return False

    def check_difficulty_and_number_of_questions_is_correct(self,difficulty,number_of_questions):
        """
        Function to check if the questions repo has enough number of questions for the new quiz and enough questions with the given difficulty
        :param difficulty: the difficulty of the quiz
        :param number_of_questions: the number of questions in the quiz
        :return: true if the question repo has enough qurstions to create the quiz and false otherwise
        """
        number_of_difficulty_questions=0
        if len(self.question_repo) < int(number_of_questions):
            return False
        else:
          for question in self.question_repo:
            if question.get_difficulty == difficulty:
                number_of_difficulty_questions+=1

          if number_of_difficulty_questions < len(number_of_questions)/2:
              print(number_of_difficulty_questions)
              return False
          else:
             return True
