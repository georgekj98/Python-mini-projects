from tkinter import *
from tkinter import messagebox
from password_vault_db import Database


db = Database('vault_trial.db')

def login(user_id):
    log = Tk()
    
    website_text = StringVar()
    website_label = Label(log, text = 'Website', pady = 20, padx = 15)
    website_label.grid(row = 0, column = 0)
    website_entry = Entry(log, textvariable = website_text)
    website_entry.grid(row = 0, column = 1, padx = 10)

    password_text = StringVar()
    password_label = Label(log, text = 'Password', padx = 15)
    password_label.grid(row = 0, column = 2)
    password_entry = Entry(log, textvariable = password_text)
    password_entry.grid(row = 0, column = 3, padx = 10)

    add_button = Button(log, text = "Add", command = lambda : db.new_entry(user_id, website_entry.get(), password_entry.get()), width = 17)
    add_button.grid(row = 2, column = 1, pady = 20)

    remove_button = Button(log, text = "Remove", command = lambda : db.remove_entry(user_id, website_entry.get(), password_entry.get()), width = 17)
    remove_button.grid(row = 2, column = 2, pady = 20)

    update_button = Button(log, text = "Update", command = lambda : db.update_site_password(user_id, website_entry.get(), password_entry.get()), width = 17)
    update_button.grid(row = 2, column = 3, pady = 20)





    log.geometry("500x400")
    log.mainloop()


def login_check():

    user_id = user_id_entry.get()
    passcode = passcode_entry.get()
    passcode_entry.delete(0, END)
    passcode_entry.insert(END,"*" * len(passcode))
    check_user = db.user_id_query(user_id)
    if check_user:
        if check_user[0][1] == passcode:
            login(user_id)
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