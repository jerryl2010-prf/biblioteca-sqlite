import sqlite3

conn = sqlite3.connect("biblioteca.db")
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
"""
)
conn.executemany("INSERT INTO usuarios(nome) VALUES(?)",
                 [("Bob",), ("Sam",), ("Frodo",)])
conn.commit()