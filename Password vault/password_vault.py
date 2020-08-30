import sqlite3


def db_create():
    create_user = ''' CREATE TABLE IF NOT EXISTS user(
                        user_id     TEXT PRIMARY KEY,
                        passcode    TEXT
                        );'''

    create_vault = ''' CREATE TABLE IF NOT EXISTS vault(
                        user_id      TEXT   PRIMARY KEY,
                        site         TEXT   NOT NULL,
                        password     TEXT   NOT NULL
                        );'''                    