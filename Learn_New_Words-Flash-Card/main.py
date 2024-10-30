BACKGROUND_COLOR = "#B1DDC6"

import random
from tkinter import *
import pandas

try:
    data = pandas.read_csv('data/french_words_not_remembered.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words_copy.csv')
    not_remembered = data.to_dict(orient='records')
else:
    not_remembered = data.to_dict(orient='records')

win = Tk()
win.config(padx=50, pady=30, bg=BACKGROUND_COLOR )
win.title('Flashy')

card = random.choice(not_remembered)

def next_image():
    global card
    card = random.choice(not_remembered)
    canvas.itemconfig(card_card, image = card_front)
    canvas.itemconfig(language, text = 'FRENCH')
    canvas.itemconfig(word, text = card['French'])
    
    
    
def flip_image():
    global card
    canvas.itemconfig(card_card, image = card_back)
    canvas.itemconfig(language, text = 'ENGLISH')
    canvas.itemconfig(word, text = card['English'])
    flip_it = win.after(3000, func=next_image)

def known():
    global card
    not_remembered.remove(card)
    dats = pandas.DataFrame(not_remembered)
    dats.to_csv('data/french_words_not_remembered.csv')
    next_image()


canvas = Canvas(width=800, height=650,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file = 'images/card_front.png')
card_back = PhotoImage(file = 'images/card_back.png')
card_card = canvas.create_image(400,280,image=card_front)
language = canvas.create_text(400,100, text = 'FRENCH', font=('Calibri', 20, 'italic','bold'))
word = canvas.create_text(400,250,text =card['French'], font=('Arial',45,'bold'))
canvas.grid(row=0,column=0, columnspan=3)


right = PhotoImage(file = 'images/right.png')
wrong = PhotoImage(file = 'images/wrong.png')
nextimage = Button(image=right, highlightthickness=0, command=known)
nextimage.grid(row=1, column=2)
flipimage = Button(image=wrong, highlightthickness=0, command=flip_image)
flipimage.grid(row=1, column=0)


win.mainloop()