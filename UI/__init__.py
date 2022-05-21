import os

if not os.path.exists(os.path.join(os.path.expanduser("~"), '.LMSystem')):
    # Creates the file folder for database
    os.mkdir(os.path.join(os.path.expanduser("~"), '.LMSystem'))
