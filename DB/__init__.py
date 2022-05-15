import sqlite3
import os

connection = sqlite3.connect(os.path.join(os.path.expanduser("~"), '.LMSystem/library.sqlite'))
connection.execute('PRAGMA foreign_keys = ON')  # We need this because foreign keys are disabled by default
cursor = connection.cursor()

# Books table
cursor.execute('''CREATE TABLE IF NOT EXISTS Books(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    rating INTEGER,
    genre TEXT NOT NULL,
    add_date TEXT NOT NULL,
    copies_total INTEGER NOT NULL,
    copies_issued INTEGER NOT NULL
    CHECK (rating > 0 AND rating < 6)
    )
    ''')

# Members table
cursor.execute('''CREATE TABLE IF NOT EXISTS Members(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL,
    DOB TEXT NOT NULL,
    reg TEXT NOT NULL
    )
    ''')

# Issue table
cursor.execute('''CREATE TABLE IF NOT EXISTS Issue(
    id_user INTEGER NOT NULL,
    id_book INTEGER NOT NULL,
    issue_date TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY(id_user) REFERENCES Members(id),
    FOREIGN KEY(id_book) REFERENCES Books(id)
    )
    ''')

# Rating table
cursor.execute('''CREATE TABLE IF NOT EXISTS Rating(
   id_book INTEGER NOT NULL,
   rating INTEGER,
   CHECK(rating > 0 AND rating < 6),
   FOREIGN KEY(id_book) REFERENCES Books(id)
   )
   ''')

connection.commit()
connection.close()
