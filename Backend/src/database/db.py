from os import path
import sqlite3
import atexit


class DataBase:
    def __init__(self, database_path: str):
        self.connection = sqlite3.connect(database_path, check_same_thread=False)
        self.cursor = self.connection.cursor()

        atexit.register(self.close)
       
        self.connection.execute('PRAGMA foreign_keys = ON;')
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                register_date DATE NOT NULL DEFAULT CURRENT_DATE,
                streak_start DATE,
                streak INTEGER,
                longer_streak INTEGER
            );
            CREATE TABLE IF NOT EXISTS timers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                start TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                presumed_end TIMESTAMP NOT NULL,
                status INTEGER NOT NULL DEFAULT 0,
                ping_step INTEGER NOT NULL,
                category INTEGER NOT NULL,
                last_ping TIMESTAMP,
                ping_confirmed BOOLEAN NOT NULL DEFAULT 0 CHECK (ping_confirmed IN (0, 1)),
                current_ping TIMESTAMP NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
            );
        ''')
        self.connection.commit()


    def close(self):
        self.connection.close()


DATABASE_PATH = path.abspath(path.join(path.dirname(__file__), 'database.db'))

db = DataBase(DATABASE_PATH)

