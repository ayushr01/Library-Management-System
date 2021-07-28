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


def initialiserating():
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Rating(
    id_book INTEGER NOT NULL,
    rating INTEGER,
    CHECK(rating > 0 AND rating < 6),
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


def returnbook(id_user, id_book, dateissued):
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    cursor.execute('''UPDATE Issue SET return_date = datetime('now','localtime') 
    WHERE id_user = ? AND id_book = ? and issue_date = ?''', (id_user, id_book, dateissued))

    cursor.execute('UPDATE Books SET copies_issued = copies_issued - 1 WHERE id = ?', (id_book,))
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


def setrating(id_book, rating):
    rate = None
    if rating['one']:
        rate = 1
    elif rating['two']:
        rate = 2
    elif rating['three']:
        rate = 3
    elif rating['four']:
        rate = 4
    elif rating['five']:
        rate = 5

    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Rating VALUES(?, ?)', (id_book, rate))
    connection.commit()
    connection.close()

    updaterating(id_book)


def updaterating(id_book):
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
    cursor = connection.cursor()

    cursor.execute('SELECT rating FROM Rating WHERE id_book = ?', (id_book,))

    rating = cursor.fetchall()
    rating = [rate[0] for rate in rating]

    sum = 0
    for num in rating:
        sum = sum + num

    avg = sum / len(rating)

    cursor.execute('UPDATE Books SET rating = ? WHERE id = ?', (round(avg, 1), id_book))

    connection.commit()
    connection.close()


initialise()  # Makes sure the table is available
initialiserating()
