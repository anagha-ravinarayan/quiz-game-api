from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()

        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_board = Label(text=f"Score: {0}", font=("Arial", 16, "bold"), fg="white", highlightthickness=0, bg=THEME_COLOR)
        self.score_board.grid(row=0, column=0, columnspan=2)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Hey there", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=lambda: self.on_press("true"))
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=lambda: self.on_press("false"))
        self.false_button.grid(row=2, column=1)

        self.ask_question()

        self.window.mainloop()

    def ask_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.ask_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. Your final score is {self.quiz.get_score()}.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def on_press(self, user_answer):
        timer = None
        if timer is not None:
            self.window.after_cancel(timer)

        is_right = self.quiz.check_answer(user_answer)
        if is_right:
            self.update_score_board()
        self.give_feedback(is_right)

        timer = self.window.after(1000, self.ask_question)

    def update_score_board(self):
        self.score_board.config(text=f"Score: {self.quiz.get_score()}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
