from quiz_brain import *
from question_model import Question
from data import question_data

questionBank = []

#roda nos dados e instancia um objeto para cada pergunta, resgatando o texto e a resposta dela 
for item in question_data:
<<<<<<< HEAD
    question_text = item["question"]
    question_answer = item["correct_answer"]
    question = Question(question_text,question_answer)
=======
    question = Question(item["question"],item["correct_answer"])
>>>>>>> e4516bcaf93d76cf427cb3d4383ba28da0abafaa
    questionBank.append(question)

#instancia um objeto da classe QuizBrain passando como parametro a lista de questoes
quizBrain = QuizBrain(questionBank)

#loop para continuar imprimindo questões até acabar e fica checando as respostas dos 
while quizBrain.still_has_questions() == True:
    quizBrain.nextQuestion()
    print("\n")

if quizBrain.still_has_questions() == False:
    print("Congratulations! You've completed the quiz!")
    print(f"Your final score was {quizBrain.score} / 12")    

