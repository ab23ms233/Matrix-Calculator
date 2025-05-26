#IMPORTING NECESSARY LIBRARIES
import numpy as np
from numpy import ndarray
from sympy import Matrix


intro_text = "Enter a row of a matrix, separarted by space, in the input field\nEnter x to stop entering the rows for a matrix\nEnter u to undo the last entry\n"

# Function for extracting Matrix from the User
def matrix_extractor() -> ndarray:
    """
    Asks for a matrix from the user in the form of rows for 1 input field.

    Returns:
    tuple: (The array entered by the user, (dimensions of the array))
    """
    row_count, mtx = 0, []

    #Asking for rows of the matrix
    while True:
        row_count += 1  #Incrementing row_count
        row = input(f"Enter row {row_count}: ").lower().strip()

        #Checking if user wants to terminate entering rows
        if row == 'x':
            break
        elif row == 'u':
            row_count -= 2
            mtx.pop()
            continue

        elements = row.split()  #Each element of the row
        elements = list(map(int, elements)) #Converting the elements to integer
        mtx.append(elements)    #Appending each row to mtx to finally extract the mtx
          
    arr = np.array(mtx)
    return arr

# SOME NECESSARY FUNCTIONS

#Dimension checker for addition of matrices
def dim_check_add(A: ndarray, B: ndarray) -> bool:
    """
    Checks if the dimensions of 2 matrices to be added are correct

    Parameters:
    A(ndarray): 1st array
    B(ndarray): 2nd array

    Returns:
    bool: True if correct; False otherwise
    """
    if A.shape == B.shape:
        return True
    return False

#Dimension checker for multiplication of matrices
def dim_check_mul(A: ndarray, B: ndarray) -> bool:
    """
    Checks if the dimensions of 2 matrices to be multiplied are correct

    Parameters:
    A(ndarray): 1st array
    B(ndarray): 2nd array

    Returns:
    bool: True if correct; False otherwise
    """
    rows_B, columns_A = A.shape[1], B.shape[0]
    if rows_B == columns_A:
         return True
    
    return False

#Check if determinant of a matrix is possible
def is_square(A: ndarray):
    """
    Checks if it is a square matrix
    Parameters:
    A(ndarray): array to be checked
    Returns:
    bool: True if square; False otherwise
    """
    if A.shape[0] == A.shape[1]:
         return True
    return False

#Check if inverse of a matrix is possible
def is_invertible(A: ndarray):
    """
    Checks if inverse is possible
    Parameters:
    A(ndarray): array to be checked
    Returns:
    bool: True if possible; False otherwise
    """
    if is_square(A) and np.linalg.det(A) != 0:
         return True
    return False          

# Function for finding inverse of a matrix
def inverse(matrix: ndarray):
    """
    Finds the inverse of a matrix, if invertible

    Parameters:
    matrix(ndarray): The matrix whose inverse is required

    Returns:
    ndarray: Inverse of matrix, if invertible
    """
    if is_invertible(matrix):
        return f"Result:\n{np.linalg.inv(matrix)}"
    elif not is_square(matrix):
        return "The matrix is not square so determinant cannot be calculated"
    else:
        return "Matrix is not invertible as determinant is 0"

# Function for Addition/Multiplication of matrices
def add_multiply(dim_checker, is_add: bool):
    """
    Function for adding/multiplying matrices

    Parameters:
    dim_checker(function): The dimension checking function
    is_add(bool): True for addition; False for multiplication

    Returns:
    ndarray: The resultant array/matrix
    """
    num = int(input("How many matrices do you have? ")) #No. of matrices

    print(intro_text)
    print()

    #Asking for num no. of matrices
    for i in range(num):
        print(f"Matrix {i+1}")

        arr = matrix_extractor()
        print(arr)
        print()
        rows, columns = arr.shape
        
        #Initialising result_mtx once
        if i==0:
            if is_add == True:
                result_mtx = np.zeros(shape = (rows, columns))  #Initial zero mtx for addition
            else:
                result_mtx = np.identity(rows)   #Initial identity mtc for multiplication

        #Checking dimensions
        if dim_checker(result_mtx, arr): #type: ignore
            if is_add == True:
                result_mtx += arr #type: ignore
            else:
                result_mtx = result_mtx@arr #type: ignore
        else: 
            return "The matrices are not of correct dimensions"
    
    return result_mtx #type: ignore

# Diagonalisation of a matrix
def diagonalise(mtx: ndarray):
    """
    Diagonalises a given matrix, if diagonalisable

    Parameters:
    mtx(ndarray): The matrix to be diagonalised

    Returns:
    tuple: Tuple consisting of P, D, P_inv such that mtx = PDP^(-1), if diagonalisable
    Else returns error
    """
    mtx_sp = Matrix(mtx)

    if mtx_sp.is_diagonalizable():
        eigenvals, eigenvects = np.linalg.eig(mtx)

        # mtx = PDP^(-1)     mtx^n = P(D^n)P^(-1)
        D = np.diag(eigenvals)  #D = diagonal matrix of all eigenvalues
        P = eigenvects
        P_inv = np.linalg.inv(P)

        return (P, D, P_inv)
    
    else:
        return "Matrix is not diagonalisable"
