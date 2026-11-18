import random, sqlite3, string, validators
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "shorty.db"


def _connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    with _connect() as conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY,
                url TEXT NOT NULL,
                short TEXT UNIQUE NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )"""
        )


def all_entries():
    """Return all entries oldest first."""
    with _connect() as conn:
        rows = conn.execute("SELECT id, url, short FROM links ORDER BY id").fetchall()
    return [dict(row) for row in rows]


def short_exists(short):
    with _connect() as conn:
        row = conn.execute("SELECT 1 FROM links WHERE short = ?", (short,)).fetchone()
    return row is not None


def create_short():
    short = "".join(random.choices(string.ascii_letters, k=5))
    while short_exists(short):
        short = "".join(random.choices(string.ascii_letters, k=5))
    return short


def validate_url(url):
    url = url.strip()
    if not url.startswith(("https://", "http://")):
        url = "https://" + url

    return url if validators.url(url) else None


def add_entry(url, short):
    """Store a new entry and return it."""
    with _connect() as conn:
        cur = conn.execute("INSERT INTO links (url, short) VALUES (?, ?)", (url, short))
    return {"id": cur.lastrowid, "url": url, "short": short}


def search_for_url(short_url):
    with _connect() as conn:
        row = conn.execute("SELECT url FROM links WHERE short = ?", (short_url,)).fetchone()
    return row["url"] if row else None


init_db()
