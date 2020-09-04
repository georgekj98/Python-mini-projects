from tkinter import *
from tkinter import messagebox
from password_vault_db import Database


db = Database('vault_trial.db')

def login():
    log = Tk()
    log.mainloop()


def login_check():
    user_id = user_id_entry.get()
    passcode = passcode_entry.get()
    check_user = db.user_id_query(user_id)
    print(check_user)
    if check_user:
        if check_user[0][1] == passcode:
            login()
    else:
        print("Doesnt exist or wrong")
    print(user_id)
    print(passcode)
    passcode_entry.delete(0, END)
    passcode_entry.insert(END,"*" * len(passcode))


def sign_up_check():
    print("Sign up check function")


app = Tk()

user_id_text = StringVar()
user_id_label = Label(app, text = 'User ID', pady = 20, padx = 15)
user_id_label.grid(row = 0, column = 0)
user_id_entry = Entry(app, textvariable = user_id_text)
user_id_entry.grid(row = 0, column = 1, padx = 10)

passcode_text = StringVar()
passcode_label = Label(app, text = 'Passcode', padx = 15)
passcode_label.grid(row = 1, column = 0)
passcode_entry = Entry(app, textvariable = passcode_text)
passcode_entry.grid(row = 1, column = 1, padx = 10)

login_button = Button(app, text = "Login", command = login_check, width = 17)
login_button.grid(row = 2, column = 1, pady = 20)

sign_up_button = Button(app, text = "Sign up", command = sign_up_check, width = 17)
sign_up_button.grid(row = 3, column = 1)

app.title("Password vault")
app.geometry('250x200')
app.mainloop()