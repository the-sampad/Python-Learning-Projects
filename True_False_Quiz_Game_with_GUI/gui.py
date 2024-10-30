from tkinter import *

from quiz_master import QuizMaster

THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self, quizmaster : QuizMaster):
        self.quiz = quizmaster
        
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=30, pady=30, bg= THEME_COLOR)

        self.score_label = Label(text="Score : 0", fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=300, width=300, bg= 'white')
        self.question_text = self.canvas.create_text(150, 150, width=280, fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file = 'images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2,column=0)

        false_image = PhotoImage(file = 'images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.new_question()

        self.window.mainloop()
    
    def new_question(self) -> None:
        self.canvas.config(bg="white")
        if self.quiz.ques_left():
            self.score_label.config(text=f'Score = {self.quiz.score}')
            ques_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = ques_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "This is the end of the quiz")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self) -> None:
        self.feedback(self.quiz.check_answer('True'))
    
    def false_pressed(self) -> None:
        correct = self.quiz.check_answer('False')
        self.feedback(correct)
    
    def feedback(self,correct: bool) -> None:
        if correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.new_question)
    