# 클래스를 이용한 퀴즈 

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data :
    question_bank.append(Question(i["question"],i["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question() :
  quiz.next_question()
  quiz.check_answer(quiz.answer,quiz.question_list[quiz.question_number].A)
     
