from draw_shapes.drawer import DrawersProvider
from draw_shapes.shape import Rectangle, Triangle, Circle


if __name__ == "__main__":

    drawers = DrawersProvider().drawers

    for shape in [Rectangle(), Triangle(), Circle()]:

        shape.draw(drawers['pixel'])
        shape.draw(drawers['vector'])
