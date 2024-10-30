from gui import UserInterface
from quiz_data import ques_data
from quiz_master import QuestionFormat, QuizMaster

ques_bank = []
for question in ques_data:
    question_text = question['question']
    answer_text = question['correct_answer']
    new_question = QuestionFormat(question_text, answer_text)
    ques_bank.append(new_question)

quizi = QuizMaster(ques_bank)
quiz_ui = UserInterface(quizi)
