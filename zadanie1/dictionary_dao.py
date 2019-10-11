from zadanie1.i_dao import IDao


class DictionaryDao(IDao):
    def __init__(self):
        self.storege = dict()

    def read_all(self):
        print("Reading all elements: ")
        for key in self.storege.keys():
            self.storege[key].print_me()

    def read_element(self, id):
        print("Reading one element with id {}".format(id))
        try:
            self.storege[id].print_me()
        except:
            print("There is no element with given id!")

    def save(self, storage_object):
        print("Saving an element with id {}".format(storage_object.id))
        # check if there is no element with this id
        if storage_object.id not in self.storege.keys():
            self.storege[storage_object.id] = storage_object
        else:
            print("There is already an element with this id!")

    def update(self, id, params):
        print("Updating element with id {}".format(id))
        try:
            element = self.storege[id]
        except:
            print("There is no element with given id!")
            return

        element.update(params)
        self.storege[id] = element

    def delete(self, id):
        print("Deleting element with id {}".format(id))
        try:
            del self.storege[id]
        except:
            print("There is no element with given id!")
