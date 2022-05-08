import os


def makefolder():
    if not os.path.exists(os.path.realpath('Files')):
        os.mkdir(os.path.realpath('Files'))  # Creates the file folder for database
