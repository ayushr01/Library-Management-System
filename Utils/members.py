import sqlite3
import re
import os

from PyQt5.QtWidgets import *
import UI.addmembersdialog as addmemdialog
import UI.deletemembersdialog as deletememdialog


# Dialog window to add more users to the member table
class AddMemberDialog(QDialog, addmemdialog.Ui_addmemdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the member table

        self.dialog = QDialog(adminwindow)  # Creates a dialog window under the mainwindow
        self.setupUi(self.dialog)  # Calls the function to create all the elements in the dialog window

        # Default date to clear the input field
        self.defaultdate = self.datepicker.dateTime()

        # Button actions
        self.clearbutton.clicked.connect(self.clearfields)
        self.submitbutton.clicked.connect(self.getfields)
        self.closebutton.clicked.connect(self.dialog.close)

    def makedialog(self):
        self.clearfields()  # Clears the fields before opening up the dialog window
        self.dialog.exec_()  # Runs the dialog window

    def clearfields(self):
        self.inputname.setText('')
        self.errorlabel.setText('')
        self.datepicker.setDateTime(self.defaultdate)

    def getfields(self):
        name = self.inputname.text()
        if namecheck(name):
            self.errorlabel.setText('')
            dob = self.datepicker.dateTime().date().toPyDate().strftime('%d-%m-%Y')
            insert(name, dob)
            self.adminwindow.loadmem()  # Refreshes the member table after adding memberss
            self.dialog.close()
        else:
            self.errorlabel.setText('Error: Enter a valid First and Last Name!')


# Dialog window to Remove users from the member table
class DeleteMemberDialog(QDialog, deletememdialog.Ui_deletememdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the member table

        self.dialog = QDialog(adminwindow)  # Creates a dialog window under the mainwindow
        self.setupUi(self.dialog)  # Calls the function to create all the elements in the dialog window

        # Button actions
        self.deletebutton.clicked.connect(self.deletemember)
        self.closebutton.clicked.connect(self.dialog.close)

    def makedialog(self):
        self.getlist()  # Populates the list as soon as the dialog box is displayed
        self.errorlabel.setText('')
        self.dialog.exec_()  # Runs the dialog window

    def getlist(self):
        self.memlist.clear()
        memdata = readall()
        position = 0
        for row in memdata:
            self.memlist.insertItem(position, f"{row[0]} - {row[1]} - ({row[2]})")
            position = position + 1
        self.memlist.item(0).setSelected(True)

    def deletemember(self):
        memdata = self.memlist.currentItem()
        print(memdata)
        if memdata is not None:
            self.errorlabel.setText('')
            idtodelete = memdata.text().split('-')[0].rstrip()
            if delete(idtodelete) is False:
                self.errorlabel.setText('Error: Book issued in their name!')
            self.getlist()
            self.adminwindow.loadmem()  # Refreshes the member table after deleting memberss
        else:
            self.errorlabel.setText('Error: Select an entry!')


###############################################
# All the helper functions for the dialog boxes
###############################################

def initialise():
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
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
    validate = None
    validate = re.search("^[A-Z][a-z]+\s[A-Z][a-z]+$", name)
    if validate is None:
        return False
    else:
        return True


def insert(name, dob):
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Members(name, DOB, reg) VALUES(?, ?, datetime('now','localtime'))", (name, dob,))

    connection.commit()
    connection.close()


def delete(idtodelete):
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
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
    connection = sqlite3.connect(os.path.realpath('Files/library.sqlite'))
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Members")
    data = cursor.fetchall()

    connection.close()
    return data


initialise()  # Makes sure the table is available
