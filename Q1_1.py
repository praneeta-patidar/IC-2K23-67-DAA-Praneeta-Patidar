# PART 1: Trace it yourself given list:8,3,15,6,2
# Find the largest number by checking one number at a time. Write down how many comparisons you made.

A = [8, 3, 15, 6, 2]
maximum = A[0]
comparisons = 0

for i in range(1, len(A)):
    comparisons += 1
    if A[i] > maximum:
        maximum = A[i]

print(A)
print("Largest Number:", maximum)
print("Comparisons:", comparisons)