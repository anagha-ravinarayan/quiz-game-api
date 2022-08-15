from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for q in question_data:
    question = Question(q["question"], q["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz_brain=quiz)
