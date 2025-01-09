class Author:
    def __init__(self, name, surname, birth_date, nationality):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.nationality = nationality

    def __repr__(self):
        return (f"Author(name='{self.name}', surname='{self.surname}',"
                f"birth_date='{self.birth_date}, nationality='{self.nationality})")
