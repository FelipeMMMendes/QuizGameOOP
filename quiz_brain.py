#essa classe tem como objetivo controlar a lógica por trás da execução do quiz,
#exercendo funcoes como checar a resposta, puxar a proxima pergunta, etc

class QuizBrain:
    def __init__(self,questList):
        self.questNumber = 0
        self.questList = questList
        self.score = 0

    def still_has_questions(self):
        return self.questNumber < len(self.questList)
        #ou poderia ser:
        #  return False
        #else:
        #  return True      

    def nextQuestion(self):
        currentQuestion = self.questList[self.questNumber]
        self.questNumber += 1
        userAnswer = input(f"Q.{self.questNumber}: {currentQuestion.text} (True/False): ")
        self.checkAnswer(userAnswer,currentQuestion.answer)

    def checkAnswer(self,UserAnswer,RightAnswer):
        if UserAnswer.lower() == RightAnswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The right answer was {RightAnswer}")    
        print(f"Your current score is {self.score}/{self.questNumber}")
                



