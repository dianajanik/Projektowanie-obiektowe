from factory_with_prototypes.robot_base import RobotBase
from factory_with_prototypes.singleton import Singleton


class RobotA(RobotBase):

    def __init__(self):
        RobotBase.__init__(self, "A")


class RobotB(RobotBase):

    def __init__(self):
        RobotBase.__init__(self, "B")


class RobotC(RobotBase):

    def __init__(self):
        RobotBase.__init__(self, "C")


class RobotD(RobotBase):

    def __init__(self):
        RobotBase.__init__(self, "D")


class RobotsChandler(metaclass=Singleton):

    def __init__(self):
        self.robot_prototypes = {}

    def add_new_prototype(self, identifier, instance):
        self.robot_prototypes[identifier] = instance

    def delete_prototype(self, identifier):
        del self.robot_prototypes[identifier]

    def get_clone(self, identifier):
        return self.robot_prototypes[identifier].clone()
