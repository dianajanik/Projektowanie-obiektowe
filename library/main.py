from library.list_dao import ListDao
from library.dictionary_dao import DictionaryDao
from library.book import Book
from library.person import Person


def test_dao(dao):
    a = Book(1, "Games of Throne", "Gorge R.R Martin", 820)
    b = Book(2, "Some book", "Some author", 100)
    dao.save(a)
    dao.save(b)
    c = Person(3, "Jane", "Doe", 23, "female")
    dao.save(c)
    dao.read_all()
    dao.update(2, ["Cat's Cradle", "Kurt Vonnegut", 205, 3])
    dao.read_element(2)
    dao.delete(3)
    dao.delete(8)
    dao.read_all()


if __name__ == "__main__":
    dict_dao = DictionaryDao()
    test_dao(dict_dao)

    list_dao = ListDao()
    test_dao(list_dao)

    # check singleton
    dict_dao_2 = DictionaryDao()
    assert dict_dao == dict_dao_2, \
        "Assertion failed -> the instances of dict dao are not same object"

    list_dao_2 = ListDao()
    assert list_dao == list_dao_2, \
        "Assertion failed -> the instances of list dao are not same object"



