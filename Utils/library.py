import sqlite3
import os


def initialise():
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
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
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO Issue(id_user, id_book, issue_date, return_date) 
    VALUES(?, ?, datetime('now','localtime'), NULL)''', (id_user, id_book,))

    cursor.execute('UPDATE Books SET copies_issued = copies_issued + 1 WHERE id = ?', (id_book,))

    connection.commit()
    connection.close()


def checkstock(item):
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()
    text = item.text()
    beg = text.find('<') + 5
    end = text.find('>')
    bookid = int(text[beg:end])

    cursor.execute('SELECT copies_issued, copies_total FROM Books WHERE id = ?', (bookid,))
    data = cursor.fetchone()

    connection.close()
    if data[0] == data[1]:
        return False
    else:
        return True


initialise()  # Makes sure the table is available
