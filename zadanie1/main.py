from zadanie1.list_dao import ListDao
from zadanie1.dictionary_dao import DictionaryDao
from zadanie1.book import Book
from zadanie1.person import Person


def test_dao(dao):
    a = Book(1, "Games of Throne", "Gorge R.R Martin", 820)
    b = Book(2, "Some book", "Some author", 100)
    dao.save(a)
    dao.save(b)
    c = Person(3, "Jane", "Doe", 23, "female")
    dao.save(c)
    dao.read_all()
    dao.update(2, ["Cat's Cradle", "Kurt Vonnegut", 205])
    dao.read_element(2)
    dao.delete(3)
    dao.delete(8)
    dao.read_all()


if __name__ == "__main__":
    dict_dao = DictionaryDao()
    test_dao(dict_dao)

    list_dao = ListDao()
    test_dao(list_dao)





