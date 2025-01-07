import tkinter as tk  # tk는 파이썬 문법과 다름름

window = tk.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label

my_label = tk.Label(text="I Am a Label", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# tk.label에서 **kwargs 변경 
my_label["text"] = "New Text" 
my_label.config(text="New text")

# 버튼

def button_clicked():
    user_input = input.get()
    my_label["text"] = user_input



button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


# ENTRY 

input = tk.Entry(width=10)
input.grid(column=5, row=2)
print(input.get())


button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=0)

        

 












window.mainloop()

