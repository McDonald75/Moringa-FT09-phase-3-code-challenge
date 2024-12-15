from database.connection import cursor, conn

class Author:
    def __init__(self,id, name):
        self._id = id
        self._name = name


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):
            if isinstance(value, str) and len(value) > 0:
                self._name = value
            else:
                raise ValueError("Name must be a non-empty string")
        else:
            raise AttributeError("Cannot change name after initialization")

    def articles(self):
        cursor.execute("""
            SELECT articles.id, articles.title, magazines.id, magazines.name, magazines.category
            FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """, (self.id,))
        articles = cursor.fetchall()
        return [Article(self, Magazine(row[3], row[4], row[2]), row[1], row[0]) for row in articles]

    def magazines(self):
        cursor.execute("""
            SELECT DISTINCT magazines.id, magazines.name, magazines.category
            FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        return [Magazine(row[1], row[2], row[0]) for row in magazines]
    def __repr__(self):
        return f'<Author {self.name}>'