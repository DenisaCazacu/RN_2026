def print_matrix(matrix: list[list[float]]) -> None:
    for row in matrix:
        print(" ".join(f"{val:.2f}" for val in row))
    print()


def print_vector(vector: list[float]) -> None:
    print("[" + ", ".join(f"{val:.2f}" for val in vector) + "]")
    print()