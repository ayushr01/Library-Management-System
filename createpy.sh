#!/bin/bash
pyside6-uic GeneratedUI/uifiles/myapp.ui -o GeneratedUI/myapp.py
pyside6-uic GeneratedUI/uifiles/addmembers.ui -o GeneratedUI/addmembersdialog.py
pyside6-uic GeneratedUI/uifiles/deletemembers.ui -o GeneratedUI/deletemembersdialog.py
pyside6-uic GeneratedUI/uifiles/admin.ui -o GeneratedUI/adminui.py
pyside6-uic GeneratedUI/uifiles/pwd.ui -o GeneratedUI/pwddialog.py
pyside6-uic GeneratedUI/uifiles/pwdnew.ui -o GeneratedUI/pwddialognew.py
pyside6-uic GeneratedUI/uifiles/addbooks.ui -o GeneratedUI/addbooksdialog.py
pyside6-uic GeneratedUI/uifiles/deletebooks.ui -o GeneratedUI/deletebooksdialog.py
pyside6-uic GeneratedUI/uifiles/bookdetails.ui -o GeneratedUI/bookdetails.py
pyside6-uic GeneratedUI/uifiles/issuebook.ui -o GeneratedUI/issuebook.py
