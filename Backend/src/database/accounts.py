import sqlite3


class Accounts:
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor


    def is_registered(self, user_id: int) -> bool:
        self.cursor.execute('SELECT 1 FROM users WHERE user_id = ?', (user_id,))
        row = self.cursor.fetchone()
        return row is not None


    def register_user(self, user_id: int) -> None:
        self.cursor.execute('INSERT OR IGNORE INTO users (user_id) VALUES (?)', (user_id,))
        self.connection.commit()


    def delete_user(self, user_id: int) -> None:
        self.cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        self.connection.commit()

