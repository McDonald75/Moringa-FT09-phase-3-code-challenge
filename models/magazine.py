from .author import Author
from .article import Article

class Magazine:
    def __init__(self,id, name, category='default'):
        self._id = id
        self.name = name
        self.category = category
        
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
            
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
            
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
       
        return [Article(Author(row[3], row[2]), self, row[1], row[0]) for row in articles]

    def contributors(self):
        
        return [Author(row[1], row[0]) for row in Author.all]

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        
        return [magazine.author for magazine in Magazine.all]
    def __repr__(self):
        return f'<Magazine {self.name}>'