from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text=f'Score: {self.quiz.score}')
        self.score_label.config(bg=THEME_COLOR, fg='white', font=('Arial', 18, 'normal'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg='white')
        self.canvas_text = self.canvas.create_text(150, 125, text='Jakie pytanie wariacie?', fill='black',
                                                   width=200, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.false_img = PhotoImage(file='.\\images\\false.png')
        self.false_btn = Button(image=self.false_img, command=self.false_pressed)
        self.false_btn.grid(row=2, column=1, padx=20, pady=20)

        self.true_img = PhotoImage(file='.\\images\\true.png')
        self.true_btn = Button(image=self.true_img, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0, padx=20, pady=20)

        self.update_question()

        self.window.mainloop()

    def update_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz!")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.update_question)
