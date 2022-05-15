import re

from PySide6.QtWidgets import QDialog

import GeneratedUI.addmembersdialog
import GeneratedUI.deletemembersdialog

import DB.members


# Validator
def namecheck(name):
    validate = re.search("^[A-Z][a-z]+\s[A-Z][a-z]+$", name)
    if validate is None:
        return False
    else:
        return True


# Dialog window to add more users to the member table
class AddMemberDialog(QDialog, GeneratedUI.addmembersdialog.Ui_addmemdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the member table

        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

        # Default date to clear the input field
        self.defaultdate = self.datepicker.dateTime()

        # Setting field margins
        self.inputname.setTextMargins(5, 0, 5, 0)

        # Button actions
        self.clearbutton.clicked.connect(self.clearfields)
        self.submitbutton.clicked.connect(self.getfields)
        self.closebutton.clicked.connect(self.close)

    def makedialog(self):
        self.clearfields()  # Clears the fields before opening up the dialog window
        self.exec()  # Runs the dialog window

    def clearfields(self):
        self.inputname.setText('')
        self.error.setText('')
        self.datepicker.setDateTime(self.defaultdate)

    def getfields(self):
        name = self.inputname.text()
        if namecheck(name):
            self.error.setText('')
            dob = self.datepicker.dateTime().date().toPyDate().strftime('%d-%m-%Y')
            DB.members.insert(name, dob)
            self.adminwindow.loadmem()  # Refreshes the member table after adding memberss
            self.close()
        else:
            self.error.setText('Error: Enter a valid First and Last Name!')


# Dialog window to Remove users from the member table
class DeleteMemberDialog(QDialog, GeneratedUI.deletemembersdialog.Ui_deletememdialog):
    def __init__(self, adminwindow):
        super().__init__()

        self.adminwindow = adminwindow  # To refresh the member table

        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

        # Button actions
        self.deletebutton.clicked.connect(self.deletemember)
        self.closebutton.clicked.connect(self.close)

    def makedialog(self):
        self.getlist()  # Populates the list as soon as the dialog box is displayed
        self.errorlabel.setText('')
        self.exec()  # Runs the dialog window

    def getlist(self):
        self.memlist.clear()
        memdata = DB.members.readall()
        if len(memdata) != 0:
            position = 0
            for row in memdata:
                self.memlist.insertItem(position, f"{row[0]} - {row[1]} - ({row[2]})")
                position = position + 1
            self.memlist.item(0).setSelected(True)

    def deletemember(self):
        memdata = self.memlist.currentItem()
        if memdata is not None:
            self.errorlabel.setText('')
            idtodelete = memdata.text().split('-')[0].rstrip()
            if DB.members.delete(idtodelete) is False:
                self.errorlabel.setText('Error: Book issued in their name!')
            self.getlist()
            self.adminwindow.loadmem()  # Refreshes the member table after deleting memberss
        else:
            self.errorlabel.setText('Error: Select an entry!')
