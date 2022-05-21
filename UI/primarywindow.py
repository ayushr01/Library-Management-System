from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QVBoxLayout

import GeneratedUI.myapp as myapp

import UI.pwd as pwd
import UI.admin as admin
import UI.books as book

import DB.books
import DB.members
import DB.library


class MainWindow(QMainWindow, myapp.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Calls the function to create all the elements in the window

        # Password dialog boxes
        self.pwddialog = pwd.PwdDialog(mainwindow=self)
        self.pwddialognew = pwd.PwdDialogNew(mainwindow=self)
        self.bookdialog = book.BookDetailsDialog()
        self.issuedialog = book.IssueBooksDialog()

        # Button actions
        self.adminbutton.clicked.connect(self.loadpwdadmin)
        self.refreshbutton.clicked.connect(self.loadbooks)
        self.detailsbutton.clicked.connect(self.loaddetails)
        self.issuebutton.clicked.connect(self.loadissue)

        # Radio buttons
        self.avaiablebooksbutton.setChecked(True)
        self.titlebutton.setChecked(True)

        self.adminwindow = admin.AdminWindow(self)  # Creates the admin window on launch
        # I pass self so that the genre function can be called

        # Button actions
        self.viewbookbutton.clicked.connect(lambda: self.loadissuedbooks('norm'))
        self.viewbookhistorybutton.clicked.connect(lambda: self.loadissuedbooks('hist'))
        self.returnbutton.clicked.connect(self.returnbook)

        # Functions to run on startup
        self.fivestar.setChecked(True)
        self.loadgenre()  # Populates genres on launch
        self.loadbooks()  # Populates list on launch

        # Used to check if pwd is cleared or not
        self.isAuthenticated = False

        # Setting group box header as bold
        font = self.sortby.font()
        font.setBold(True)
        font.setPixelSize(14)

        self.sortby.setFont(font)
        self.viewmode.setFont(font)
        self.genre.setFont(font)

        # Restore the font of each children to regular.
        font.setBold(False)
        font.setPixelSize(13)

        for child in self.sortby.children():
            if not isinstance(child, QVBoxLayout):
                child.setFont(font)
        for child in self.viewmode.children():
            if not isinstance(child, QVBoxLayout):
                child.setFont(font)
        for child in self.genre.children():
            if not isinstance(child, QVBoxLayout):
                child.setFont(font)
        
        # Setting field margins
        self.idfield.setTextMargins(5, 0, 5, 0)

    def loadpwdadmin(self):
        if pwd.checkadmin():
            self.pwddialog.makedialog()
        else:
            self.pwddialognew.makedialog()
        if self.isAuthenticated is True:
            self.adminwindow.exec()  # Shows the admin window
            self.isAuthenticated = False

    def loaddetails(self):
        if len(self.booklist.selectedItems()) == 0:
            self.errorlabel.setText('Error: Select a book!')
        else:
            self.bookdialog.makedialog(self.booklist.selectedItems()[0])

    def loadissue(self):
        if len(self.booklist.selectedItems()) == 0:
            self.errorlabel.setText('Error: Select a book!')
        elif DB.library.checkstock(self.booklist.selectedItems()[0]):
            self.errorlabel.setText('')
            self.issuedialog.makedialog(self.booklist.currentItem())
        else:
            self.errorlabel.setText('Error: This book is out of stock!')

    def loadissuedbooks(self, flag):
        self.returnbooklist.clear()
        text = self.idfield.text()
        if text == '':
            self.errorlabeldeposit.setText('Error: Enter your member id!')
        elif text.isnumeric() is False:
            self.errorlabeldeposit.setText('Error: Enter a number!')
        else:
            self.errorlabeldeposit.setText('')
            if DB.members.checkid(int(text)) and flag == 'norm':
                position = 0
                for row in DB.members.booksissuedbymem(int(text), flag):
                    self.errorlabeldeposit.setText(f"Viewing books issued by {row[1]}")
                    item = QListWidgetItem()
                    item.setSizeHint(QSize(500, 50))
                    item.setText(f'''<ID: {row[0]}> {row[2]}
Issued on {row[3]}''')
                    self.returnbooklist.insertItem(position, item)
                    position = position + 1
            elif DB.members.checkid(int(text)) and flag == 'hist':
                position = 0
                for row in DB.members.booksissuedbymem(int(text), flag):
                    self.errorlabeldeposit.setText(f"Viewing history of books issued by {row[1]}")
                    item = QListWidgetItem()
                    item.setSizeHint(QSize(500, 75))
                    item.setText(f'''<ID: {row[0]}> {row[2]}
Issued on {row[3]}
Returned on {row[4]}''')
                    self.returnbooklist.insertItem(position, item)
                    position = position + 1
            else:
                self.errorlabeldeposit.setText('Member not found in database!')

    def loadbooks(self):
        self.booklist.clear()
        sortingdata = self.filters()
        bookdata = DB.books.readsorted(sortingdata)
        position = 0
        for row in bookdata:
            rating = ''
            if row[3] is not None:
                rating = ' - '
                for num in range(1, int(row[3]) + 1):
                    rating = rating + '☆'
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 50))
            item.setText(f" <ID: {row[0]}>  {row[1]} by {row[2]} - {row[4]}{rating}")
            self.booklist.insertItem(position, item)
            position = position + 1

    def loadgenre(self):
        self.genrebox.clear()
        self.genrebox.addItem("No Genre")
        data = DB.books.readgenre()
        for row in data:
            self.genrebox.addItem(row[0])

    def filters(self):
        viewfilter = {
            'all': self.allbooksbutton.isChecked(),
            'available': self.avaiablebooksbutton.isChecked(),
        }
        sortfilter = {
            'title': self.titlebutton.isChecked(),
            'author': self.authorbutton.isChecked(),
            'rating': self.ratingbutton.isChecked()
        }
        genrefilter = self.genrebox.currentText()
        return [viewfilter, sortfilter, genrefilter]

    def returnbook(self):
        bookdata = self.returnbooklist.currentItem()
        if bookdata is not None:
            text = bookdata.text()
            beg = text.find('<') + 5
            end = text.find('>')
            bookid = int(text[beg:end])
            memid = int(self.idfield.text())
            beg = text.find('Issued on ')
            dateissued = text[beg + 10:]

            rating = {
                'one': self.onestar.isChecked(),
                'two': self.twostar.isChecked(),
                'three': self.threestar.isChecked(),
                'four': self.fourstar.isChecked(),
                'five': self.fivestar.isChecked()
            }

            DB.library.setrating(bookid, rating)
            DB.library.returnbook(memid, bookid, dateissued)
            self.loadissuedbooks('norm')
