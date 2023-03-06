from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from tkinter import *
question_bank = []

for value in question_data:
    new_question = Question(value["text"],value["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

def true():
    quiz.pass_input("true")
    canve.itemconfig(text2, text=f"Result: {quiz.SCORE}/{quiz.question_number}")
    canve.itemconfig(text,text=quiz.next_question())

def false():
    quiz.pass_input("false")
    canve.itemconfig(text2, text=f"Result: {quiz.SCORE}/{quiz.question_number}")
    canve.itemconfig(text,text=quiz.next_question())

def game():
    global text, text2
    canve.create_image(174,128, image=bg)
    text = canve.create_text(163,50, text=quiz.next_question(), justify=CENTER, fill="#ffffff",
        font=("Arial Rounded MT Bold",10))
    text2 = canve.create_text(293, 160, text=f"Result: {quiz.SCORE}/{quiz.question_number}", justify=CENTER, fill="#ffffff",
        font=("Arial Rounded MT Bold", 10))

    t = Button(canve,image=tu, border=0, bg="#011f6e", command=true)
    t.place(x=18,y=192)
    f = Button(canve,image=fs, border=0, bg="#011f6e", command=false)
    f.place(x=270, y=192)

home = Tk()
home.geometry("352x230")
bg = PhotoImage(file="image/background.png")
fs = PhotoImage(file="image/false.png")
tu = PhotoImage(file="image/true.png")
canve = Canvas(width=352, height=230)
canve.place(x=-2,y=-1)
game()
home.mainloop()

