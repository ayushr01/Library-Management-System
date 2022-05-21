from PySide6.QtWidgets import QDialog, QTableWidgetItem

import GeneratedUI.adminui

import UI.members
import UI.books

import DB.books
import DB.members


# Admin window with 2 tabs
class AdminWindow(QDialog, GeneratedUI.adminui.Ui_AdminWindow):
    def __init__(self, mainwindow):
        super().__init__()
        # Calls the function to create all the elements in the window
        self.setupUi(self)

        self.mainwindow = mainwindow  # To refresh the genre list

        # Member tab
        self.addmemberdialog = UI.members.AddMemberDialog(adminwindow=self)
        self.deletememberdialog = UI.members.DeleteMemberDialog(
            adminwindow=self)

        self.addmem.clicked.connect(self.addmemberdialog.makedialog)
        self.refreshmem.clicked.connect(self.loadmem)
        self.deletemem.clicked.connect(self.deletememberdialog.makedialog)

        self.memtable.setColumnWidth(0, 50)

        self.loadmem()  # Populates table as soon as the program runs

        # Book tab
        self.addbookdialog = UI.books.AddBookDialog(adminwindow=self)
        self.deletebookdialog = UI.books.DeleteBookDialog(adminwindow=self)

        self.addbook.clicked.connect(self.addbookdialog.makedialog)
        self.refreshbook.clicked.connect(self.loadbook)
        self.deletebook.clicked.connect(self.deletebookdialog.makedialog)

        self.booktable.setColumnWidth(0, 50)
        self.booktable.setColumnWidth(4, 50)
        self.booktable.setColumnWidth(5, 50)
        self.loadbook()  # Populates table as soon as the program runs

    # Adds data to the table in the member tab
    def loadmem(self):
        data = DB.members.readall()
        # It is always zero so we modify it
        self.memtable.setRowCount(len(data))
        position = 0
        for row in data:
            self.memtable.setItem(position, 0, QTableWidgetItem(str(row[0])))
            self.memtable.setItem(position, 1, QTableWidgetItem(row[1]))
            self.memtable.setItem(position, 2, QTableWidgetItem(row[2]))
            self.memtable.setItem(position, 3, QTableWidgetItem(row[3]))
            position = position + 1

    # Adds data to the table in the book tab
    def loadbook(self):
        data = DB.books.readall()
        # It is always zero so we modify it
        self.booktable.setRowCount(len(data))
        position = 0
        for row in data:
            self.booktable.setItem(position, 0, QTableWidgetItem(str(row[0])))
            self.booktable.setItem(position, 1, QTableWidgetItem(row[1]))
            self.booktable.setItem(position, 2, QTableWidgetItem(row[2]))
            self.booktable.setItem(position, 3, QTableWidgetItem(row[4]))
            self.booktable.setItem(position, 4, QTableWidgetItem(str(row[6])))
            self.booktable.setItem(position, 5, QTableWidgetItem(str(row[7])))
            position = position + 1
        self.mainwindow.loadgenre()  # Populates the genre list with new genres
