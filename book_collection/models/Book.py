class Book:
    def __init__(self, title, author_id, genre_id, release_year):
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.release_year = release_year

    def __repr__(self):
        return (f"Book(title='{self.title}', author_id='{self.author_id}',"
                f"genre_id='{self.genre_id}', release_year={self.release_year})")
