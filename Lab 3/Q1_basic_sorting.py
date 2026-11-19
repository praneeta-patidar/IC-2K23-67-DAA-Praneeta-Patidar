def bubble_sort(arr):
    a = arr.copy()

    print("\n--- Bubble Sort ---")
    print("Initial:", a)

    n = len(a)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        print(f"After pass {i + 1}: {a}")

        if not swapped:
            break

    return a


def selection_sort(arr):
    a = arr.copy()

    print("\n--- Selection Sort ---")
    print("Initial:", a)

    n = len(a)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]

        print(f"After pass {i + 1}: {a}")

    return a


def insertion_sort(arr):
    a = arr.copy()

    print("\n--- Insertion Sort ---")
    print("Initial:", a)

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key

        print(f"After pass {i}: {a}")

    return a

sample = [64, 25, 12, 22, 11]

print("Original Array:", sample)

result1 = bubble_sort(sample)
print("Bubble Sort Result:", result1)

result2 = selection_sort(sample)
print("Selection Sort Result:", result2)

result3 = insertion_sort(sample)
print("Insertion Sort Result:", result3)

print("\nOriginal array remains:", sample)
