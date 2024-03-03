from random import randint

class Sentence_repo:

    def __init__(self, file_name):
        self._file_name=file_name
        self.sentence_repo=[]
        self._load_file()

    def _load_file(self):
        try:
            file = open(self._file_name, "r")
        except IOError:
            raise ValueError("Error! File not found!")
        line = file.readline().strip()
        while line != "":
            self.sentence_repo.append(line)
            line = file.readline().strip()
        file.close()

    def _save_file(self):
        file = open(self._file_name, "w")
        for sentence in self.sentence_repo:
            file.write(sentence + "\n")
        file.close()

    def add_sentence(self, new_sentence):
        """
        The function gets a sentence, it checks that it follows the criteria and adds it to the repository if it does,
        or raises an exception otherwise
        :param new_sentence: the sentence to be added to the repository
        :return:
        """
        copy_of_sentence=new_sentence.strip()
        list_of_words=copy_of_sentence.split()
        if len(list_of_words) == 0:
            raise IndexError("The sentence should have at least a word!")

        for word in list_of_words:
            number_of_letters=0
            for letter in word:
                number_of_letters+=1
                if number_of_letters >=3:
                    break
            if number_of_letters <3:
                raise IndexError("The sentence is incorrect!")
        for sentence in range(0,len(self.sentence_repo)):
            if self.sentence_repo ==  new_sentence:
               raise IndexError("The sentence you are trying to add to the repository already exists!")
            else:
                self.sentence_repo.append(new_sentence)
                self._save_file()
                return True

    def choose_sentence(self):
        """
        The programm choses random a sentence from the list of sentences by getting a random number and selecting
        the sentence with that particullar index
        """
        sentence_number= randint(0,len(self.sentence_repo)-1)
        sentence= self.sentence_repo[sentence_number]
        sentence=sentence.split()
        return sentence




