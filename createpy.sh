#!/bin/bash
pyside6-uic UI/uifiles/myapp.ui -o UI/myapp.py
pyside6-uic UI/uifiles/addmembers.ui -o UI/addmembersdialog.py
pyside6-uic UI/uifiles/deletemembers.ui -o UI/deletemembersdialog.py
pyside6-uic UI/uifiles/admin.ui -o UI/adminui.py
pyside6-uic UI/uifiles/pwd.ui -o UI/pwddialog.py
pyside6-uic UI/uifiles/pwdnew.ui -o UI/pwddialognew.py
pyside6-uic UI/uifiles/addbooks.ui -o UI/addbooksdialog.py
pyside6-uic UI/uifiles/deletebooks.ui -o UI/deletebooksdialog.py
pyside6-uic UI/uifiles/bookdetails.ui -o UI/bookdetails.py
pyside6-uic UI/uifiles/issuebook.ui -o UI/issuebook.py