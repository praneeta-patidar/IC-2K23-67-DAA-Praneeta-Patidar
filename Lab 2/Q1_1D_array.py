def display_array(arr):
    print("Current Array:", arr)


def insert_value(arr):
    value = int(input("Enter value to insert: "))
    index = int(input("Enter index: "))

    if 0 <= index <= len(arr):
        arr.insert(index, value)
        print("Value inserted successfully.")
    else:
        print("Invalid index.")

    display_array(arr)


def delete_value(arr):
    index = int(input("Enter index to delete: "))

    if 0 <= index < len(arr):
        deleted = arr.pop(index)
        print("Deleted value:", deleted)
    else:
        print("Invalid index.")

    display_array(arr)


def linear_search(arr):
    value = int(input("Enter value to search: "))

    if value in arr:
        print("Value found at index:", arr.index(value))
    else:
        print("Value not found.")

    display_array(arr)


def left_rotate(arr):
    if len(arr) == 0:
        print("Array is empty.")
        return

    k = int(input("Enter number of positions to rotate left: "))
    k = k % len(arr)

    arr[:] = arr[k:] + arr[:k]

    print("Array after left rotation:")
    display_array(arr)


def right_rotate(arr):
    if len(arr) == 0:
        print("Array is empty.")
        return

    k = int(input("Enter number of positions to rotate right: "))
    k = k % len(arr)

    arr[:] = arr[-k:] + arr[:-k] if k != 0 else arr

    print("Array after right rotation:")
    display_array(arr)


arr = list(map(int, input("Enter array elements separated by spaces: ").split()))

display_array(arr)

while True:
    print("\n===== 1D ARRAY OPERATIONS =====")
    print("1. Insert value")
    print("2. Delete value")
    print("3. Linear search")
    print("4. Left rotation")
    print("5. Right rotation")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_value(arr)

    elif choice == 2:
        delete_value(arr)

    elif choice == 3:
        linear_search(arr)

    elif choice == 4:
        left_rotate(arr)

    elif choice == 5:
        right_rotate(arr)

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
