import os
import sqlite3

db_name = "collection.db"
db_path = os.path.join(os.path.dirname(__file__), os.pardir, "data", db_name)


def connect():
    return sqlite3.connect(db_path)
