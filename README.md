# Library-Management-System
A library management system built using Python and Sqlite3 with PyQt5 for the front end.

**Only tested on MacOS, build available only for M1 Macs.**

### To Build:
 pyinstaller app.py --windowed --clean --name "LM System" --icon "icon.icns"  

### Link to Download (Pending): 
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
![1 - Admin screen](https://user-images.githubusercontent.com/22570553/127285218-f9d9e4dc-8fb9-4fa2-83fb-4da26fe420a9.gif)
#### Admin Window (Adding & Deleting):
![2 - Add](https://user-images.githubusercontent.com/22570553/127285235-d7cd05fd-d8d1-4f79-b902-3e1db8f5c1eb.gif)
![3 - Delete](https://user-images.githubusercontent.com/22570553/127285256-ccbefced-dbc9-483c-bf2a-97c0bcaf686a.gif)
#### Issue Feature:
![4 - Issue Feature](https://user-images.githubusercontent.com/22570553/127285268-afcf5a1b-b3f1-47b9-a1a4-b711ea0f85e2.gif)
#### Deposit Feature:
![5 - Deposit Feature](https://user-images.githubusercontent.com/22570553/127285287-9106282c-a086-48d1-9286-17dec1fd7f64.gif)
#### Prevention of Deletion:
![6 - Data Integrity](https://user-images.githubusercontent.com/22570553/127285293-672176e8-96ac-4432-9591-fe21a2430498.gif)
