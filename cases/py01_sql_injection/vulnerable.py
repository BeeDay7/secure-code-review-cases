import sqlite3

def login(conn: sqlite3.Connection, username: str, password: str) -> bool:
    # Flaw: user input is concatenated into the SQL statement.
    query = f"SELECT 1 FROM users WHERE name = '{username}' AND password = '{password}'"
    return conn.execute(query).fetchone() is not None
