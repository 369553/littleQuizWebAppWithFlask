class Question:
    def __init__(self, id, question, optA, optB, optC, optD, answer, explanation):
        self.id = id
        self.question = question
        self.optA = optA
        self.optB = optB
        self.optC = optC
        self.optD = optD
        self.answer = answer
        self.explanation = explanation
    
    def getId(self):
        return self.id
    def getQuestionText(self):
        return self.question

    def getOptionA(self):
        return self.optA
    
    def getOptionB(self):
        return self.optB
    
    def getOptionC(self):
        return self.optC
    
    def getOptionD(self):
        return self.optD
    
    def getAnswer(self):
        return self.getAnswer
    
    def getExplanation(self):
        if explanation is not None:
            return self.explanation
        else:
            return ""
    
    def __str__(self):
        return "Soru - " + str(self.id) + ": " + self.question