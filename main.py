from quiz_brain import *
from question_model import Question
from data import question_data


questionBank = []

#roda nos dados e instancia um objeto para cada pergunta, resgatando o texto e a resposta dela 
for item in question_data:
    question = Question(item["text"],item["answer"])
    questionBank.append(question)

#instancia um objeto da classe QuizBrain passando como parametro a lista de questoes
quizBrain = QuizBrain(questionBank)

while quizBrain.still_has_questions():
    quizBrain.nextQuestion()
#chama o metodo para imprimir a questao
