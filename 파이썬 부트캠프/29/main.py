from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letter =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol =  ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


def passwork_generator():
    password_entry.delete(0, END)
    letters = [choice(letter) for _ in range(randint(8,10))]
    nums = [choice(num) for _ in range(randint(2,4))]
    symbols = [choice(symbol) for _ in range(randint(2,4))]

    password_list = letters + nums + symbols 

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    user_id = user_id_entry.get()
    password = password_entry.get()

    website_entry.delete(0, END)
    user_id_entry.delete(0, END)
    password_entry.delete(0, END)
    


    if not (website and password):
        messagebox.showinfo(title="Oops", message="Please don't any field empty!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details enterd: \nEmail: {user_id} \n "
                                               f"Password: {password} \nIs it ok to save?")
    
    
    if is_ok:
        with open("./29/dataset.text", 'a') as file:
            file.write('\n')
            file.write(f"{website}/{user_id}/{password}")


# ---------------------------- UI SETUP ------------------------------- #





window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)




canvas = Canvas(height=200, width=200)
MyPass_img = PhotoImage(file="./29/logo.png")
canvas.create_image(100, 100, image=MyPass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_id_label = Label(text="Email/Username:")
user_id_label.grid(column=0, row=2)

user_id_entry = Entry(width=35)
user_id_entry.grid(column=1, row=2, columnspan=2)
user_id_entry.insert(0, "dlwnsgh@naver.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

g_password_button = Button(text="Generate Password", command=passwork_generator)
g_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
