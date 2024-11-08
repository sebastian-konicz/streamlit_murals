import sqlite3
import pandas as pd

# Połączenie z bazą danych
conn = sqlite3.connect('data/murals.db')

# Wczytanie danych z tabeli 'murals' do DataFrame Pandas
df = pd.read_sql_query("SELECT * FROM murals", conn)

# Zamknięcie połączenia
conn.close()

# Wyświetlenie danych
print(df)