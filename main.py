import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer_id = None

from tkinter import *


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer_id)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps  = reps + 1
    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    #1, 3, 5, 7 => 25 minutes
    #2,4,6, => 5 minutes break
    #8th => long break

    if reps % 8 == 0:
        title_label.config(text="Long Break", fg=RED)
        count_down(long_break_secs)
    elif reps % 2 == 1:
        title_label.config(text="Focus", fg=GREEN)
        count_down(work_sec)
    else:
        title_label.config(text="Short Break", fg=PINK)
        count_down(short_break_secs)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer_id
    minutes = math.floor(count / 60)
    seconds = count % 60

    if minutes <= 9:
        minutes = f"0{minutes}"
    
    if seconds <= 9:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if(count > 0):
        timer_id = window.after(1000, count_down, count - 1)
    else:
        sessions_count = reps // 2
        check_marks.config(text=sessions_count * "✔️")
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

resest_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
resest_button.grid(row=2, column=2)



check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
