from factory_with_prototypes.devices import Devices, PneumaticToaster, HydrokineticBananaPeeler, RetroTV, DeviceModulesList
from factory_with_prototypes.robots import RobotsChandler


class FactoryMethod:

    def __init__(self):
        self.rc = RobotsChandler()

    def create(self, device):

        if device == Devices.RETRO_TV:
            l = DeviceModulesList.RETRO_TV
            modules = [self.rc.robot_prototypes[element].clone().produce() for element in l]
            return RetroTV(modules)
        elif device == Devices.PNEUMATIC_TOSTER:
            l = DeviceModulesList.PNEUMATIC_TOSTER
            modules = [self.rc.robot_prototypes[element].clone().produce() for element in l]
            return PneumaticToaster(modules)
        elif device == Devices.HYDROKINETIC_BANANA_PEELER:
            l = DeviceModulesList.HYDROKINETIC_BANANA_PEELER
            modules = [self.rc.robot_prototypes[element].clone().produce() for element in l]
            return HydrokineticBananaPeeler(modules)
        else:
            raise Exception("Not supported device!")