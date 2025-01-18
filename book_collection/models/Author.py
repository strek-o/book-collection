class Author:
    def __init__(self, name, surname, birth_date, nationality):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.nationality = nationality

    def __repr__(self):
        return (f"\nAuthor (\n\tname='{self.name}',"
                f"\n\tsurname='{self.surname}',"
                f"\n\tbirth_date='{self.birth_date},"
                f"\n\tnationality='{self.nationality}\n)\n")
