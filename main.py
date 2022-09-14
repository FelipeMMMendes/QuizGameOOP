from cgitb import text
from question_model import Question
from data import question_data


questionBank = []

#roda nos dados e instancia um objeto para cada pergunta, resgatando o texto e a resposta dela 
for item in question_data:
    question = Question(item["text"],item["answer"])
    questionBank.append(question)

