#!/bin/bash
pyuic6 UI/uifiles/myapp.ui -o UI/myapp.py
pyuic6 UI/uifiles/addmembers.ui -o UI/addmembersdialog.py
pyuic6 UI/uifiles/deletemembers.ui -o UI/deletemembersdialog.py
pyuic6 UI/uifiles/admin.ui -o UI/adminui.py
pyuic6 UI/uifiles/pwd.ui -o UI/pwddialog.py
pyuic6 UI/uifiles/pwdnew.ui -o UI/pwddialognew.py
pyuic6 UI/uifiles/addbooks.ui -o UI/addbooksdialog.py
pyuic6 UI/uifiles/deletebooks.ui -o UI/deletebooksdialog.py
pyuic6 UI/uifiles/bookdetails.ui -o UI/bookdetails.py
pyuic6 UI/uifiles/issuebook.ui -o UI/issuebook.py