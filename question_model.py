#importa os dados das questoes
from cgitb import text
from data import question_data as qd
import random

#define a class question com parametros de texto e resposta
class Question:
    def __init__(self,text,answer):
        self.text = text
        self.answer = answer

    def getQuestion(self):
        self.text = random.choice(list(qd.values()))
        print(text)        




