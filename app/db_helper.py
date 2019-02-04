import sqlite3

def connect_db():
    conn = sqlite3.connect('db/example.db')
    return conn

def close_db_con(conn):
    conn.close()
