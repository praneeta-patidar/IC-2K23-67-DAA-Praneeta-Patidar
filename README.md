# DAA Lab Task 1

# Part 1: Trace It Yourself
# 1.Find Largest
# Input
8, 3, 15, 6, 2
# Output
Largest Number: 15
Comparisons Made: 4
# Dry Run
Start with max = 8
Compare 3 with 8: 3 < 8, so max remains 8 (Comparison = 1)
Compare 15 with 8: 15 > 8, so max becomes 15 (Comparison = 2)
Compare 6 with 15: 6 < 15, so max remains 15 (Comparison = 3)
Compare 2 with 15: 2 < 15, so max remains 15 (Comparison = 4)

# 2.Sort
# Input
A = [8, 3, 15, 6, 2]
# Output
[2, 3, 6, 8, 15]
# Steps
# Pass 1
Compare 8 and 3: Swap
3 8 15 6 2
Compare 8 and 15: No Swap
3 8 15 6 2
Compare 15 and 6: Swap
3 8 6 15 2
Compare 15 and 2: Swap
3 8 6 2 15
### Pass 2
Compare 3 and 8: No Swap
3 8 6 2 15
Compare 8 and 6: Swap
3 6 8 2 15
Compare 8 and 2: Swap
3 6 2 8 15
# Pass 3
Compare 3 and 6: No Swap
3 6 2 8 15
Compare 6 and 2: Swap
3 2 6 8 15
# Pass 4
Compare 3 and 2: Swap
2 3 6 8 15
# Final Output
2 3 6 8 15


# Part 2: Stack and Queue
# Input
Task1, Task2, Task3, Task4, Task5
# 1. Stack
# Order of Completion
Task5
Task4
Task3
Task2
Task1
# Explanation
Push Task1
Push Task2
Push Task3
Push Task4
Push Task5
Now remove tasks using pop():
Pop Task5
Pop Task4
Pop Task3
Pop Task2
Pop Task1
Therefore, order is:
Task5 Task4 Task3 Task2 Task1

# 2. Queue
# Order of Completion
Task1
Task2
Task3
Task4
Task5
# Explanation
Enqueue Task1
Enqueue Task2
Enqueue Task3
Enqueue Task4
Enqueue Task5
Now remove tasks using dequeue():
Dequeue Task1
Dequeue Task2
Dequeue Task3
Dequeue Task4
Dequeue Task5
Therefore, order is:
Task1 Task2 Task3 Task4 Task5

# 3. Printer Queue
# Printing Order
Task1
Task2
Task3
Task4
Task5
# Explanation
Task1 is received first, so it is printed first.
Task2 is printed after Task1.
Task3 is printed after Task2.
Task4 is printed after Task3.
Task5 is printed last.
Therefore, a Queue is the most suitable data structure for a printer.

# Part 4: Count the Steps
# 1
FOR i = 1 to 5
    PRINT i
The loop runs 5 times because the value of "i" goes from 1 to 5.

# 2
FOR i = 1 to n
    PRINT i
If n = 20,
The loop runs 20 times

# Part 3
FOR i = 1 to 5
    FOR j = 1 to 5
        PRINT i, j
The outer loop runs 5 times
For each outer loop iteration, the inner loop also runs 5 times

Total number of PRINT executions:
5 × 5 = 25
So, the PRINT statement runs 25 times

# Part 4
FOR i = 1 to n
    FOR j = 1 to n
        PRINT i, j
If n = 10,
The outer loop runs 10 times and the inner loop also runs 10 times for each outer loop iteration.
Total number of PRINT executions:
10 × 10 = 100
So, the PRINT statement runs 100 times
