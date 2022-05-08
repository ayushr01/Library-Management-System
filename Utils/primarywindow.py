from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QListWidgetItem

import UI.myapp as myapp

import Utils.pwd as pwd
import Utils.admin as admin
import Utils.books as book
import Utils.members as mem
import Utils.library as lib


#######################
# Wriiten by: Ayush Rao
#######################

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
        self.adminbutton.clicked.connect(self.loadpwd)
        self.refreshbutton.clicked.connect(self.loadbooks)
        self.detailsbutton.clicked.connect(self.loaddetails)
        self.issuebutton.clicked.connect(self.loadissue)

        # Radio buttons
        self.avaiablebooksbutton.setChecked(True)
        self.titlebutton.setChecked(True)

        self.adminwindow = admin.AdminWindow(self)  # Creates the admin window on launch
        # I pass self so that the genre function can be called

        # Deposit tab

        # Button actions
        self.viewbookbutton.clicked.connect(lambda: self.loadissuedbooks('norm'))
        self.viewbookhistorybutton.clicked.connect(lambda: self.loadissuedbooks('hist'))
        self.returnbutton.clicked.connect(self.returnbook)

        # Functions to run on startup
        self.fivestar.setChecked(True)
        self.loadgenre()  # Populates genres on launch
        self.loadbooks()  # Populates list on launch

    def loadadmin(self):
        self.adminwindow.show()  # Shows the admin window

    def loadpwd(self):
        if pwd.checkadmin():
            self.pwddialog.makedialog()
        else:
            self.pwddialognew.makedialog()

    def loaddetails(self):
        if self.booklist.currentItem() is None:
            pass
        else:
            self.bookdialog.makedialog(self.booklist.currentItem())

    def loadissue(self):
        if self.booklist.currentItem() is None:
            pass
        elif lib.checkstock(self.booklist.currentItem()):
            self.errorlabel.setText('')
            self.issuedialog.makedialog(self.booklist.currentItem())
        else:
            self.errorlabel.setText('Error: This book is out of stock!')

    def loadissuedbooks(self, flag):
        self.returnbooklist.clear()
        text = self.idfield.text()
        if text == '':
            self.errorlabel_2.setText('Error: Enter your member id!')
        elif text.isnumeric() is False:
            self.errorlabel_2.setText('Error: Enter a number!')
        else:
            self.errorlabel_2.setText('')
            if mem.checkid(int(text)) and flag == 'norm':
                position = 0
                for row in mem.booksissuedbymem(int(text), flag):
                    self.errorlabel_2.setText(f"Viewing books issued by {row[1]}")
                    item = QListWidgetItem()
                    item.setSizeHint(QSize(500, 50))
                    item.setText(f'''<ID: {row[0]}> {row[2]}
Issued on {row[3]}''')
                    self.returnbooklist.insertItem(position, item)
                    position = position + 1
            elif mem.checkid(int(text)) and flag == 'hist':
                position = 0
                for row in mem.booksissuedbymem(int(text), flag):
                    self.errorlabel_2.setText(f"Viewing history of books issued by {row[1]}")
                    item = QListWidgetItem()
                    item.setSizeHint(QSize(500, 75))
                    item.setText(f'''<ID: {row[0]}> {row[2]}
Issued on {row[3]}
Returned on {row[4]}''')
                    self.returnbooklist.insertItem(position, item)
                    position = position + 1
            else:
                self.errorlabel_2.setText('Member not found in database!')

    def loadbooks(self):
        self.booklist.clear()
        sortingdata = self.filters()
        bookdata = book.readsorted(sortingdata)
        position = 0
        for row in bookdata:
            rating = ''
            if row[3] is not None:
                rating = ' - '
                for num in range(1, int(row[3]) + 1):
                    rating = rating + '⭐'
            item = QListWidgetItem()
            item.setSizeHint(QSize(0, 50))
            item.setText(f" <ID: {row[0]}>  {row[1]} by {row[2]} - {row[4]}{rating}")
            self.booklist.insertItem(position, item)
            position = position + 1
        if len(bookdata) != 0:
            self.booklist.item(0).setSelected(True)

    def loadgenre(self):
        self.genrebox.clear()
        self.genrebox.addItem("No Genre")
        data = book.readgenre()
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

            lib.setrating(bookid, rating)
            lib.returnbook(memid, bookid, dateissued)
            self.loadissuedbooks('norm')
