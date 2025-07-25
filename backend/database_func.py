import sqlite3

def table_exists(table_name: str, cursor):
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' AND name=?;
    """, (table_name,))
    return cursor.fetchone() is not None