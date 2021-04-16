from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_counter = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_counter.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Testtesttesttest", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_button_icon = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_icon, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        false_button_icon = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_icon, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!", fill=THEME_COLOR)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)



    def answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, fill="white")
            self.score_counter.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, fill="white")

        self.window.after(1000, self.get_next_question)
