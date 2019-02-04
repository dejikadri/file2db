import sqlite3

def connect_db():
    conn = sqlite3.connect('db/movie_stars_db.db')
    return conn

def close_db_con(conn):
    conn.close()
