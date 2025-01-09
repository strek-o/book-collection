import schemas.Authors as sA
import schemas.Genres as sG
import schemas.Books as sB
import models.Author as mA
import models.Genre as mG
import models.Book as mB
import service.queries as q


def initialize_database():
    sA.create_table()
    sG.create_table()
    sB.create_table()


def terminate_database():
    sA.drop_table()
    sG.drop_table()
    sB.drop_table()
