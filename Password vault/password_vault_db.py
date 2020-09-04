import sqlite3


class Database:
    def __init__(self,db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
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
        self.cursor.execute(create_user)
        self.cursor.execute(create_vault)
        self.connection.commit()

    def check_NULL(self, test):
        if "" in test:
            return False
        else:
            return True


    def new_user(self, user_id, pwd):
        if self.check_NULL((user_id, pwd)):
            new_user_query = "INSERT INTO user VALUES(?,?)"
            self.cursor.execute(new_user_query, (user_id, pwd))
            self.connection.commit()


    def new_entry(self, user_id, site, password):
        if self.check_NULL((user_id, site, password)):
            check_query = f"SELECT site FROM vault WHERE user_id = '{user_id}'"
            all_pwds = self.cursor.execute(check_query)
            if (site,) not in all_pwds.fetchall():
                new_entry_query = "INSERT INTO vault VALUES(?,?,?)"
                self.cursor.execute(new_entry_query, (user_id, site, password))
                self.connection.commit()
    

    def remove_entry(self, user_id, del_site, del_password):
        if self.check_NULL((user_id, del_site, del_password)):
            del_site_query = f"DELETE FROM vault WHERE user_id ='{user_id}' AND site ='{del_site}'"
            self.cursor.execute(del_site_query)
            self.connection.commit()


    def remove_user(self, remove_user_id):
        if self.check_NULL((remove_user_id,)):
            del_user_query = f"DELETE FROM user WHERE user_id ='{remove_user_id}'"
            del_vault_query = f"DELETE FROM vault WHERE user_id ='{remove_user_id}'"
            self.cursor.execute(del_user_query)
            self.cursor.execute(del_vault_query)
            self.connection.commit()


    def update_user_passcode(self, update_user, update_pwd):
        if self.check_NULL((update_user, update_pwd)):
            update_user_query = f"UPDATE user SET passcode ='{update_pwd}' WHERE user_id ='{update_user}'"
            self.cursor.execute(update_user_query)
            self.connection.commit()


    def update_site_password(self, update_user_id, update_site, new_password):
        if self.check_NULL((update_user_id, update_site, new_password)):
            update_site_query = f"UPDATE vault set password ='{new_password}' WHERE user_id = '{update_user_id}' AND site ='{update_site}'"
            self.cursor.execute(update_site_query)
            self.connection.commit()


    def user_vault_query(self,fetch_user_id):
        if self.check_NULL((fetch_user_id,)):
            ret = f"SELECT * FROM vault WHERE user_id ='{fetch_user_id}'"
            data = self.cursor.execute(ret)
            return data.fetchall()
    

    def user_id_query(self, fetch_user_id):
        if self.check_NULL((fetch_user_id,)):
            ret = f"SELECT * FROM user WHERE user_id ='{fetch_user_id}'"
            data = self.cursor.execute(ret)
            return data.fetchall()
    

    def __del__(self):
        self.connection.close()

#db = Database('vault_trial.db')
#db.new_user("george", "mypass")
#print(db.user_vault_query("george"))
