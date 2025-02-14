import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('data/database.db')
        self.cursor = self.connection.cursor()
        self.create_instagram()
        self.create_youtube()
        self.create_tik_tok()
        self.create_facebook()
        self.create_pinterest()
        self.create_snapchat()

    # Instagram Table
    def create_instagram(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS instagram (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            url TEXT
        )
        """)

    def instagram_add_url(self, user_id, title, url):
        self.cursor.execute("INSERT INTO instagram (user_id, title, url) VALUES (?, ?, ?)",
                            (user_id, title, url))
        self.connection.commit()

    def instagram_all_urls(self):
        self.cursor.execute("SELECT * FROM instagram")
        return self.cursor.fetchall()

    # YouTube Table
    def create_youtube(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS youtube (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            url TEXT
        )
        """)

    def youtube_add_url(self, user_id, title, url):
        self.cursor.execute("INSERT INTO youtube (user_id, title, url) VALUES (?, ?, ?)",
                            (user_id, title, url))
        self.connection.commit()

    def youtube_all_urls(self):
        self.cursor.execute("SELECT * FROM youtube")
        return self.cursor.fetchall()

    # TikTok Table
    def create_tik_tok(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tik_tok (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            url TEXT
        )
        """)

    def tiktok_add_url(self, user_id, title, url):
        self.cursor.execute("INSERT INTO tik_tok (user_id, title, url) VALUES (?, ?, ?)",
                            (user_id, title, url))
        self.connection.commit()

    def tiktok_all_urls(self):
        self.cursor.execute("SELECT * FROM tik_tok")
        return self.cursor.fetchall()

    # Facebook Table
    def create_facebook(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS facebook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            url TEXT
        )
        """)

    def facebook_add_url(self, user_id, title, url):
        self.cursor.execute("INSERT INTO facebook (user_id, title, url) VALUES (?, ?, ?)",
                            (user_id, title, url))
        self.connection.commit()

    def facebook_all_urls(self):
        self.cursor.execute("SELECT * FROM facebook")
        return self.cursor.fetchall()

    # Pinterest Table
    def create_pinterest(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pinterest (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            url TEXT
        )
        """)

    def pinterest_add_url(self, user_id, title, url):
        self.cursor.execute("INSERT INTO pinterest (user_id, title, url) VALUES (?, ?, ?)",
                            (user_id, title, url))
        self.connection.commit()

    def pinterest_all_urls(self):
        self.cursor.execute("SELECT * FROM pinterest")
        return self.cursor.fetchall()

    # Snapchat Table
    def create_snapchat(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS snapchat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT,
            url TEXT
        )
        """)

    def snapchat_add_url(self, user_id, title, url):
        self.cursor.execute("INSERT INTO snapchat (user_id, title, url) VALUES (?, ?, ?)",
                            (user_id, title, url))
        self.connection.commit()

    def snapchat_all_urls(self):
        self.cursor.execute("SELECT * FROM snapchat")
        return self.cursor.fetchall()
