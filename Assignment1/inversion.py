from matrix_operations import determinant, minor, transpose, multiply

def cofactor(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    cof = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor_matrix = minor(matrix, i, j)
            det_minor = determinant(minor_matrix)
            cof[i][j] = ((-1) ** (i + j)) * det_minor
    return cof

def inverse(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)

    adjugate_matrix = transpose(cofactor(matrix))
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted")
    return [[adjugate_matrix[i][j] / det for j in range(n)] for i in range(n)]


def solve_inversion(A: list[list[float]], B: list[float]) -> list[float]:
    inv_A = inverse(A)
    n = len(B)
    return multiply(inv_A, B)