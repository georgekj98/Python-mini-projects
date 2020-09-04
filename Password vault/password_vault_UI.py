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
    passcode_entry.delete(0, END)
    passcode_entry.insert(END,"*" * len(passcode))
    check_user = db.user_id_query(user_id)
    if check_user:
        if check_user[0][1] == passcode:
            login()
        else:
            messagebox.showerror(title="Error",message= "Password is wrong")
            passcode_entry.delete(0, END)
            return
    else:
        messagebox.showerror(title="Error",message= "User Id doesn't exist")
        passcode_entry.delete(0, END)
        return
    

def sign_up_check():
    
    user_id = user_id_entry.get()
    passcode = passcode_entry.get()
    check_user = db.user_id_query(user_id)
    if check_user:
        messagebox.showerror(title="Error",message= "User Id already exists")
        return
    else:
        db.new_user(user_id, passcode)
        messagebox.showinfo(title="Password vault", message=f"New User_Id : {user_id} successfully created")
        passcode_entry.delete(0, END)
        return




if __name__ == "__main__":   
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