class Author:
    def __init__(self, name, surname, birth_date, nationality):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.nationality = nationality

    def __repr__(self):
        return (f"\nAuthor (\n\tname='{self.name}',\n\tsurname='{self.surname}',\n\t"
                f"birth_date='{self.birth_date},\n\tnationality='{self.nationality}\n)\n")
