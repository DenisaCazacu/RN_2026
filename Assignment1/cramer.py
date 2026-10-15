from matrix_operations import determinant

def replace_column(matrix: list[list[float]], col_index: int, new_col: list[float]) -> list[list[float]]:
    n = len(matrix)
    replaced = []
    for i in range(n):
        replaced.append([new_col[i] if j == col_index else matrix[i][j] for j in range(n)])
    return replaced

def solve_cramer(A: list[list[float]], B: list[float]) -> list[float]:
    n = len(A)
    det_A = determinant(A)
    if det_A == 0:
        raise ValueError("The system has no unique solution")

    solutions = [0] * n
    for i in range(n):
        A_i = replace_column(A, i, B)
        det_A_i = determinant(A_i)
        if det_A_i == 0:
            raise ValueError(f"The system has no unique solution for column {i}")
        solutions[i] = det_A_i / det_A
    return solutions