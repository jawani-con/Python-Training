import numpy as np
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply_matrices(matrix1, matrix2):
        try:
            result = np.dot(matrix1, matrix2)
            return result
        except ValueError:
            return "Matrix dimensions do not align for multiplication"
