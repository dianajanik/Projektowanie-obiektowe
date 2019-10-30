from abc import abstractmethod, ABC


class Organelle(ABC):

    @abstractmethod
    def to_string(self):
        pass


class IAnimalOrganelle(ABC):
    pass


class IPlantOrganelle(ABC):
    pass


class ProtectiveLayer(Organelle, ABC):
    pass


class Membrane(ProtectiveLayer, ABC):
    pass


class CellWall(ProtectiveLayer, IPlantOrganelle):
    def to_string(self):
        print("I am cell wall")


class CellMembrane(Membrane, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am cell membrane")


class TesticleMembrane(Membrane, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am testicle membrane")


class CellTesticle(Organelle, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am cell testicle")


class Cytoplasm(Organelle, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am cytoplasm")


class EndoplasmicReticulum(Organelle, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am endoplasmic reticulum")


class Ribosome(Organelle, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am ribosome")


class Mitochondrion(Organelle, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am mitochondrion")


class Vacuole(Organelle, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am vacuole")


class Lysosome(Organelle, IAnimalOrganelle, IPlantOrganelle):
    def to_string(self):
        print("I am lysosome")


class Chloroplast(Organelle, IPlantOrganelle):
    def to_string(self):
        print("I am chloroplast")