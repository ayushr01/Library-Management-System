
# Library-Management-System
A library management system built using Python and Sqlite3 with PyQt5 for the front end.

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

