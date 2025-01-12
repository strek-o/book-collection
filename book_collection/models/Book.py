class Book:
    def __init__(self, title, author_id, genre_id, release_year):
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.release_year = release_year

    def __repr__(self):
        return (f"\nBook (\n\ttitle='{self.title}',\n\tauthor_id='{self.author_id}',\n\t"
                f"genre_id='{self.genre_id}',\n\trelease_year={self.release_year}\n)\n")
