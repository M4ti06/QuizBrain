class QuizBrain:

    def __init__(self, list_of_questions):
        self.question_number = 0
        self.questions = list_of_questions
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.questions):
            return True
        else:
            return False

    def next_question(self):
        question_obj = self.questions[self.question_number]
        question_txt = question_obj.text
        question_ans = question_obj.answer
        self.question_number += 1
        users_answer = input(f"Q {self.question_number} {question_txt}. Type 'true' or 'false': ")
        self.check_answer(users_answer, question_ans)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
        print("\n")
