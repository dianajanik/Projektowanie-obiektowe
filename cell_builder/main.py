
from cell_builder.builder import PlantCellBuilder, AnimalCellBuilder

def test(builder, name):
    cell = builder.create_cell()
    print("{} cell contains : \n".format(name))
    for x in cell.organelles:
        x.to_string()
    print("\nend \n")


if __name__ == "__main__":
    plant_builder = PlantCellBuilder()
    test(plant_builder, "Plant ")
    animal_builder = AnimalCellBuilder()
    test(animal_builder, "Animal ")


