import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_no = 0
        self.score = 0
        self.current_question = None

    def ask_question(self):
        self.current_question = self.question_list[self.question_no]
        self.question_no += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_no}: {q_text} \nTrue or False?"

    def check_answer(self, user_answer: str) -> bool:
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        return False

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

    def get_score(self):
        return self.score
