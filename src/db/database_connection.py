import sqlite3
from db.config import DATABASE_FILE_PATH
# Pylint disabled due to fixing the "error" makes the actual code not work

CONNECTION = None


def get_database_connection():
    global CONNECTION
    if CONNECTION is None:
        CONNECTION = sqlite3.connect(DATABASE_FILE_PATH)
        CONNECTION.row_factory = sqlite3.Row
    return CONNECTION
