# Agregar que el usuario pueda poner los tiempos de work, break y long break
from math import floor
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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  global reps
  canvas.itemconfig(timer_text, text="00:00")
  
  windows.after_cancel(timer)
  timer_label.config(text="Timer", width=11,fg=GREEN, bg= YELLOW, font= (FONT_NAME, 35, "bold"))

  checkmark_label.config(text="")
  start_button.config(state="normal")
  reps = 0
  

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  reps += 1
  start_button.config(state="disabled")
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60
  
  if reps % 2 == 0:
      if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
        reps = 0
      else: 
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
        
  else:
      count_down(work_sec)
      timer_label.config(text="Work", fg=GREEN)

# ---------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
  global timer
  count_min = floor(count / 60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  
  canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    timer = windows.after(1000, count_down, count - 1)
  else:
    start_timer()
    marks = []
    work_sessions = floor(reps/2)
    for _ in range(work_sessions):
      marks.append("✓")
    checkmark_label.config(text=marks)
  
# ---------------------------- UI SETUP ------------------------------- #

# window
windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)

# canva
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodor_ing = PhotoImage(file="images/tomato.png")
canvas.create_image(100, 112, image=pomodor_ing)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME,
35, "bold"))
canvas.grid(column=1, row=1)



#Label
timer_label = Label(text="Timer", width=11,fg=GREEN, bg= YELLOW, font= (FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg= YELLOW, font= (FONT_NAME, 24, "normal"))
checkmark_label.grid(column=1, row=3)

# Button
start_button = Button(text="Start", font=FONT_NAME, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=FONT_NAME, command=reset_timer)
reset_button.grid(column=2, row=2)




windows.mainloop()