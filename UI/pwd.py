import os
import json

from PySide6.QtWidgets import QDialog

import GeneratedUI.pwddialog
import GeneratedUI.pwddialognew


class PwdDialog(QDialog, GeneratedUI.pwddialog.Ui_passworddialog):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow  # Used to launch the admin window after closing the dialog
        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

        # Setting field margins
        self.userfield.setTextMargins(5, 0, 5, 0)
        self.pwdfield.setTextMargins(5, 0, 5, 0)

        # Button actions
        self.clearbutton.clicked.connect(self.clearfields)
        self.submitbutton.clicked.connect(self.getfields)
        self.closebutton.clicked.connect(self.close)

        # Setting font sizes
        font = self.info.font()
        font.setPixelSize(15)
        self.info.setFont(font)

        # Enter action for fields
        self.userfield.returnPressed.connect(self.submitbutton.click)
        self.pwdfield.returnPressed.connect(self.submitbutton.click)

    def makedialog(self):
        self.userfield.setFocus()  # Make sure that userfield is always focused
        self.clearfields()  # Clears the fields before opening up the dialog window
        self.exec()  # Runs the dialog window

    def clearfields(self):
        self.userfield.setText('')
        self.pwdfield.setText('')
        self.error.setText('')

    def getfields(self):
        if checkusrpwd(self.userfield.text(), self.pwdfield.text()):
            self.mainwindow.isAuthenticated = True
            self.close()
        else:
            self.error.setText('Error: Username or Password is incorrect!')


class PwdDialogNew(QDialog, GeneratedUI.pwddialognew.Ui_passworddialog):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow  # Used to launch the admin window after closing the dialog
        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

        # Setting field margins
        self.userfield.setTextMargins(5, 0, 5, 0)
        self.pwdfield.setTextMargins(5, 0, 5, 0)
        self.pwdfieldconfirm.setTextMargins(5, 0, 5, 0)

        # Button actions
        self.clearbutton.clicked.connect(self.clearfields)
        self.submitbutton.clicked.connect(self.getfields)
        self.closebutton.clicked.connect(self.close)

        # Setting font sizes
        font = self.info.font()
        font.setPixelSize(15)
        self.info.setFont(font)

        # Enter action for fields
        self.userfield.returnPressed.connect(self.submitbutton.click)
        self.pwdfield.returnPressed.connect(self.submitbutton.click)
        self.pwdfieldconfirm.returnPressed.connect(self.submitbutton.click)

    def makedialog(self):
        self.userfield.setFocus()  # Make sure that userfield is always focused
        self.clearfields()  # Clears the fields before opening up the dialog window
        self.exec()  # Runs the dialog window

    def clearfields(self):
        self.userfield.setText('')
        self.pwdfield.setText('')
        self.pwdfieldconfirm.setText('')
        self.error.setText('')

    def getfields(self):
        if self.userfield.text() == '':
            self.error.setText('Error: Enter a username!')
            return
        else:
            self.error.setText('')

        if self.pwdfield.text() == '':
            self.error.setText('Error: Enter a password!')
            return
        else:
            self.error.setText('')

        if self.pwdfieldconfirm.text() == '':
            self.error.setText('Error: Confirm your password!')
            return
        else:
            self.error.setText('')
            if self.pwdfield.text() == self.pwdfieldconfirm.text():
                setusrpwd(self.userfield.text(), self.pwdfield.text())
                self.mainwindow.isAuthenticated = True
                self.close()
            else:
                self.error.setText('Error: The passwords do not match!')


def checkadmin():
    if os.path.isfile(os.path.join(os.path.expanduser("~"), '.LMSystem/pwd.json')):
        return True
    else:
        return False


def setusrpwd(username, password):
    data = dict()
    data['username'] = username
    data['password'] = password

    file = open(os.path.join(os.path.expanduser("~"), '.LMSystem/pwd.json'), 'w')
    json.dump(data, file)

    file.close()


def checkusrpwd(username, password):
    file = open(os.path.join(os.path.expanduser("~"), '.LMSystem/pwd.json'), 'r')
    data = json.load(file)
    if data['username'] == username and data['password'] == password:
        return True
    else:
        return False
