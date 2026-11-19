# LAB 2 – ARRAY AND MATRIX OPERATIONS

## 1. 1D Array Operations

### Aim
To implement basic operations on a one-dimensional array using a Python list, including insertion, deletion, linear search, left rotation, and right rotation.

### Logic
The program takes the array elements as input and provides a menu for performing different operations. Python list operations are used to insert and delete elements, while linear search checks elements sequentially. Rotation is performed by rearranging the elements according to the given number of positions.

### Sample Input / Output

#### Normal Case

**Sample Input:**

Enter array elements separated by spaces: 10 20 30 40 50

1D ARRAY OPERATIONS 
1. Insert value
2. Delete value
3. Linear search
4. Left rotation
5. Right rotation
6. Exit

Enter your choice: 1
Enter value to insert: 25
Enter index: 2

**Sample Output:**

Current Array: [10, 20, 30, 40, 50]
Value inserted successfully.
Current Array: [10, 20, 25, 30, 40, 50]


#### Boundary Case – Out-of-Range Index

**Input:**

Enter your choice: 2
Enter index to delete: 10

**Output:**

Invalid index.
Current Array: [10, 20, 25, 30, 40, 50]

#### Rotation Example

**Input:**

Enter your choice: 4
Enter number of positions to rotate left: 2

**Output:**

Array after left rotation:
Current Array: [25, 30, 40, 50, 10, 20]


## 2. 2D Array Operations

### Aim
To implement operations on a two-dimensional array using a Python list of lists, including row insertion, row deletion, searching, and 90-degree clockwise rotation.

### Logic
The program stores the matrix as a list of lists and uses row and column positions to access its elements. Rows can be inserted or deleted at a specified position, while searching checks every element of the matrix. For rotation, the rows and columns are rearranged to produce a 90-degree clockwise rotation.

### Sample Input / Output

#### Normal Case

**Sample Input:**

Enter number of rows: 2
Enter number of columns: 3

Enter elements of row 0: 1 2 3
Enter elements of row 1: 4 5 6

**Output:**

Current Matrix:
[1, 2, 3]
[4, 5, 6]

#### Search Example

**Input:**

Enter your choice: 3
Enter value to search: 5

**Output:**

Value found at row 1, column 1

#### Boundary Case – Invalid Row Position

**Input:**

Enter your choice: 2
Enter row position to delete: 10

**Output:**

Invalid position.

Current Matrix:
[1, 2, 3]
[4, 5, 6]

#### 90-Degree Clockwise Rotation

**Input:**

Enter your choice: 4

**Output:**

Matrix after 90-degree clockwise rotation:

[4, 1]
[5, 2]
[6, 3]


## 3. Sparse Matrix Representation and Operations

### Aim
To convert a full two-dimensional matrix into sparse triple representation, reconstruct the original matrix from its sparse representation, and add two sparse matrices without converting them back to full matrices.

### Logic
The program stores only non-zero elements of a matrix along with their row and column positions in triple form (row, column, value). For addition, the two sparse representations are traversed together and elements having the same position are added directly. The resulting sparse matrix is then reconstructed into its full matrix form for comparison.

### Sample Input / Output

#### Sample Input

Enter rows for Matrix 1: 3
Enter columns for Matrix 1: 3

Enter Matrix 1:
0 5 0
0 0 8
6 0 9

Enter Matrix 2:
0 2 0
3 0 0
4 0 1

### Sample Output

 MATRIX 1 

Full Matrix:
[0, 5, 0]
[0, 0, 8]
[6, 0, 9]

Sparse Triple Representation:
(Row, Column, Value)
(3, 3, 4)
(0, 1, 5)
(1, 2, 8)
(2, 0, 6)
(2, 2, 9)


 MATRIX 2 

Full Matrix:
[0, 2, 0]
[3, 0, 0]
[4, 0, 1]

Sparse Triple Representation:
(Row, Column, Value)
(3, 3, 4)
(0, 1, 2)
(1, 0, 3)
(2, 0, 4)
(2, 2, 1)


 ADDITION RESULT

Sparse Triple Representation:
(Row, Column, Value)
(3, 3, 5)
(0, 1, 7)
(1, 0, 3)
(1, 2, 8)
(2, 0, 10)
(2, 2, 10)

Reconstructed Full Matrix:
[0, 7, 0]
[3, 0, 8]
[10, 0, 10]

#### Boundary Case – Completely Zero Matrix

**Input:**

Matrix 1:
0 0
0 0

Matrix 2:
0 0
0 0

**Output:**

Sparse Triple Representation:
(2, 2, 0)

Reconstructed Full Matrix:
[0, 0]
[0, 0]

This demonstrates that a matrix containing only zero values has no non-zero entries in its sparse representation.


## 4. Matrix Calculator – Menu Driven Program

### Aim
To develop a menu-driven matrix calculator that performs matrix addition, matrix multiplication, transpose, and determinant calculation with proper dimension validation.

### Logic
The program displays a menu and accepts the user's choice before taking the required matrix input. Addition is performed only when both matrices have the same dimensions, while multiplication requires the number of columns of the first matrix to equal the number of rows of the second matrix. Determinant calculation is performed only for square 2×2 and 3×3 matrices.

### Sample Input / Output

#### 1. Matrix Addition

**Sample Input:**

Enter your choice: 1

Enter Matrix 1:
Enter number of rows: 2
Enter number of columns: 2
Enter row 1: 1 2
Enter row 2: 3 4

Enter Matrix 2:
Enter number of rows: 2
Enter number of columns: 2
Enter row 1: 5 6
Enter row 2: 7 8

**Sample Output:**

Result:
[6, 8]
[10, 12]

### 2. Matrix Multiplication

**Sample Input:**

Enter your choice: 2

Matrix 1:
1 2
3 4

Matrix 2:
5 6
7 8

**Sample Output:**

Result:
[19, 22]
[43, 50]

### 3. Transpose

**Sample Input:**

Enter your choice: 3

Enter Matrix:
1 2 3
4 5 6

**Sample Output:**

Transpose:
[1, 4]
[2, 5]
[3, 6]

### 4. Determinant

**Sample Input:**

Enter your choice: 4

Enter Matrix:
1 2
3 4

**Sample Output:**

Determinant = -2

### Boundary Case – Incompatible Matrix Dimensions

For matrix addition, if the first matrix is 2 × 2 and the second matrix is 2 × 3:

**Output:**
Addition not possible. Dimensions must be the same.

For multiplication, if the first matrix is `2 × 3` and the second matrix is 2 × 2:

**Output:**
Multiplication not possible. Columns of first matrix must equal rows of second.

### Boundary Case – Non-Square Matrix for Determinant

**Input:**
Matrix:
1 2 3
4 5 6

**Output:**
Determinant can only be calculated for a square matrix.

# Conclusion
This lab demonstrates fundamental operations on one-dimensional arrays, two-dimensional arrays, sparse matrices, and matrices using Python. The programs also demonstrate input validation and handling of boundary cases such as invalid indices, empty matrices, and incompatible matrix dimensions.
