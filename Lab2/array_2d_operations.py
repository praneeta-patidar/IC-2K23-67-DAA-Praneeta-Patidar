# 2D Array Operations
# Supports row insertion, row deletion, searching and 90-degree clockwise rotation.


def display_matrix(matrix):
    print("\nMatrix:")
    if not matrix:
        print("Empty matrix")
        return

    for row in matrix:
        print(*row)


def insert_row(matrix):
    try:
        index = int(input("Enter position to insert row: "))

        if index < 0 or index > len(matrix):
            print("Invalid position.")
            return

        if len(matrix) > 0:
            cols = len(matrix[0])
        else:
            cols = int(input("Enter number of columns: "))

        row = []

        print(f"Enter {cols} elements:")
        for i in range(cols):
            row.append(int(input(f"Element {i}: ")))

        matrix.insert(index, row)
        display_matrix(matrix)

    except ValueError:
        print("Invalid input.")


def delete_row(matrix):
    if len(matrix) == 0:
        print("Matrix is empty.")
        return

    try:
        index = int(input("Enter row index to delete: "))

        if index < 0 or index >= len(matrix):
            print("Invalid row index.")
            return

        matrix.pop(index)
        print("Row deleted.")
        display_matrix(matrix)

    except ValueError:
        print("Please enter a valid index.")


def search_value(matrix):
    try:
        value = int(input("Enter value to search: "))

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == value:
                    print(f"Value found at row {i}, column {j}")
                    return

        print("Value not found.")

    except ValueError:
        print("Please enter a valid number.")


def rotate_clockwise(matrix):
    if not matrix:
        print("Matrix is empty.")
        return

    rows = len(matrix)
    cols = len(matrix[0])

    rotated = []

    for j in range(cols):
        new_row = []

        for i in range(rows - 1, -1, -1):
            new_row.append(matrix[i][j])

        rotated.append(new_row)

    matrix[:] = rotated

    print("After 90-degree clockwise rotation:")
    display_matrix(matrix)


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Rows and columns must be positive.")
        return

    matrix = []

    print("Enter matrix elements:")

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(int(input(f"Element [{i}][{j}]: ")))

        matrix.append(row)

    display_matrix(matrix)

    while True:
        print("\n--- 2D Array Menu ---")
        print("1. Insert Row")
        print("2. Delete Row")
        print("3. Search Value")
        print("4. Rotate 90 Degrees Clockwise")
        print("5. Display")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            insert_row(matrix)

        elif choice == "2":
            delete_row(matrix)

        elif choice == "3":
            search_value(matrix)

        elif choice == "4":
            rotate_clockwise(matrix)

        elif choice == "5":
            display_matrix(matrix)

        elif choice == "6":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
