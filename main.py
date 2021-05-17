from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data :
    question_text=question["text"]
    question_answer=question["answer"]
    new_questions=Question(question_text,question_answer)
    question_bank.append(new_questions)

quiz=QuizBrain(question_bank)
while quiz.still_has_question() :
    quiz.next_question()

print(f"You have the completed the quiz {quiz.question_score}/{question_bank}")
