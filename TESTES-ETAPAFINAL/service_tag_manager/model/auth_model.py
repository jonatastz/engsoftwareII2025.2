import hashlib
import sqlite3


def _hash(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()


class AuthModel:
    def __init__(self, db_path: str = "equipamentos.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self._ensure()

    def _ensure(self):
        c = self.conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                display_name TEXT
            )
        """)
        c.execute("SELECT COUNT(*) FROM users")
        if c.fetchone()[0] == 0:
            c.execute(
                "INSERT INTO users (username, password_hash, display_name) VALUES (?,?,?)",
                ("admin", _hash("admin"), "Administrador"),
            )
        self.conn.commit()

    def validate(self, username: str, password: str):
        if not username or not password:
            return False, {}
        c = self.conn.cursor()
        c.execute(
            "SELECT id, username, display_name, password_hash FROM users WHERE username=?",
            (username,),
        )
        r = c.fetchone()
        if not r:
            return False, {}
        uid, uname, dname, ph = r
        return (ph == _hash(password)), {"id": uid, "username": uname, "display_name": dname}
