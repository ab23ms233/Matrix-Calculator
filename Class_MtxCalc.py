#IMPORTING NECESSARY LIBRARIES
import numpy as np
from numpy import ndarray
from sympy import Matrix
from typing import Tuple, List

class MatrixCalculator:
    intro_text = """Enter a row of a matrix, separarted by space, in the input field
    Enter x to stop entering the rows for a matrix
    Enter u to undo the last entry\n"""

    def __init__(self, matrix: ndarray):
        """
        Initializes the MatrixCalculator class.
        This class contains methods for matrix operations such as addition, multiplication,
        finding inverse, and diagonalisation.

        Parameters:
            matrix (ndarray): The matrix to be used for calculations
        
        Raises:
            TypeError: If the provided matrix is not a numpy ndarray
        """
        if not isinstance(matrix, ndarray):
            raise TypeError("Matrix must be a numpy ndarray")
        
        self.matrix = matrix

    # Function for extracting Matrix from the User
    @staticmethod
    def matrix_extractor() -> ndarray:
        """
        Asks for a matrix from the user in the form of rows for 1 input field.

        Returns:
            ndarray: The matrix entered by the user
        """
        row_count, mtx = 0, []

        # Asking for rows of the matrix
        while True:
            row_count += 1  #Incrementing row_count
            row = input(f"Enter row {row_count}: ").lower().strip()

            if row == 'x':  # If user wants to stop entering rows
                if row_count == 1:
                    print("No rows entered. Please enter at least one row.")
                    row_count -= 1
                    continue
                break

            elif row == 'u':    # If user wants to undo the last entry
                if row_count == 1:
                    print("No rows to undo.")
                    continue

                print(f"Undoing row {row_count-1}")
                row_count -= 2
                mtx.pop()
                continue

            elements = row.split()  #Each element of the row
            elements = list(map(int, elements)) #Converting the elements to integer
            mtx.append(elements)    #Appending each row to mtx to finally extract the mtx

        arr = np.array(mtx)
        return arr

    # Dimension checker for addition of matrices
    @staticmethod
    def dim_check_add(mtx_1: ndarray, mtx_2: ndarray) -> bool:
        """
        Checks if the dimensions of 2 matrices to be added are correct

        Parameters:
            mtx_1 (ndarray): 1st matrix
            mtx_2 (ndarray): 2nd matrix

        Returns:
            bool: True if correct; False otherwise

        Raises:
            TypeError: If mtx_1 or mtx_2 is not a numpy ndarray
        """
        if not isinstance(mtx_1, ndarray) or not isinstance(mtx_2, ndarray):
            raise TypeError("Both the matrices must be numpy ndarrays")

        if mtx_1.shape == mtx_2.shape:
            return True
        return False

    # Dimension checker for multiplication of matrices
    @staticmethod
    def dim_check_mul(mtx_1: ndarray, mtx_2: ndarray) -> bool:
        """
        Checks if the dimensions of 2 matrices to be multiplied are correct

        Parameters:
            mtx_1 (ndarray): 1st matrix
            mtx_2 (ndarray): 2nd matrix

        Returns:
            bool: True if correct; False otherwise
        
        Raises:
            TypeError: If mtx_1 or mtx_2 is not a numpy ndarray
        """
        rows_mtx1, columns_mtx2 = mtx_1.shape[1], mtx_2.shape[0]

        if rows_mtx1 == columns_mtx2:
             return True
        return False

    # Check if determinant of a matrix is possible
    def is_square(self) -> bool:
        """
        Checks if it is a square matrix

        Returns:
            bool: True if square; False otherwise
        """
        if self.matrix.ndim == 2 and (self.matrix.shape[0] == self.matrix.shape[1]):
             return True
        return False

    # Compute determinant
    def determinant(self) -> float:
        """
        Compute the determinant of a matrix

        Returns:
            float: The determinant of the matrix
        
        Raises:
            ValueError: If the determinant is not square
        """
        if self.is_square():
            return np.linalg.det(self.matrix)
        else:
            raise ValueError("Matrix is not square so determinant cannot be calculated")
        
    # Check if inverse of a matrix is possible
    def is_invertible(self) -> bool:
        """
        Checks if inverse is possible
        
        Returns:
            bool: True if possible; False otherwise
        """
        if self.is_square() and np.linalg.det(self.matrix) != 0:
            return True
        return False          

    # Function for finding inverse of a matrix
    def inverse(self) -> ndarray:
        """
        Finds the inverse of a matrix

        Returns:
            ndarray: Inverse of matrix
        
        Raises:
            ValueError: If the matrix is not square or singular (determinant is 0)
        """
        if self.is_invertible():
            return np.linalg.inv(self.matrix)
        elif not self.is_square():
            raise ValueError("Matrix is not square, hence inverse cannot be calculated")
        else:
            raise ValueError("Matrix is singular (i.e., determinant is 0), hence inverse cannot be calculated")

    # Function for Addition/Multiplication of matrices
    @staticmethod
    def add_multiply(dim_checker: function, is_add: bool) -> ndarray:
        """
        Function for adding/multiplying matrices

        Parameters:
            dim_checker (function): The dimension checking function
            is_add (bool): True for addition; False for multiplication

        Returns:
            ndarray: The resultant array/matrix
        """
        num = int(input("How many matrices do you have? ")) #No. of matrices

        print(MatrixCalculator.intro_text)
        print()

        #Asking for num no. of matrices
        for i in range(num):
            print(f"Matrix {i+1}")

            arr = MatrixCalculator.matrix_extractor()
            print(arr)
            print()
            rows, columns = arr.shape

            #Initialising result_mtx once
            if i==0:
                if is_add == True:
                    result_mtx = np.zeros(shape = (rows, columns))  #Initial zero mtx for addition
                else:
                    result_mtx = np.identity(rows)   #Initial identity mtx for multiplication

            #Checking dimensions
            if dim_checker(result_mtx, arr): #type: ignore
                if is_add == True:
                    result_mtx += arr #type: ignore
                else:
                    result_mtx = result_mtx@arr #type: ignore
            else: 
                raise ValueError("Dimensions of matrices do not match for the operation")

        return result_mtx #type: ignore

    # Diagonalisation of a matrix
    def diagonalise(self) -> Tuple[ndarray, ndarray, ndarray]:
        """
        Diagonalises a given matrix

        Returns:
            Tuple[ndarray, ndarray, ndarray]: Tuple containing:
                - P: Matrix of eigenvectors
                - D: Diagonal matrix of eigenvalues
                - P_inv: Inverse of matrix P
        
        Raises:
            ValueError: If the matrix is not diagonalizable
        """
        mtx_sp = Matrix(self.matrix)

        if mtx_sp.is_diagonalizable():
            eigenvals, eigenvects = np.linalg.eig(self.matrix)

            # mtx = PDP^(-1)     mtx^n = P(D^n)P^(-1)
            D = np.diag(eigenvals)  # D = diagonal matrix of all eigenvalues
            P = eigenvects
            P_inv = np.linalg.inv(P)

            return (P, D, P_inv)

        else:
            raise ValueError("Matrix is not diagonalisable")

    # Calculating eigenvalues/eigenvectors
    def eigen(self) -> List[Tuple[float, ndarray]]:
        """
        Calculates the eigenvalues and eigenvectors of a matrix

        Returns:
            List[Tuple[float, ndarray]]: List of tuples where each tuple contains:
                - Eigenvalue (float)
                - Eigenvector (ndarray)
        
        Raises:
            ValueError: If the matrix is not square
        """
        if not self.is_square():
            raise ValueError("Eigenvalues/eigenvectors cannot be computed for non-square matrices")
        
        mtx = Matrix(self.matrix)
        eigen_data = mtx.eigenvects()   #Each element of eigen_data = (eigenvals, algebraic_multiplicity, list(Matrix(eigenvectors)))
        result = list()

        #Iterating through eigen_data to extract eigenvalues and eigenvectors
        for i in range(len(eigen_data)):
            eigenvals = eigen_data[i][0]
            eigenvects = eigen_data[i][2]
            eigenvects = np.array(eigenvects[0].tolist())   #Array of eigenvectors

            eig = (eigenvals, eigenvects)
            result.append(eig)
        
        return result
    
    # Computing Powers of a matrix
    def power(self, power: int) -> ndarray:
        """
        Computes the power of a matrix

        Parameters:
            power (int): The power to which the matrix is raised

        Returns:
            ndarray: The matrix raised to the specified power
            
        Raises:
            ValueError: If the matrix is not square
        """
        if not self.is_square():
            raise ValueError("Powers cannot be calculated for non-square matrices")
        
        result = np.linalg.matrix_power(self.matrix, power)
        return result