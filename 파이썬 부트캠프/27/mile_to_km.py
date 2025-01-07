from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


m_entry = Entry(width=7)
m_entry.grid(column=1,row=0)

m_label = Label(text="Miles", font=("Arial", 12))
m_label.grid(column=2, row=0)
m_label.config()

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

k_v_label = Label(text="0")
k_v_label.grid(column=1, row=1)


k_label = Label(text="Km")
k_label.grid(column=2, row=1)

def calculate():
    miles = int(m_entry.get())
    km = miles*1.609344
    k_v_label["text"] = str(km)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()