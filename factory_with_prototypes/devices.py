class DeviceBase:

    def __init__(self, modules, name):
        self.modules = modules
        self.name = name

    def print_modules(self):
        print("Device name : {} , modules : {}".format(self.name, self.modules))


class PneumaticToaster(DeviceBase):

    def __init__(self, modules):
        DeviceBase.__init__(self, modules, "Pneumatic toaster")


class RetroTV(DeviceBase):

    def __init__(self, modules):
        DeviceBase.__init__(self, modules, "Retro TV")


class HydrokineticBananaPeeler(DeviceBase):

    def __init__(self, modules):
        DeviceBase.__init__(self, modules, "Hydrokinetic banana peeler")


class DeviceModulesList(object):

    PNEUMATIC_TOSTER = ["A", "B", "B", "B", "A", "D"]
    RETRO_TV = ["A", "A","A", "B", "B", "C"]
    HYDROKINETIC_BANANA_PEELER = ["C", "D","A", "D"]


class Devices(object):

    PNEUMATIC_TOSTER = 1
    RETRO_TV = 2
    HYDROKINETIC_BANANA_PEELER = 3