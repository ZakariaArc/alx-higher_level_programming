#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        return m_a * m_b
    """
    return numpy.matmul(m_a, m_b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
