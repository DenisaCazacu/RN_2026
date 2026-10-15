import math

def minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def determinant(matrix: list[list[float]]) -> float | None:
    size = len(matrix)

    if size == 1:
        return matrix[0][0]

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if size == 3:
        return (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
        )

    det = 0
    for c in range(size):
        m = minor(matrix, 0, c)
        det_minor = determinant(m)
        det += ((-1) ** c) * matrix[0][c] * det_minor

    return det
    
def trace(matrix: list[list[float]]) -> float:
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("Expected a square matrix")

    return sum(matrix[i][i] for i in range(size))

def norm(vector: list[float]) -> float:
    return math.sqrt(sum(x ** 2 for x in vector))

def transpose(matrix: list[list[float]]) -> list[list[float]]:
    transpose = [list() for _ in range(len(matrix[0]))]

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transpose[i].append(matrix[j][i])

    return transpose

def multiply(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(vector)
    m = len(matrix)

    if m != n:
        raise ValueError("Incompatible dimensions for matrix-vector multiplication")
    
    result = [0.0 for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i] += matrix[i][j] * vector[j]
    return result