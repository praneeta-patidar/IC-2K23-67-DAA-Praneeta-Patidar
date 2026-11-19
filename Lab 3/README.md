# LAB 3 – SORTING AND SEARCHING

## Objective
To implement and understand different sorting algorithms and binary search using Python.

## Implementation Approach
All sorting algorithms are implemented as separate functions.

### Consistency
All sorting functions return a new sorted list and do not modify the original input list.

# 1. Bubble Sort, Selection Sort and Insertion Sort

## Aim
To implement Bubble Sort, Selection Sort, and Insertion Sort as separate functions and display the array after every pass.

## Algorithms Implemented
Bubble Sort
Selection Sort
Insertion Sort

## QUESTION 1 

## Sample Input

[64, 25, 12, 22, 11]

## Sample Output

Original Array: [64, 25, 12, 22, 11]

Bubble Sort:
After pass 1: [25, 12, 22, 11, 64]
After pass 2: [12, 22, 11, 25, 64]

Bubble Sort Result: [11, 12, 22, 25, 64]

Selection Sort Result: [11, 12, 22, 25, 64]

Insertion Sort Result: [11, 12, 22, 25, 64]

# 2. Merge Sort, Quick Sort and Heap Sort

## Aim
To implement Merge Sort, Quick Sort, and Heap Sort as separate functions and display the sorting process.

## Algorithms Implemented
Merge Sort
Quick Sort
Heap Sort

## QUESTION 2

## Quick Sort Pivot Strategy

The last element is selected as the pivot.
This strategy is clearly mentioned in the Quick Sort function.

## Sample Input

[38, 27, 43, 3, 9, 82, 10]

## Sample Output

Original Array: [38, 27, 43, 3, 9, 82, 10]

Merge Sort Result:
[3, 9, 10, 27, 38, 43, 82]

Quick Sort Result:
[3, 9, 10, 27, 38, 43, 82]

Heap Sort Result:
[3, 9, 10, 27, 38, 43, 82]

The program also prints intermediate merge steps, pivot operations, heap construction, and extraction steps so that the sorting process is visible.

# 3. Radix Sort

## Aim
To implement Radix Sort for non-negative integers using the Least Significant Digit (LSD) approach.

## Logic
Radix Sort processes the numbers digit by digit, starting from the least significant digit. A counting sort helper function is used to arrange the numbers according to each digit position. The process continues until all digit positions have been processed.

## QUESTION 3

## Sample Input

[170, 45, 75, 90, 802, 24, 2, 66]

## Sample Output

Original Array: [170, 45, 75, 90, 802, 24, 2, 66]

After sorting by digit place 1:
[170, 90, 802, 2, 24, 45, 75, 66]

After sorting by digit place 10:
[802, 2, 24, 45, 66, 170, 75, 90]

After sorting by digit place 100:
[2, 24, 45, 66, 75, 90, 170, 802]

Radix Sort Result:
[2, 24, 45, 66, 75, 90, 170, 802]

This implementation supports non-negative integers only, as required.

# 4. Binary Search

## Aim
To implement iterative Binary Search that returns the index of the target element or `-1` if the target is not found.

## Logic
Binary Search repeatedly checks the middle element of a sorted array. If the target is greater than the middle element, the search continues in the right half; otherwise, it continues in the left half. The process continues until the element is found or the search range becomes empty.

## QUESTION 4

## Sample Input

Sorted Array:
[10, 20, 30, 40, 50, 60, 70]

Target 1:
40

Target 2:
45

## Sample Output

Searching for: 40
Index: 3

Searching for: 45
Index: -1

The first test demonstrates a successful search, while the second demonstrates the not-found case.

# Conclusion
This lab implements fundamental sorting and searching algorithms using Python.
The sorting algorithms implemented are:

1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Merge Sort
5. Quick Sort
6. Heap Sort
7. Radix Sort

Binary Search is also implemented iteratively.

Each sorting algorithm is implemented as a standalone function and consistently returns a new sorted list without modifying the original input.
