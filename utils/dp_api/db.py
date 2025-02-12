import sqlite3


# from data.config import DATABASE_PATH


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('data/database.db')
        self.cursor = self.connection.cursor()
        self.create_instagram()
        self.create_youtube()
        self.create_tik_tok()
        self.create_youtube()

    # INSTAGRAM uchun ma'lumotlar ombori(DataBase)
    def create_instagram(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS instagram (
            id INTEGER PRIMARY KEY,
            title VARCHAR,
            url VARCHAR
        )
        """)

    def instagram_add_url(self, title, url):
        self.cursor.execute("insert into instagram (title, url) values (?, ?)",
                            (title, url))
        self.connection.commit()

    def instagram_all_urls(self):
        self.cursor.execute("select * from instagram")
        return self.cursor.fetchall()

    # Youtube uchun ma'lumotlar ombori(DataBase)
    def create_youtube(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS youtube (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            url TEXT
        )
        """)

    def youtube_add_url(self, title, url):
        self.cursor.execute("insert into youtube (title, url) values (?, ?)",
                            (title, url))
        self.connection.commit()

    def youtube_all_urls(self):
        self.cursor.execute("select * from youtube")
        return self.cursor.fetchall()

    # TikTok uchun ma'lumotlar ombori(DataBase)
    def create_tik_tok(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tik_tok (
            id INTEGER PRIMARY KEY,
            title VARCHAR,
            url VARCHAR
        )
        """)

    def tiktok_add_url(self, title, url):
        self.cursor.execute("insert into tik_tok (title, url) values (?, ?)",
                            (title, url))
        self.connection.commit()

    def tiktok_all_urls(self):
        self.cursor.execute("select * from tik_tok")
        return self.cursor.fetchall()

    # FaceBook uchun ma'lumotlar ombori(DataBase)
    def create_facebook(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS facebook (
            id INTEGER PRIMARY KEY,
            title VARCHAR,
            url VARCHAR
        )
        """)

    def facebook_add_url(self, title, url):
        self.cursor.execute("insert into facebook (title, url) values (?, ?)",
                            (title, url))
        self.connection.commit()

    def facebook_all_urls(self):
        self.cursor.execute("select * from facebook")
        return self.cursor.fetchall()

    # pinterest uchun ma'lumotlar ombori(DataBase)
    def create_pinterest(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pinterest (
            id INTEGER PRIMARY KEY,
            title VARCHAR,
            url VARCHAR,
        )
        """)

    def pinterest_add_url(self, title, url):
        self.cursor.execute("insert into pinterest (title, url) values (?, ?)",
                            (title, url))
        self.connection.commit()

    def pinterest_all_urls(self):
        self.cursor.execute("select * from pinterest")
        return self.cursor.fetchall()

    # Snapchat uchun ma'lumotlar ombori(DataBase)

    def create_snapchat(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS snapchat (
            id INTEGER PRIMARY KEY,
            title VARCHAR,
            url VARCHAR,
        )
        """)

    def snapchat_add_url(self, title, url):
        self.cursor.execute("insert into snapchat (title, url) values (?, ?)",
                            (title, url))
        self.connection.commit()

    def snapchat_all_urls(self):
        self.cursor.execute("select * from snapchat")

        return self.cursor.fetchall()
