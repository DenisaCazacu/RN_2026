from pathlib import Path


def parse_term(token: str) -> tuple[str, float]:
    if not token or not token[-1].isalpha():
        raise ValueError("Expected a term ending in a single-letter variable")

    variable = token[-1]
    coefficient = token[:-1]
    if coefficient in ("", "+", "-"):
        coefficient += "1"

    return variable, float(coefficient)


def load_system(path: Path) -> tuple[list[list[float]], list[float]]:
    equations = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            equations.append(line)

    if not equations:
        raise ValueError("Expected at least one equation")

    matrix: list[list[float]] = []
    vector: list[float] = []
    expected_variables: list[str] | None = None

    for line_number, equation in enumerate(equations, start=1):
        if equation.count("=") != 1:
            raise ValueError(f"Line {line_number}: expected one '=' separator")

        left, right = equation.split("=")
        tokens = left.split()
        if not tokens:
            raise ValueError(f"Line {line_number}: expected variable terms")

        terms: list[tuple[str, float]] = []
        try:
            terms.append(parse_term(tokens[0]))
            token_index = 1
            while token_index < len(tokens):
                operator = tokens[token_index]
                if operator not in ("+", "-"):
                    raise ValueError("Expected '+' or '-' between terms")
                if token_index + 1 == len(tokens):
                    raise ValueError("Expected a term after the sign")

                variable, coefficient = parse_term(tokens[token_index + 1])
                if operator == "-":
                    coefficient = -coefficient
                terms.append((variable, coefficient))
                token_index += 2
        except ValueError as error:
            raise ValueError(f"Line {line_number}: {error}") from error

        variables = [variable for variable, _ in terms]
        if len(set(variables)) != len(variables):
            raise ValueError(f"Line {line_number}: each variable must appear once")

        if expected_variables is None:
            expected_variables = variables
        elif variables != expected_variables:
            raise ValueError(
                f"Line {line_number}: variables must appear in the same order "
                "as in the first equation"
            )

        coefficients = [coefficient for _, coefficient in terms]

        try:
            constant = float(right.strip())
        except ValueError as error:
            raise ValueError(f"Line {line_number}: invalid right-hand side") from error

        matrix.append(coefficients)
        vector.append(constant)

    if len(matrix) != len(expected_variables):
        raise ValueError(
            f"Expected a square system, found {len(matrix)} equations "
            f"and {len(expected_variables)} variables"
        )

    return matrix, vector