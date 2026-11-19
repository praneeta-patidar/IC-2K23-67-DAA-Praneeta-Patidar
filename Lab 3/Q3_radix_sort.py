def counting_sort_by_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    # Count occurrences of each digit
    for number in arr:
        digit = (number // exp) % 10
        count[digit] += 1

    # Convert count into positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // exp) % 10

        output[count[digit] - 1] = arr[i]

        count[digit] -= 1

    return output


def radix_sort(arr):
    if len(arr) == 0:
        return []

    if any(number < 0 for number in arr):
        raise ValueError(
            "Radix Sort only supports non-negative integers."
        )

    a = arr.copy()

    print("\n--- Radix Sort ---")
    print("Initial:", a)

    max_value = max(a)

    exp = 1

    while max_value // exp > 0:
        a = counting_sort_by_digit(a, exp)

        print(
            f"After sorting by digit place {exp}: {a}"
        )

        exp *= 10

    return a


sample = [170, 45, 75, 90, 802, 24, 2, 66]

print("Original Array:", sample)

result = radix_sort(sample)

print("Radix Sort Result:", result)

print("Original array remains:", sample)
