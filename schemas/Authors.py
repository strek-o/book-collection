from config.database import connect


def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Authors (
            author_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            birth_date INTEGER NOT NULL,
            nationality TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def drop_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS Authors
    ''')
    conn.commit()
    conn.close()
