import sqlite3

def db_connection():
    connection = sqlite3.connect('vault_trial.s3db')
    cursor = connection.cursor()


def db_create():
    create_user = ''' CREATE TABLE IF NOT EXISTS user(
                        user_id     TEXT PRIMARY KEY,
                        passcode    TEXT
                        );'''

    create_vault = ''' CREATE TABLE IF NOT EXISTS vault(
                        user_id      TEXT   NOT NULL,
                        site         TEXT   NOT NULL,
                        password     TEXT   NOT NULL,
                        FOREIGN KEY (user_id) 
                            REFERENCES user (user_id)
                        );'''  
    cursor.execute(create_user)
    cursor.execute(create_vault)
    connection.commit()


def new_user(user_id, pwd):
    new_user_query = "INSERT INTO user VALUES(?,?)"
    cursor.execute(new_user_query, (user_id, pwd))
    connection.commit()


def new_entry(user_id, site, password):
    new_entry_query = "INSERT INTO vault VALUES(?,?,?)"
    cursor.execute(new_entry_query, (user_id, site, password))
    connection.commit()


def remove_entry(user_id, del_site):
    del_site_query = f"DELETE FROM vault WHERE user_id ='{user_id}' AND site ='{del_site}'"
    cursor.execute(del_site_query)
    connection.commit()


def update_user(update_user, update_pwd):
    update_user_query = f"UPDATE user SET password = {update_pwd} WHERE user_id = {update_user}"
    cursor.execute(update_user_query)
    connection.commit()


def db_full_query():
    ret = 'SELECT * FROM user JOIN vault ON user.user_id = vault.user_id'
    data = cursor.execute(ret)
    print(data.fetchall())


def main():
    
    #db_connection()
    connection = sqlite3.connect('vault_trial.s3db')
    cursor = connection.cursor()
    db_create()
    choice = 123
    while(choice != 0):
        ch_1 = input("PASSWORD VAULT\nENTER CHOICE\n1. Login\n2. Sign up\n3. Exit")
        if ch_1 == '3':
            break
        elif ch_1 == '1':
            print("call login functions")
        elif ch_1 == '2':
            user_id = input("Enter the new user id")
            passcode = input("Enter new passcode")
            new_user(user_id,passcode)
            db_full_query()
        else:
            print("Error input choice")

if __name__ == "__main__":
    main()