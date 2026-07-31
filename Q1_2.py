# PART 1: Trace it yourself given list:8,3,15,6,2
# Sort this list from smallest to largest using any method you like. Write down the steps you followed.

A = [8, 3, 15, 6, 2]
print(A)
n = len(A)

for i in range(n):
    for j in range(0, n - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]

print("Sorted Array:", A)