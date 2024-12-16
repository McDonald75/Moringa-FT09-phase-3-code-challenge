from database.connection import cursor
class Magazine:
    def __init__(self,id, name, category='default'):
        self.name = name
        self.category = category
        self.id = id
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise Exception("Invalid Id")
        cursor.execute('''
                       INSERT INTO magazines (name, category) VALUES (?, ?)
                       ''', (self._name, self._category))
        self._id = cursor.lastrowid
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) and 2 <= len(value) <= 16:
            raise Exception("Invalid name")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not (isinstance(value, str) and len(value) > 0):
            raise Exception("invalid category")
        self._category = value

    def articles(self):
       
        pass

    def contributors(self):
        
        pass

    def article_titles(self):
        articles = self.articles()
        return [article.title for article in articles] if articles else None

    def contributing_authors(self):
        
        return [magazine.author for magazine in Magazine.all]
    def __repr__(self):
        return f'<Magazine {self.name}>'