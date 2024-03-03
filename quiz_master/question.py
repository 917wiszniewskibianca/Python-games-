class Question:
    def __init__(self,id,text,answear1,answear2,answear3,correct_answear,difficulty):
        self._id=id
        self.text=text
        self.answear1=answear1
        self.answear2=answear2
        self.answear3=answear3
        self.correct_answear=correct_answear
        self.difficulty=difficulty

    @property
    def get_id(self):
        return self._id
    @property
    def get_text(self):
        return self.text
    @property
    def get_answear1(self):
        return self.answear1
    @property
    def get_answear2(self):
        return self.answear2
    @property
    def get_answear3(self):
        return self.answear3
    @property
    def get_correct_answear(self):
        return self.correct_answear
    @property
    def get_difficulty(self):
        return self.difficulty
