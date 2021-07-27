#!/bin/bash
pyuic5 UI/uifiles/myapp.ui -o UI/myapp.py
pyuic5 UI/uifiles/addmembers.ui -o UI/addmembersdialog.py
pyuic5 UI/uifiles/deletemembers.ui -o UI/deletemembersdialog.py
pyuic5 UI/uifiles/admin.ui -o UI/adminui.py
pyuic5 UI/uifiles/pwd.ui -o UI/pwddialog.py
pyuic5 UI/uifiles/pwdnew.ui -o UI/pwddialognew.py
pyuic5 UI/uifiles/addbooks.ui -o UI/addbooksdialog.py
pyuic5 UI/uifiles/deletebooks.ui -o UI/deletebooksdialog.py
pyuic5 UI/uifiles/bookdetails.ui -o UI/bookdetails.py
pyuic5 UI/uifiles/issuebook.ui -o UI/issuebook.py