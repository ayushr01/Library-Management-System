import sqlite3
import os


def initialise():
    connection = sqlite3.connect(os.path.realpath('../Files/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Issue(
    id_user INTEGER NOT NULL,
    id_book INTEGER NOT NULL,
    issue_date TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY(id_user) REFERENCES Members(id),
    FOREIGN KEY(id_book) REFERENCES Books(id)
    )
    ''')

    connection.commit()
    connection.close()


def insert(id_user, id_book):
    connection = sqlite3.connect(os.path.realpath('../Files/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    try:
        cursor.execute('''
        INSERT INTO Issue(id_user, id_book, issue_date, return_date) 
        VALUES(?, ?, datetime('now','localtime'), NULL)''', (id_user, id_book,))
    except sqlite3.IntegrityError:
        print('FOREIGN KEY ERROR!')

    connection.commit()
    connection.close()


# TODO: REMOVE THESE AFTER YOU ARE DONE
initialise()
insert(1, 1)
