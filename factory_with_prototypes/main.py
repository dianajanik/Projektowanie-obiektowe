from factory_with_prototypes.robots import RobotsChandler, RobotB, RobotA, RobotC, RobotD
from factory_with_prototypes.factory_method import FactoryMethod
from factory_with_prototypes.devices import Devices, PneumaticToaster, HydrokineticBananaPeeler, RetroTV, DeviceModulesList

if __name__ == "__main__":

    robot_chandler = RobotsChandler()
    robot_chandler.add_new_prototype("A", RobotA())
    robot_chandler.add_new_prototype("B", RobotB())
    robot_chandler.add_new_prototype("C", RobotC())
    robot_chandler.add_new_prototype("D", RobotD())

    my_factory = FactoryMethod()

    for device in [1, 2, 3]:
        d = my_factory.create(device)
        d.print_modules()

