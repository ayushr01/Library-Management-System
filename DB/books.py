import os
import sqlite3


def insert(title, author, genre, totalcopies):
    connection = sqlite3.connect(os.path.join(os.path.expanduser("~"), '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO Books(title, author, rating, genre, add_date, copies_total, copies_issued) 
    VALUES(?, ?, NULL, ?, datetime('now','localtime'), ?, 0)''', (title, author, genre, totalcopies,))

    connection.commit()
    connection.close()


def delete(idtodelete):
    connection = sqlite3.connect(os.path.join(os.path.expanduser("~"), '.LMSystem/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    try:
        cursor.execute("DELETE FROM Books WHERE id=?", (idtodelete,))
    except sqlite3.IntegrityError:
        return False

    connection.commit()
    connection.close()
    return True


def readall():
    connection = sqlite3.connect(os.path.join(os.path.expanduser("~"), '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Books')
    data = cursor.fetchall()

    connection.close()
    return data


def readsorted(sortingdata):
    connection = sqlite3.connect(os.path.join(os.path.expanduser("~"), '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    # viewfilter and genre
    constraint = ''
    if sortingdata[0]['available']:
        constraint = ' WHERE copies_issued < copies_total'
        if sortingdata[2] != 'No Genre':
            constraint = constraint + ' AND genre = ' + f"\'{sortingdata[2]}\'"
    elif sortingdata[0]['all']:
        if sortingdata[2] != 'No Genre':
            constraint = ' WHERE genre = ' + f"\'{sortingdata[2]}\'"

    # sortfilter
    sortconstraint = ' ORDER BY '
    if sortingdata[1]['title']:
        sortconstraint = sortconstraint + 'title'
    elif sortingdata[1]['author']:
        sortconstraint = sortconstraint + 'author'
    elif sortingdata[1]['rating']:
        sortconstraint = sortconstraint + 'rating DESC'

    maincommand = 'SELECT * FROM Books'
    command = maincommand + constraint + sortconstraint

    cursor.execute(command)
    data = cursor.fetchall()

    connection.close()
    return data


def readgenre():
    connection = sqlite3.connect(os.path.join(os.path.expanduser("~"), '.LMSystem/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('SELECT DISTINCT genre FROM Books')
    data = cursor.fetchall()

    connection.close()
    return data


def readwithid(idtodisplay):
    connection = sqlite3.connect(os.path.join(os.path.expanduser("~"), '.LMSystem/library.sqlite'))
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Books WHERE id = ?', (idtodisplay,))
    data = cursor.fetchall()

    connection.close()
    return data
