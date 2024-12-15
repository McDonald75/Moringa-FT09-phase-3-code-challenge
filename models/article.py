
from database.connection import cursor, conn

class Article:
    def __init__(self,id, title, content, author_id, magazine_id):
        self._id = id
        self._author = author_id
        self._magazine = magazine_id
        self.title = title
        self.content = content
        if not id:
            self._save()

    def _save(self):
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                       (self._title, self._author.id, self._magazine.id))
        conn.commit()
        self._id = cursor.lastrowid

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not hasattr(self, '_title'):
            if isinstance(value, str) and 5 <= len(value) <= 50:
                self._title = value
            else:
                raise ValueError("Title must be a string between 5 and 50 characters")
        else:
            raise AttributeError("Cannot change title after initialization")

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
    def __repr__(self):
        return f'<Article {self.title}>'