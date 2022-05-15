import os
import re
import sqlite3

from UI.foldermaker import home


def initialise():
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Members(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL,
    DOB TEXT NOT NULL,
    reg TEXT NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


def namecheck(name):
    validate = re.search("^[A-Z][a-z]+\s[A-Z][a-z]+$", name)
    if validate is None:
        return False
    else:
        return True


def insert(name, dob):
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Members(name, DOB, reg) VALUES(?, ?, datetime('now','localtime'))", (name, dob,))

    connection.commit()
    connection.close()


def delete(idtodelete):
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM Members WHERE id=?", (idtodelete,))
    except sqlite3.IntegrityError:
        return False

    connection.commit()
    connection.close()
    return True


def readall():
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Members")
    data = cursor.fetchall()

    connection.close()
    return data


def checkid(idtodisplay):
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM Members")
    data = cursor.fetchall()

    connection.close()

    ids = [num[0] for num in data]
    if idtodisplay in ids:
        return True
    else:
        return False


def booksissuedbymem(idtodisplay, flag):
    connection = sqlite3.connect(os.path.join(home, '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    if flag == 'norm':
        cursor.execute('''SELECT Books.id, Members.name, Books.title, Issue.issue_date, Issue.return_date 
        FROM Books JOIN Members JOIN Issue
        ON Members.id = Issue.id_user AND Books.id = Issue.id_book 
        WHERE Members.id = ? AND Issue.return_date is NULL
        ORDER BY Issue.issue_date DESC
        ''', (idtodisplay,))
    else:
        cursor.execute('''SELECT Books.id, Members.name, Books.title, Issue.issue_date, Issue.return_date 
        FROM Books JOIN Members JOIN Issue
        ON Members.id = Issue.id_user AND Books.id = Issue.id_book 
        WHERE Members.id = ? 
        ORDER BY Issue.return_date ASC
        ''', (idtodisplay,))

    data = cursor.fetchall()
    connection.close()

    return data
