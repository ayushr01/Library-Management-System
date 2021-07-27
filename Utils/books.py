import sqlite3
import re
import os

from PyQt5.QtWidgets import *
import UI.addbooksdialog as addbkdialog
import UI.deletebooksdialog as delbkdialog


# Dialog window to add more users to the member table
class AddBookDialog(QDialog, addbkdialog.Ui_addbkdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the book table

        self.dialog = QDialog(adminwindow)  # Creates a dialog window under the mainwindow
        self.setupUi(self.dialog)  # Calls the function to create all the elements in the dialog window

        # Button actions
        self.clearbutton.clicked.connect(self.clearfields)
        self.submitbutton.clicked.connect(self.getfields)
        self.closebutton.clicked.connect(self.dialog.close)

    def makedialog(self):
        self.clearfields()  # Clears the fields before opening up the dialog window
        self.dialog.exec_()  # Runs the dialog window

    def clearfields(self):
        self.inputtitle.setText('')
        self.inputauthor.setText('')
        self.inputgenre.setText('')
        self.inputtotal.setText('')
        self.errortitle.setText('')
        self.errorauthor.setText('')
        self.errorgenre.setText('')

    def getfields(self):
        issue = False
        title = self.inputtitle.text()
        author = self.inputauthor.text()
        genre = self.inputgenre.text()
        totalcopies = self.inputtotal.text()

        if check(title, 'title') is False:
            issue = True
            self.errortitle.setText('Error: Enter a valid title!')
        else:
            self.errortitle.setText('')

        if check(author, 'author') is False:
            issue = True
            self.errorauthor.setText('Error: Enter a valid First and Last Name!')
        else:
            self.errorauthor.setText('')

        if check(genre, 'genre') is False:
            issue = True
            self.errorgenre.setText('Error: Enter a valid genre!')
        else:
            self.errorgenre.setText('')

        if totalcopies.isnumeric() is False:
            issue = True
            self.errortotal.setText('Error: Enter a number!')
        else:
            totalcopies = int(totalcopies)
            if totalcopies < 1 or totalcopies > 100:
                issue = True
                self.errortotal.setText('Error: Enter in the range 1-100')
            else:
                self.errortotal.setText('')

        if issue is False:
            insert(title, author, genre, totalcopies)
            self.adminwindow.loadbook()  # Refreshes the book table after adding books
            self.dialog.close()


class DeleteBookDialog(QDialog, delbkdialog.Ui_deletebookdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the book table

        self.dialog = QDialog(adminwindow)  # Creates a dialog window under the mainwindow
        self.setupUi(self.dialog)  # Calls the function to create all the elements in the dialog window

        # Button actions
        self.deletebutton.clicked.connect(self.deletebook)
        self.closebutton.clicked.connect(self.dialog.close)

    def makedialog(self):
        self.getlist()  # Populates the list as soon as the dialog box is displayed
        self.errorlabel.setText('')
        self.dialog.exec_()  # Runs the dialog window

    def getlist(self):
        self.booklist.clear()
        bookdata = readall()
        position = 0
        for row in bookdata:
            self.booklist.insertItem(position, f"{row[0]} - {row[1]} by {row[2]}")
            position = position + 1

    def deletebook(self):
        bookdata = self.booklist.currentItem()
        if bookdata is not None:
            self.errorlabel.setText('')
            idtodelete = bookdata.text().split('-')[0].rstrip()
            if delete(idtodelete) is False:
                self.errorlabel.setText('Error: Book issued by a member!')
            self.getlist()
            self.adminwindow.loadbook()  # Refreshes the book table after deleting books
        else:
            self.errorlabel.setText('Error: Select an entry!')


###############################################
# All the helper functions for the dialog boxes
###############################################


def initialise():
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Books(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    rating INTEGER,
    genre TEXT NOT NULL,
    add_date TEXT NOT NULL,
    copies_total INTEGER NOT NULL,
    copies_issued INTEGER NOT NULL
    CHECK (rating > 0 AND rating < 6)
    )
    ''')

    connection.commit()
    connection.close()


def check(data, field):
    regex = {
        'title': "^[A-Za-z0-9\s\-,\.;:()]+$",
        'author': "^[A-Z][a-z]+\s[A-Z][a-z]+$",
        'genre': "^[A-Za-z\s\-]+$"
    }
    validate = re.search(regex[field], data)
    if validate is None:
        return False
    else:
        return True


def insert(title, author, genre, totalcopies):
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO Books(title, author, rating, genre, add_date, copies_total, copies_issued) 
    VALUES(?, ?, NULL, ?, datetime('now','localtime'), ?, 0)''', (title, author, genre, totalcopies,))

    connection.commit()
    connection.close()


def delete(idtodelete):
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
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
    initialise()  # Needs to be only in this function as it is called as soon as the window is created
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Books')
    data = cursor.fetchall()

    connection.close()
    return data


def readsorted(sortingdata):
    initialise()  # Needs to be only in this function as it is called as soon as the window is created
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()

    # viewfilter and genre
    constraint = ''
    if sortingdata[0]['all']:
        if sortingdata[2] != 'No Genre':
            constraint = ' WHERE genre = ' + f"\'{sortingdata[2]}\'"
    elif sortingdata[0]['available']:
        constraint = ' WHERE copies_issued < copies_total'
        if sortingdata[2] != 'No Genre':
            constraint = constraint + ' AND genre = ' + f"\'{sortingdata[2]}\'"

    # sortfilter
    sortconstraint = ' ORDER BY '
    if sortingdata[1]['title']:
        sortconstraint = sortconstraint + 'title'
    elif sortingdata[1]['author']:
        sortconstraint = sortconstraint + 'author'
    elif sortingdata[1]['rating']:
        sortconstraint = sortconstraint + 'rating DESC'

    command = 'SELECT * FROM Books' + constraint + sortconstraint

    cursor.execute(command)
    data = cursor.fetchall()

    connection.close()
    return data


def readgenre():
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute('SELECT DISTINCT genre FROM Books')
    data = cursor.fetchall()

    connection.close()
    return data


def readwithid(idtodisplay):
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Books WHERE id = ?', (idtodisplay,))
    data = cursor.fetchall()

    connection.close()
    return data
