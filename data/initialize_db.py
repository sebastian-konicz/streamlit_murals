import os
import sqlite3

def create_database():
    # Połączenie z bazą danych (tworzy plik `murals.db`, jeśli jeszcze nie istnieje)
    db_path = os.path.join(os.path.dirname(__file__), 'murals.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    # Tworzenie tabeli murals (jeśli jeszcze nie istnieje)
    c.execute('''
        CREATE TABLE IF NOT EXISTS murals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            lat REAL NOT NULL,
            lon REAL NOT NULL,
            description TEXT,
            image_url TEXT,
            type TEXT
        )
    ''')

    # Opcjonalnie: Dodanie przykładowych danych do tabeli
    sample_murals = [
        ("Mural XYZ", 52.2297, 21.0122, "Opis muralu XYZ", "https://example.com/image_xyz.jpg", 'non-commercial'),
        ("Mural ABC", 52.2300, 21.0200, "Opis muralu ABC", "https://example.com/image_abc.jpg", 'non-commercial')
    ]
    c.executemany("INSERT INTO murals (name, lat, lon, description, image_url, type) VALUES (?, ?, ?, ?, ?, ?)", sample_murals)

    # Zatwierdzenie zmian i zamknięcie połączenia
    conn.commit()
    conn.close()
    print("Baza danych została pomyślnie utworzona wraz z przykładowymi danymi.")

# Uruchomienie funkcji tworzącej bazę danych
if __name__ == "__main__":
    create_database()