class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.SCORE = 0


    def next_question(self):
        if self.question_number != len(self.question_list):
            self.new_question = self.question_list[self.question_number]
            self.question_number += 1
            return f"Q{self.question_number}: {self.new_question.question} \n(True/False): "
        else:
            return f"you have completed the quiz\nyour final score is {self.SCORE}/{self.question_number}"

    def pass_input(self, user_input ):
        if self.question_number != len(self.question_list):
            self.check_answer(user_input, self.new_question.answer)
        else:
            return f"you have completed the quiz\nyour final score is {self.SCORE}/{self.question_number}"



    def check_answer(self, user_input, question):
        if user_input.lower() == question.lower():
            self.SCORE += 1
            return "you are right."
        else:
            return f"you are wrong. \nThe correct answer is {question}"

