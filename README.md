# Library-Management-System

A library management system built using Python and Sqlite3 with PySide6 for the front end.

**Tested on MacOS and Windows, build available only for M1 Macs and Windows x64.**

### To Build (MacOS):

pyinstaller app.py -y --windowed --clean --name "LM System" --icon "icon.png" --distpath "./pyinstaller/dist" --workpath "./pyinstaller/build" --add-data "Assets:Assets"

### To Build (Windows):

pyinstaller app.py -y --onefile --noconsole --clean --name "LM System" --icon "icon.png" --distpath "./pyinstaller/dist" --workpath "./pyinstaller/build" --add-data "Assets;Assets"

### Link to Download:

https://drive.google.com/drive/folders/1KwaN11ke53sPyp_n8JTCHFvoG02Af1EY?usp=sharing

### Tables used:

#### Books:

- id (Primary & Autoincrement)
- title
- author
- rating (Average calculated from Rating table on return)
- genre
- add_date
- copies_total
- copies_issued

#### Members:

- id (Primary & Autoincrement)
- name
- DOB
- reg

#### Issue:

- id_user (Foreign from Members)
- id_book (Foreign from Books)
- issue_date (Generated on issue)
- return_date (Generated on return)

#### Rating:

- id_book (Foreign from Books)
- rating

### Demo:

#### Password Prompt:

![](Videos/1_pwdprompt.gif)

#### Admin Window (Adding & Deleting):

![](Videos/2_adminwindow.gif)

#### Searching book online using ISBN:

![](Videos/3_addisbn.gif)

#### Issue Feature:

![](Videos/4_issue.gif)

#### Deposit Feature:

![](Videos/5_deposit.gif)

#### Prevention of Deletion:

![](Videos/6_prevention.gif)
