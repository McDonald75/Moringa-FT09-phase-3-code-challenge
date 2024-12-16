
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
    def author(self):
        cursor.execute("SELECT authors.* FROM articles JOIN authors ON articles.author_id = authors.id  WHERE articles.author_id == ?  LIMIT 1 ", (self.author_id))
        author = cursor.fetchone()
        return author
    def magazine(self):
        cursor.execute("SELECT authors.* FROM articles JOIN authors ON articles.author_id = authors.id  WHERE articles.author_id == ?  LIMIT 1 ", (self.author_id))
        author = cursor.fetchone()
        return author
        
    def __repr__(self):
        return f'<Article {self.title}>'