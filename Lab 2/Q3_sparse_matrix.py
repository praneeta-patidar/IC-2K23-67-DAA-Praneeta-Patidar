
def display_matrix(matrix):
    for row in matrix:
        print(row)


def to_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    sparse = [[rows, cols, 0]]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])
                sparse[0][2] += 1

    return sparse


def display_sparse(sparse):
    print("\nSparse Triple Representation:")
    print("(Row, Column, Value)")

    for item in sparse:
        print(tuple(item))


def sparse_to_full(sparse):
    rows = sparse[0][0]
    cols = sparse[0][1]

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    for item in sparse[1:]:
        row, col, value = item
        matrix[row][col] = value

    return matrix


def add_sparse(a, b):
    if a[0][0] != b[0][0] or a[0][1] != b[0][1]:
        return None

    rows = a[0][0]
    cols = a[0][1]

    result = [[rows, cols, 0]]

    i = 1
    j = 1

    while i < len(a) and j < len(b):

        if a[i][0] == b[j][0] and a[i][1] == b[j][1]:

            value = a[i][2] + b[j][2]

            if value != 0:
                result.append([a[i][0], a[i][1], value])
                result[0][2] += 1

            i += 1
            j += 1

        elif (a[i][0], a[i][1]) < (b[j][0], b[j][1]):

            result.append(a[i])
            result[0][2] += 1
            i += 1

        else:

            result.append(b[j])
            result[0][2] += 1
            j += 1

    while i < len(a):
        result.append(a[i])
        result[0][2] += 1
        i += 1

    while j < len(b):
        result.append(b[j])
        result[0][2] += 1
        j += 1

    return result

rows = int(input("Enter rows for Matrix 1: "))
cols = int(input("Enter columns for Matrix 1: "))

matrix1 = []

print("Enter Matrix 1:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)


print("\nEnter Matrix 2:")
matrix2 = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row)


sparse1 = to_sparse(matrix1)
sparse2 = to_sparse(matrix2)

print("\n MATRIX 1 ")
print("Full Matrix:")
display_matrix(matrix1)
display_sparse(sparse1)

print("\n MATRIX 2 ")
print("Full Matrix:")
display_matrix(matrix2)
display_sparse(sparse2)


result_sparse = add_sparse(sparse1, sparse2)

if result_sparse is not None:

    print("\n ADDITION RESULT ")

    display_sparse(result_sparse)

    result_full = sparse_to_full(result_sparse)

    print("\nReconstructed Full Matrix:")
    display_matrix(result_full)

else:
    print("Matrices cannot be added because their dimensions are different.")
