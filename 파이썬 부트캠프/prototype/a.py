from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)



canvas = Canvas(height=200, width=200)
MyPass_img = PhotoImage(file="./29/logo.png")
canvas.create_image(100, 100, image=MyPass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky='ew')
website_entry.focus()

user_id_label = Label(text="Email/Username:")
user_id_label.grid(column=0)

user_id_entry = Entry(width=35)
user_id_entry.grid(column=1, row=2, columnspan=2, sticky='ew')

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='ew')

g_password_button = Button(text="Generate Password")
g_password_button.grid(row=3, column=2, sticky='ew')

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky='ew')

window.mainloop()