import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps= 0
timer = None

# -------------------------------- CODE ----------------------------------#


def reset_button_click():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = math.floor(count%60)
    
    if count_min<10:
        count_min = f"0{count_min}"
    if count_sec<10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    if count>0:
        global timer
        timer = window.after(1000,countdown,count-1)
    else:
        start_button_click()
        checkmarks = ""
        work_cycles = math.floor(reps/2)
        for _ in range(work_cycles):
            checkmarks+="✔️"
        check_mark.config(text=checkmarks)


def start_button_click():
    global reps
    reps+=1

    if reps%8==0:
        countdown(LONG_BREAK_MIN*60)
        title.config(text="Break", fg=RED)
    elif reps%2==0:
        countdown(SHORT_BREAK_MIN*60)
        title.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN*60)
        title.config(text="Work", fg=GREEN)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW, highlightthickness=0 )

title = Label(text="Timer", fg = GREEN, bg=YELLOW, font=(FONT_NAME,40))
title.grid(row=0, column=1)

canvas = Canvas(width = 224, height = 224, bg=YELLOW, highlightthickness=0)

tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_png)

timer_text = canvas.create_text(100, 130, text = "00.00", font=(FONT_NAME, 30, "bold"), fill="White")
canvas.grid(row=1,column=1)

start_button = Button(text="Start", command=start_button_click)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_button_click)
reset_button.grid(row=2, column=2)

check_mark = Label(fg="green", bg=YELLOW)
check_mark.grid(row=3, column=1)


window.mainloop()