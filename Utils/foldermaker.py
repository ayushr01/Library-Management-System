import os

home = os.path.expanduser("~")


def makefolder():
    if not os.path.exists(os.path.join(home, '.LMSystem')):
        os.mkdir(os.path.join(home, '.LMSystem'))  # Creates the file folder for database
