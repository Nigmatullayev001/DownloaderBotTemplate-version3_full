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
        self.create_pinterest()

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
        """Creates a table for Pinterest URLs if it doesn't exist."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS pinterest (
                    id integer primary key,
                    title TEXT NOT NULL,
                    url TEXT NOT NULL UNIQUE
                )
            """)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            self.connection.rollback()

    def pinterest_add_url(self, title, url):
        """Adds a Pinterest URL with a title into the database."""
        try:
            self.cursor.execute("INSERT INTO pinterest (title, url) VALUES (?, ?)", (title, url))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Error: The URL '{url}' already exists in the database.")
        except sqlite3.Error as e:
            print(f"Error adding Pinterest URL: {e}")
            self.connection.rollback()

    def pinterest_all_urls(self):
        """Fetches all Pinterest URLs from the database."""
        try:
            self.cursor.execute("SELECT * FROM pinterest")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching Pinterest URLs: {e}")
            return []

    def close(self):
        """Closes the connection to the database."""
        self.connection.close()

    # Snapchat uchun ma'lumotlar ombori(DataBase)

    def create_snapchat(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS snapchat (
            id INTEGER,
            title VARCHAR,
            url VARCHAR,
        )
        """)

    def snapchat_add_url(self, id, title, url):
        self.cursor.execute("insert into snapchat (id, title, url) values (?, ?, ?)",
                            (id, title, url))
        self.connection.commit()

    def snapchat_all_urls(self):
        self.cursor.execute("select * from snapchat")

        return self.cursor.fetchall()
