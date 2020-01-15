import unittest
from matrix_multiplication import WrongShape, WrongParameters
from matrix_multiplication import multiply_matrix
import numpy as np


class MatrixMultiplicationTests(unittest.TestCase):

    def test_illegal_shape(self):

        with self.assertRaises(WrongShape):
            a = [[1,2],[3,4]]
            b = [[2,3,4]]
            multiply_matrix(a, b)

    def test_bad_argument(self):
        with self.assertRaises(WrongParameters) as e:
            a = 'a'
            b = [[2, 3, 4]]
            multiply_matrix(a, b)

    def test_correct_multiply(self):
        a = [[1,2], [3,4]]
        b = [[2], [3]]
        c = multiply_matrix(a, b)
        expected = [[8], [18]]
        self.assertListEqual(c.tolist(), expected)

    def test_correct_multiply2(self):
        a = [[1, 2, 3], [3, 4, 5]]
        b = [[2], [3], [4]]
        c = multiply_matrix(a, b)
        expected = [[20], [38]]
        self.assertListEqual(c.tolist(), expected)


if __name__ == "__main__":
    unittest.main()