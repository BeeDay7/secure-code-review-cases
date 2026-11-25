import sqlite3

def login(conn: sqlite3.Connection, username: str, password: str) -> bool:
    # Fix: parameterised query; input can never change the SQL structure.
    query = "SELECT 1 FROM users WHERE name = ? AND password = ?"
    return conn.execute(query, (username, password)).fetchone() is not None
