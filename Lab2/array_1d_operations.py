# 1D Array Operations
# Supports insert, delete, linear search, left rotation and right rotation.


def display_array(arr):
    print("Current array:", arr)


def insert_value(arr):
    try:
        index = int(input("Enter index: "))
        value = int(input("Enter value: "))

        if index < 0 or index > len(arr):
            print("Invalid index.")
            return

        arr.insert(index, value)
        display_array(arr)

    except ValueError:
        print("Please enter valid numbers.")


def delete_value(arr):
    try:
        if len(arr) == 0:
            print("Array is empty.")
            return

        index = int(input("Enter index to delete: "))

        if index < 0 or index >= len(arr):
            print("Invalid index.")
            return

        deleted = arr.pop(index)
        print("Deleted value:", deleted)
        display_array(arr)

    except ValueError:
        print("Please enter a valid index.")


def linear_search(arr):
    try:
        value = int(input("Enter value to search: "))

        for i in range(len(arr)):
            if arr[i] == value:
                print("Value found at index:", i)
                return

        print("Value not found.")

    except ValueError:
        print("Please enter a valid number.")


def rotate_left(arr):
    if len(arr) == 0:
        print("Array is empty.")
        return

    try:
        k = int(input("Enter number of positions: "))

        if k < 0:
            print("Number of positions cannot be negative.")
            return

        k = k % len(arr)
        arr[:] = arr[k:] + arr[:k]

        print("After left rotation:")
        display_array(arr)

    except ValueError:
        print("Please enter a valid number.")


def rotate_right(arr):
    if len(arr) == 0:
        print("Array is empty.")
        return

    try:
        k = int(input("Enter number of positions: "))

        if k < 0:
            print("Number of positions cannot be negative.")
            return

        k = k % len(arr)

        if k == 0:
            return

        arr[:] = arr[-k:] + arr[:-k]

        print("After right rotation:")
        display_array(arr)

    except ValueError:
        print("Please enter a valid number.")


def main():
    n = int(input("Enter number of elements: "))

    if n < 0:
        print("Invalid size.")
        return

    arr = []

    for i in range(n):
        value = int(input(f"Enter element {i}: "))
        arr.append(value)

    display_array(arr)

    while True:
        print("\n--- 1D Array Menu ---")
        print("1. Insert")
        print("2. Delete")
        print("3. Linear Search")
        print("4. Rotate Left")
        print("5. Rotate Right")
        print("6. Display")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            insert_value(arr)

        elif choice == "2":
            delete_value(arr)

        elif choice == "3":
            linear_search(arr)

        elif choice == "4":
            rotate_left(arr)

        elif choice == "5":
            rotate_right(arr)

        elif choice == "6":
            display_array(arr)

        elif choice == "7":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
