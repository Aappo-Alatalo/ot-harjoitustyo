import sqlite3
from db.config import DATABASE_FILE_PATH

_connection = None

def get_database_connection():
    global _connection
    if _connection is None:
        _connection = sqlite3.connect(DATABASE_FILE_PATH)
        _connection.row_factory = sqlite3.Row
    return _connection