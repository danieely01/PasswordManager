import tkinter
from tkinter import messagebox
import pyperclip
import random
#--------------GENERATE PASSWORD--------------------------#
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def password_button_clicked():
    rn_letters = random.randint(8, 10)
    rn_symbols = random.randint(2, 4)
    rn_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(rn_letters)]
    password_symbols = [random.choice(letters) for item in range(rn_symbols)]
    password_numbers = [random.choice(letters) for item in range(rn_numbers)]

    password_list = password_numbers + password_letters + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    entry3.delete(0, tkinter.END)
    entry3.insert(0, password)
    pyperclip.copy(password)

#------------- SAVE PASSWORD-----------------------------------------------#

def add_button_clicked():
    website = entry1.get()
    email_or_username = entry2.get()
    password = entry3.get()
    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        answer = messagebox.askokcancel(title="Are you sure?", message=f"Website: {website}\n Email/Username: {email_or_username}\n Password: {password}\nIs it okay to save?")
        if answer:
            with open("Password Manager.txt", "a") as f:
                f.write(f"{website} | {email_or_username} | {password}\n")
                f.close()
                entry1.delete(0, tkinter.END)
                entry3.delete(0, tkinter.END)



#-----------------------------UI SETUP--------------------------#
window = tkinter.Tk()
window.minsize(400,400)
window.title("Password Manager")
window.config(padx=20, pady=20)

#Canvas
canvas = tkinter.Canvas()
canvas.config(width=200, height=200)
pic = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=pic)
canvas.grid(column=1, row=0)


#Labels
label1 = tkinter.Label(text="Website:")
label1.grid(column=0, row=1)

label2 = tkinter.Label(text="Email/Username:")
label2.grid(column=0, row=2)

label3 = tkinter.Label(text="Password:")
label3.grid(column=0, row=3)


#Entries

entry1 = tkinter.Entry(width=52)
entry1.grid(column=1, row=1, columnspan=2)
entry1.focus()

entry2 = tkinter.Entry(width=52)
entry2.grid(column=1, row=2, columnspan=2)
entry2.insert(0, "example@gmail.com")

entry3 = tkinter.Entry(width=33)
entry3.grid(column=1, row=3)

#Buttons

button1 = tkinter.Button(text="Generate Password", command=password_button_clicked)
button1.grid(column=2, row=3)

button2 = tkinter.Button(width=44, text="Add", command=add_button_clicked)
button2.grid(column=1, row=4, columnspan=2)

window.mainloop()