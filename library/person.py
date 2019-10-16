from library.i_storage_object import IStoregeObject


class Person(IStoregeObject):

    def __init__(self, id, name, surname, age, sex, punishment=0):
        IStoregeObject.__init__(self, id)
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.punishment = punishment

    def print_me(self):
        print("Name: {} \n Surname: {} \n Age: {} \n Sex: {}, Punishment: {}".format(self.name, self.surname, self.age, self.sex, self.punishment))

    def update(self, params):
        self.name = params[0]
        self.surname = params[1]
        self.age = params[2]
        self.sex = params[3]
        self.punishment = params[4]

