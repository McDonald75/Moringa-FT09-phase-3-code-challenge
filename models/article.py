
from database.connection import cursor, conn
from .author import Author
from .magazine import Magazine
class Article:
    def __init__(self,id,title, content, author_id, magazine_id):
        self.id = id
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.content = content
        self.title = title
        self._save()
        
        
    def _save(self):
        cursor.execute("INSERT INTO articles (title,content, author_id, magazine_id) VALUES (?,?, ?, ?)",
                       (self._title,self.content, self.author_id, self.magazine_id))
        conn.commit()
        self._id = cursor.lastrowid

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, 'title') or (not isinstance(value, str) and not 5 <= len(value) <= 50):
            raise Exception('Invalid title')
        self._title = value
        
    def __repr__(self):
        return f'<Article {self.title}>'