from PyQt6.QtWidgets import QDialog, QTableWidgetItem

import UI.adminui as admin
import Utils.members as member
import Utils.books as book


#######################
# Wriiten by: Ayush Rao
#######################


# Admin window with 2 tabs
class AdminWindow(QDialog, admin.Ui_AdminWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(self)  # Calls the function to create all the elements in the window

        self.mainwindow = mainwindow  # To refresh the genre list

        # Member tab
        self.addmemberdialog = member.AddMemberDialog(adminwindow=self)
        self.deletememberdialog = member.DeleteMemberDialog(adminwindow=self)

        self.addmem.clicked.connect(self.addmemberdialog.makedialog)
        self.refreshmem.clicked.connect(self.loadmem)
        self.deletemem.clicked.connect(self.deletememberdialog.makedialog)

        self.memtable.setColumnWidth(0, 50)

        self.loadmem()  # Populates table as soon as the program runs

        # Book tab
        self.addbookdialog = book.AddBookDialog(adminwindow=self)
        self.deletebookdialog = book.DeleteBookDialog(adminwindow=self)

        self.addbook.clicked.connect(self.addbookdialog.makedialog)
        self.refreshbook.clicked.connect(self.loadbook)
        self.deletebook.clicked.connect(self.deletebookdialog.makedialog)

        self.booktable.setColumnWidth(0, 50)
        self.booktable.setColumnWidth(4, 50)
        self.booktable.setColumnWidth(5, 50)
        self.loadbook()  # Populates table as soon as the program runs

    # Adds data to the table in the member tab
    def loadmem(self):
        data = member.readall()
        self.memtable.setRowCount(len(data))  # It is always zero so we modify it
        position = 0
        for row in data:
            self.memtable.setItem(position, 0, QTableWidgetItem(str(row[0])))
            self.memtable.setItem(position, 1, QTableWidgetItem(row[1]))
            self.memtable.setItem(position, 2, QTableWidgetItem(row[2]))
            self.memtable.setItem(position, 3, QTableWidgetItem(row[3]))
            position = position + 1

    # Adds data to the table in the book tab
    def loadbook(self):
        data = book.readall()
        self.booktable.setRowCount(len(data))  # It is always zero so we modify it
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
