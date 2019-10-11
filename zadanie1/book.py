from zadanie1.i_storage_object import IStoregeObject


class Book(IStoregeObject):

    def __init__(self, id, title, author, n_pages):
        IStoregeObject.__init__(self, id)
        self.title = title
        self.author = author
        self.n_pages = n_pages

    def print_me(self):
        print("Title: {} \n Author: {} \n Number of pages: {}".format(self.title, self.author, self. n_pages))

    def update(self, params):
        self.title = params[0]
        self.author = params[1]
        self.n_pages = params[2]

