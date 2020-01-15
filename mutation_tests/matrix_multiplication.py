import numpy as np


class WrongParameters(Exception):
    pass


class WrongShape(Exception):
    pass


def multiply_matrix(a, b):
    if not (isinstance(a, list) or isinstance(a, (np.ndarray, np.generic))) \
            or not (isinstance(b, list) or isinstance(b, (np.ndarray, np.generic))):
        raise WrongParameters()

    a, b = np.array(a), np.array(b)

    shape_a, shape_b = a.shape, b.shape
    # print(shape_a)
    # print(shape_b)
    if shape_a[1] != shape_b[0]:
        raise WrongShape()

    x, y = min(shape_a[0], shape_b[0]), min(shape_a[1], shape_b[1])
    output = np.zeros((x, y))

    # iterate over all a rows
    for row_a in range(0, shape_a[0]):
        for column_a in range(0, shape_a[1]):
            # print(a[row_a][column_a])

            for column_b in range(0, shape_b[1]):
                output[row_a][column_b] += a[row_a][column_a] * b[column_a][column_b]
    return output
