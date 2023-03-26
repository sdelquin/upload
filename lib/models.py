import sqlite3
from collections import namedtuple
from pathlib import Path

import settings


def create_db_conn(db_path: Path) -> sqlite3.Connection:
    def namedtuple_factory(cursor, row):
        fields = [column[0] for column in cursor.description]
        cls = namedtuple('Row', fields)
        return cls._make(row)

    db_conn = sqlite3.connect(db_path)
    db_conn.row_factory = namedtuple_factory
    return db_conn


class DBHandler:
    def __init__(self, db_path: Path = settings.DB_PATH):
        self.conn = create_db_conn(db_path)

    def __del__(self):
        self.conn.close()

    def get_context(self, context_name: str):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT * FROM context WHERE name="{context_name}"')
        return cursor.fetchone()

    def get_contexts(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM context order by name')
        return cursor.fetchall()
