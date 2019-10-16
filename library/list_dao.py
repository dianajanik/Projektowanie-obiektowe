from library.i_dao import IDao
from library.singleton import Singleton
from library.person import Person
from library.book import Book


class ListDao(IDao, metaclass=Singleton):

    def __init__(self):
        self.storege = []

    def read_all(self):
        print("Reading all elements: ")
        for element in self.storege:
            element.print_me()

    def read_element(self, id):
        print("Reading one element with id {}".format(id))
        element = self._find_element_by_id(id)
        if element is not None:
            element.print_me()
        else:
            print("There is no element with given id!")

    def save(self, storage_object):
        print("Saving an element with id {}".format(storage_object.id))
        # check if there is no element with this id
        element = self._find_element_by_id(storage_object.id)
        if element:
            print("There is already an element with this id!")
            return

        self.storege.append(storage_object)

    def update(self, id, params):
        print("Updating element with id {}".format(id))
        element = self._find_element_by_id(id)
        self.storege.remove(element)
        element.update(params)
        self.storege.append(element)

    def delete(self, id):
        print("Deleting element with id {}".format(id))
        element = self._find_element_by_id(id)
        if element is not None:
            # remove id in each book if removing a person
            if isinstance(element, Person):
                self.return_books_by_person(element.id)
            self.storege.remove(element)
        else:
            print("There is no element with given id!")

    def _find_element_by_id(self, id):
        for element in self.storege:
            if element.id == id:
                return element
        return None

    def return_books_by_person(self, person_id):
        for element in self.storege:
            if isinstance(element, Book):
                if element.user_id == person_id:
                    element.user_id = -1
                    print("Returning book {} by user with ID : {}".format(element.id, person_id))
