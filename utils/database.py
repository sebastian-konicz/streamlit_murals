import sqlite3
import pandas as pd

def create_connection():
    conn = sqlite3.connect('data/murals.db')
    return conn

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS murals
                 (id INTEGER PRIMARY KEY, name TEXT, lat REAL, lon REAL, description TEXT, rating REAL)''')
    conn.commit()
    conn.close()

def add_mural(name, lat, lon, description):
    conn = create_connection()
    c = conn.cursor()
    c.execute("INSERT INTO murals (name, lat, lon, description) VALUES (?, ?, ?, ?)", (name, lat, lon, description))
    conn.commit()
    conn.close()

def add_sample_data():
    conn = sqlite3.connect('data/murals.db')
    c = conn.cursor()
    murals = [
        ("Mural XYZ", 52.2297, 21.0122, "Opis muralu XYZ", "https://example.com/image_xyz.jpg"),
        ("Mural ABC", 52.2300, 21.0200, "Opis muralu ABC", "https://example.com/image_abc.jpg")
    ]
    c.executemany("INSERT INTO murals (name, lat, lon, description, image_url) VALUES (?, ?, ?, ?, ?)", murals)
    conn.commit()
    conn.close()

def fetch_murals():
    conn = create_connection()
    query = 'SELECT name, lat, lon, description, image_url FROM murals'
    murals_df = pd.read_sql_query(query, conn)
    conn.close()
    return murals_df
