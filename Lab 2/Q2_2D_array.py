def display_matrix(matrix):
    print("\nCurrent Matrix:")
    for row in matrix:
        print(row)


def insert_row(matrix):
    position = int(input("Enter position to insert row: "))

    if 0 <= position <= len(matrix):
        columns = len(matrix[0]) if matrix else int(
            input("Enter number of columns: ")
        )

        new_row = list(
            map(int, input(f"Enter {columns} elements: ").split())
        )

        if len(new_row) == columns:
            matrix.insert(position, new_row)
            print("Row inserted successfully.")
        else:
            print("Invalid number of elements.")
    else:
        print("Invalid position.")

    display_matrix(matrix)


def delete_row(matrix):
    position = int(input("Enter row position to delete: "))

    if 0 <= position < len(matrix):
        matrix.pop(position)
        print("Row deleted successfully.")
    else:
        print("Invalid position.")

    display_matrix(matrix)


def search_value(matrix):
    value = int(input("Enter value to search: "))

    found = False

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                print(f"Value found at row {i}, column {j}")
                found = True
                return

    if not found:
        print("Value not found.")


def rotate_clockwise(matrix):
    if not matrix:
        print("Matrix is empty.")
        return

    rotated = [list(row) for row in zip(*matrix[::-1])]

    matrix.clear()
    matrix.extend(rotated)

    print("Matrix after 90-degree clockwise rotation:")
    display_matrix(matrix)


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(
        map(int, input(f"Enter elements of row {i}: ").split())
    )

    while len(row) != columns:
        print("Please enter exactly", columns, "elements.")
        row = list(
            map(int, input(f"Enter elements of row {i}: ").split())
        )

    matrix.append(row)

display_matrix(matrix)

while True:
    print("\n===== 2D ARRAY OPERATIONS =====")
    print("1. Insert new row")
    print("2. Delete row")
    print("3. Search value")
    print("4. Rotate 90 degrees clockwise")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_row(matrix)

    elif choice == 2:
        delete_row(matrix)

    elif choice == 3:
        search_value(matrix)

    elif choice == 4:
        rotate_clockwise(matrix)

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
