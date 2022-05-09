import os
import json

from PyQt6.QtWidgets import QDialog

import UI.pwddialog as pwddialog
import UI.pwddialognew as pwddialognew


#######################
# Wriiten by: Ayush Rao
#######################


class PwdDialog(QDialog, pwddialog.Ui_passworddialog):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow  # Used to launch the admin window after closing the dialog
        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

        # Setting field margins
        self.userfield.setTextMargins(10, 0, 10, 0)
        self.pwdfield.setTextMargins(10, 0, 10, 0)

        # Button actions
        self.clearbutton.clicked.connect(self.clearfields)
        self.submitbutton.clicked.connect(self.getfields)
        self.closebutton.clicked.connect(self.close)

    def makedialog(self):
        self.clearfields()  # Clears the fields before opening up the dialog window
        self.exec()  # Runs the dialog window

    def clearfields(self):
        self.userfield.setText('')
        self.pwdfield.setText('')
        self.error.setText('')

    def getfields(self):
        if checkusrpwd(self.userfield.text(), self.pwdfield.text()):
            self.close()
            self.mainwindow.loadadmin()  # Launches the admin window after setting pwd
        else:
            self.error.setText('Error: Username or Password is incorrect!')


class PwdDialogNew(QDialog, pwddialognew.Ui_passworddialog):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow  # Used to launch the admin window after closing the dialog
        self.setupUi(self)  # Calls the function to create all the elements in the dialog window

        # Setting field margins
        self.userfield.setTextMargins(10, 0, 10, 0)
        self.pwdfield.setTextMargins(10, 0, 10, 0)
        self.pwdfieldconfirm.setTextMargins(10, 0, 10, 0)

        # Button actions
        self.clearbutton.clicked.connect(self.clearfields)
        self.submitbutton.clicked.connect(self.getfields)
        self.closebutton.clicked.connect(self.close)

    def makedialog(self):
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
                self.close()
                self.mainwindow.loadadmin()  # Launches the admin window after setting pwd
            else:
                self.error.setText('Error: The passwords do not match!')


def checkadmin():
    if os.path.isfile(os.path.realpath('Files/pwd.json')):
        return True
    else:
        return False


def setusrpwd(username, password):
    data = dict()
    data['username'] = username
    data['password'] = password

    file = open(os.path.realpath('Files/pwd.json'), 'w')
    json.dump(data, file)

    file.close()


def checkusrpwd(username, password):
    file = open(os.path.realpath('Files/pwd.json'), 'r')
    data = json.load(file)
    if data['username'] == username and data['password'] == password:
        return True
    else:
        return False
