from abc import abstractmethod
from cell_builder.organellas import Organelle
from cell_builder.organellas import IAnimalOrganelle, IPlantOrganelle, Membrane, CellTesticle
import random
from cell_builder.cell import PlantCall, AnimalCell


class CellBuilder:
    def __init__(self):
        self.all_organelles = self._get_all_available_organelles()

    @staticmethod
    def _get_all_available_organelles():
        subclasses = set()
        work = [Organelle]
        while work:
            parent = work.pop()
            for child in parent.__subclasses__():
                if child not in subclasses:
                    subclasses.add(child)
                    work.append(child)
        return list(subclasses)

    @abstractmethod
    def create_cell(self):
        pass


class PlantCellBuilder(CellBuilder):


    def __init__(self):
        CellBuilder.__init__(self)

    def create_cell(self):
        organelles = []
        for O in self.all_organelles:
            if issubclass(O, IPlantOrganelle):  # organelle of plant cell
                n = 1 if issubclass(O, Membrane) or issubclass(O, CellTesticle) else random.randint(1, 5)
                for i in range(n):
                    organelles.append(O())

        return PlantCall(organelles)


class AnimalCellBuilder(CellBuilder):

    def __init__(self):
        CellBuilder.__init__(self)

    def create_cell(self):
        organelles = []
        for O in self.all_organelles:
            if issubclass(O, IAnimalOrganelle):  # organelle of animal cell
                n = 1 if issubclass(O, Membrane) or issubclass(O, CellTesticle) else random.randint(1, 5)
                for i in range(n):
                    organelles.append(O())

        return AnimalCell(organelles)
