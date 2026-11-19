def merge_sort(arr):
    a = arr.copy()

    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def divide(values):
        if len(values) <= 1:
            return values

        mid = len(values) // 2

        left = divide(values[:mid])
        right = divide(values[mid:])

        merged = merge(left, right)

        print(f"Merge step: {merged}")

        return merged

    print("\n--- Merge Sort ---")
    print("Initial:", a)

    return divide(a)


def quick_sort(arr):
    a = arr.copy()

    # Quick Sort uses the LAST element as pivot.

    def partition(low, high):
        pivot = a[high]

        i = low - 1

        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]

        return i + 1

    def quicksort(low, high):
        if low < high:
            pivot_index = partition(low, high)

            print(
                f"Pivot {a[pivot_index]} -> {a}"
            )

            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    print("\n--- Quick Sort ---")
    print("Initial:", a)

    quicksort(0, len(a) - 1)

    return a


def heap_sort(arr):
    a = arr.copy()

    print("\n--- Heap Sort ---")
    print("Initial:", a)

    n = len(a)

    def heapify(size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        if left < size and a[left] > a[largest]:
            largest = left

        if right < size and a[right] > a[largest]:
            largest = right

        if largest != root:
            a[root], a[largest] = a[largest], a[root]
            heapify(size, largest)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    print("Max heap:", a)

    # Extract elements
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(i, 0)

        print(f"After extraction: {a}")

    return a


sample = [38, 27, 43, 3, 9, 82, 10]

print("Original Array:", sample)

result1 = merge_sort(sample)
print("Merge Sort Result:", result1)

result2 = quick_sort(sample)
print("Quick Sort Result:", result2)

result3 = heap_sort(sample)
print("Heap Sort Result:", result3)

print("\nOriginal array remains:", sample)
