from tkinter import *
import requests


def kanye_click():
    response = requests.get(url = 'http://api.kanye.rest/')
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote, text = data['quote'])

win = Tk()
win.config(padx=30, pady=20)

canvas = Canvas(height=414, width = 300)
bkg = PhotoImage(file = 'background.png')
canvas.create_image(150, 207, image = bkg)
quote = canvas.create_text(150,190, width=200, font=('Arial',15,'italic','bold'))
canvas.grid(row = 0, column= 1)

kanye_click()

kanye = PhotoImage(file = 'kanye.png')
kanye_button = Button(image = kanye, highlightthickness=0, command=kanye_click)
kanye_button.grid(row=1, column=1)

win.mainloop()