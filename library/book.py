from library.i_storage_object import IStoregeObject


class Book(IStoregeObject):

    def __init__(self, id, title, author, n_pages, user_id=-1):
        IStoregeObject.__init__(self, id)
        self.title = title
        self.author = author
        self.n_pages = n_pages
        self.user_id = user_id  # -1 if no user

    def print_me(self):
        print("Title: {} \n Author: {} \n Number of pages: {}\n User ID: {}".format(self.title, self.author, self. n_pages, self.user_id))

    def update(self, params):
        self.title = params[0]
        self.author = params[1]
        self.n_pages = params[2]
        self.user_id = params[3]

