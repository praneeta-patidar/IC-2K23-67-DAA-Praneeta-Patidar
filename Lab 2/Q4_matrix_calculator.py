def display_matrix(matrix):
    print("\nResult:")
    for row in matrix:
        print(row)


def input_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []

    for i in range(rows):
        while True:
            row = list(
                map(int, input(f"Enter row {i + 1}: ").split())
            )

            if len(row) == cols:
                matrix.append(row)
                break

            print("Please enter exactly", cols, "elements.")

    return matrix


def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Addition not possible. Dimensions must be the same.")
        return

    result = []

    for i in range(len(a)):
        row = []

        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])

        result.append(row)

    display_matrix(result)


def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        print(
            "Multiplication not possible. "
            "Columns of first matrix must equal rows of second."
        )
        return

    result = [
        [0 for _ in range(len(b[0]))]
        for _ in range(len(a))
    ]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    display_matrix(result)


def transpose_matrix(matrix):
    result = [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]

    display_matrix(result)


def determinant(matrix):
    n = len(matrix)

    if n == 2:
        return (
            matrix[0][0] * matrix[1][1]
            - matrix[0][1] * matrix[1][0]
        )

    if n == 3:
        return (
            matrix[0][0] * (
                matrix[1][1] * matrix[2][2]
                - matrix[1][2] * matrix[2][1]
            )
            - matrix[0][1] * (
                matrix[1][0] * matrix[2][2]
                - matrix[1][2] * matrix[2][0]
            )
            + matrix[0][2] * (
                matrix[1][0] * matrix[2][1]
                - matrix[1][1] * matrix[2][0]
            )
        )

    return None


while True:

    print("\n MATRIX CALCULATOR ")
    print("1. Add two matrices")
    print("2. Multiply two matrices")
    print("3. Transpose a matrix")
    print("4. Find determinant")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print("\nEnter Matrix 1:")
        matrix1 = input_matrix()

        print("\nEnter Matrix 2:")
        matrix2 = input_matrix()

        add_matrices(matrix1, matrix2)

    elif choice == 2:

        print("\nEnter Matrix 1:")
        matrix1 = input_matrix()

        print("\nEnter Matrix 2:")
        matrix2 = input_matrix()

        multiply_matrices(matrix1, matrix2)

    elif choice == 3:

        print("\nEnter Matrix:")
        matrix = input_matrix()

        print("\nTranspose:")
        transpose_matrix(matrix)

    elif choice == 4:

        print("\nEnter Matrix:")
        matrix = input_matrix()

        if len(matrix) != len(matrix[0]):
            print("Determinant can only be calculated for a square matrix.")

        elif len(matrix) in [2, 3]:

            result = determinant(matrix)
            print("\nDeterminant =", result)

        else:
            print("Only 2x2 and 3x3 matrices are supported.")

    elif choice == 5:

        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")
