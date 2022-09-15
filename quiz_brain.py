#essa classe tem como objetivo controlar a lógica por trás da execução do quiz,
#exercendo funcoes como checar a resposta, puxar a proxima pergunta, etc

class QuizBrain:
    def __init__(self,questList):
        self.questNumber = 0
        self.questList = questList

    def still_has_questions(self):
        return self.questNumber < len(self.questList)
        #ou poderia ser:
        #  return False
        #else:
        #  return True      

    def nextQuestion(self):
        currentQuestion = self.questList[self.questNumber]
        self.questNumber += 1
        input(f"Q.{self.questNumber}: {currentQuestion.text} (True/False): ")

