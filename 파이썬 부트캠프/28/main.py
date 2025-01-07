from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
r = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
   global r
   window.after_cancel(timer)
   r = 0
   canvas.itemconfig(timer_text, text=f"00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count = 10):
    global timer
    count_min = floor(count/ 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    


    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
       start_timer()
       mark = ""
       work_sessions = floor(r/2)
       for _ in range(work_sessions):
          mark += "c"
       check_label.config(text=mark)

def start_timer():
    global r 
    r += 1

    

    if r % 8 == 0:
     timer_label.config(fg=RED)
     count_down(LONG_BREAK_MIN * 60)
    elif r % 2 == 0:
     timer_label.config(fg=RED)
     count_down(SHORT_BREAK_MIN * 60)
    else :
       timer_label.config(fg=GREEN)
       count_down(10)
       
       
       

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# def say_something(thing): 
#     print(thing)

# window.after(1000, say_something, "Hello")


tomato_img = PhotoImage(file="./28/tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)




timer_label = Label(text="Timer",font=(FONT_NAME, 50), bg =YELLOW, fg =GREEN)
timer_label.grid(column=1, row=0)




start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_label = Label( bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)





window.mainloop()

