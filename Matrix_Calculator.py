#IMPORTING NECESSARY LIBRARIES
import numpy as np
from sympy import Matrix
from necessary_functions import matrix_extractor, dim_check_add, dim_check_mul, add_multiply, inverse, is_square, diagonalise
import scipy.linalg as sclinalg


def main():   
    print("Welcome to the Matrix Calculator")
    intro_text = "Enter an element of a matrix, separarted by space, in the input field, so that a row is entered at once\nEnter x to stop entering the rows for a matrix\nEnter u to undo the last entry\n"

    while True: #flag = all_operations

        # Calculations that can be performed
        print("Choose any of the following options")
        print()
        print("(1) To add matrices")
        print("(2) To multiply matrices")
        print("(3) To find the inverse of a matrix")
        print("(4) To find the determinant of a matrix")
        print("(5) To diagonalise a matrix")
        print("(6) To find the eigenvalues & eigenvectors of a matrix")
        print("(7) To find powers of a matrix")
        print("(8) To find the functions operated on a matrix")
        print()
        choice = int(input())

        #LOGIC FOR CHOICES
        while True:     #flag = same_operation
            if choice == 1: #Addition
                print("ADDITION")
                print()
                result = add_multiply(dim_checker=dim_check_add, is_add=True)

            elif choice == 2:   #Multiplication
                print("MULTIPLICATION")
                print()
                result = add_multiply(dim_checker=dim_check_mul, is_add=False)

            elif choice in (i for i in range(3,9)):

                #Introduction text, extracting and displaying matrix to the user. Removes redundancy of code
                print(intro_text)
                print()
                mtx = matrix_extractor()
                print(mtx)
                print()

                if choice == 3: #Inverse
                    print("INVERSE")
                    print()
                    result = inverse(mtx)

                elif choice == 4:   #Determinant
                    print("DETERMINANT")
                    print()

                    if is_square(mtx):
                        result = np.linalg.det(mtx)
                    else:
                        print("The matrix is not square so determinant cannot be calculated")

                elif choice == 5:   #Diagonalisation
                    print("DIAGONALISATION")
                    print()
                    result = diagonalise(mtx) # type: ignore

                elif choice == 6: #Eigenvalues/eigenvectors
                    print("EIGENVALUES/EIGENVECTORS")
                    print()

                    if is_square(mtx):
                        mtx = Matrix(mtx)
                        eigen_data = mtx.eigenvects()   #Each element of eigen_data = (eigenvals, algebraic_multiplicity, list(Matrix(eigenvectors)))
                        result = ''

                        for i in range(len(eigen_data)):
                            eigenvals = eigen_data[i][0]
                            eigenvects = eigen_data[i][2]
                            eigenvects = np.array(eigenvects[0].tolist())   #Array of eigenvectors

                            val = f"Eigenvalue {i+1}: {eigenvals}\n"
                            vect = f"Eigenvector {i+1}: {eigenvals}\n"
                            result = val + vect + '\n'

                    else:
                        result = "Eigenvalues/eigenvectors cannot be computed for non-square matrices"

                elif choice == 7:   #Powers of mtx
                    print("POWERS OF A MATRIX")
                    print()

                    if is_square(mtx): #type: ignore to ignore unbound warning on mtx
                        pow = int(input("Enter the power of the matrix: "))
                        result = np.linalg.matrix_power(mtx, pow) #type: ignore

                        #FINDING POWERS BY DIAGONALISATION
                        # eigenvals, eigenvects = np.linalg.eig(mtx)

                        # mtx = PDP^(-1)     mtx^n = P(D^n)P^(-1)
                        # D = np.diag(eigenvals)
                        # P = eigenvects
                        # P_inv = np.linalg.inv(P)
                        # D_pow = np.linalg.matrix_power(D, pow)

                        # result = P@D_pow@P_inv

                    else:
                        print("Powers of non-sqaure matrices cannot be calculated")

                else:   #Functions on matrices

                    while True:     #flag = all_func
                        print("Choose from one of the following operations: ")
                        print("(1) sin")
                        print("(2) cos")
                        print("(3) exponential")
                        print("(4) logarithm")
                        print("(5) sinh")
                        print("(6) cosh")

                        option = int(input())
                        print()

                        while True:     #flag = same_func
                            if option == 1:
                                result = sclinalg.sinm(mtx) #type: ignore to ignore unbound warning on mtx
                            elif option == 2:
                                result = sclinalg.cosm(mtx) #type: ignore
                            elif option == 3:
                                result = sclinalg.expm(mtx) #type: ignore
                            elif option == 4:
                                result = sclinalg.logm(mtx) #type: ignore
                            elif option == 5:
                                result = sclinalg.sinhm(mtx) #type: ignore
                            elif option == 6:
                                result = sclinalg.coshm(mtx) #type: ignore
                            else:
                                print("WRONG INPUT! Returning to menu")
                                break   #Returns to all_func

                            print("Enter:")
                            print("'s' for performing the same function on matrix")
                            print("'a' for choosing from all the available functions on matrix")
                            print("'e' to exit from this category of operations")
                            print()

                            option = input().lower().strip()

                            while True:     
                                if option == 's':
                                    same_func = True
                                    exit_func = False
                                    break
                                elif option == 'a':
                                    same_func = False
                                    exit_func = False
                                    break
                                elif option == 'e':
                                    same_func = False
                                    exit_func = True
                                else:
                                    print("INVALID input. Enter again")     #Loop runs again

                            #same_func = True, Returns to same_func
                            #same_func = Fasle, Returns to exit_func
                            if not same_func:
                                break
                        
                        #exit_func = True, Breaks from matrix functions category
                        #exit_func = False, Returns to all_func
                        if exit_func:   #type:ignore  flag = exit_func
                            break

            else:   #INVALID input
                print("INVALID input. Returning to main menu")
                break   #Returns to all_operations
                
            #Printing the result of all operations at the end to reduce redundancy of code
            print(f"Result:\n{result}") #type: ignore to ignore unbound warning on result
            print()

            #Asking what user wants to do next
            print("Enter:")
            print("'s' to perform the same operation")
            print("'a' to choose from all available operations")
            print("'e' to exit ")
            print()

            while True: #flag = exit
                next_action = input().lower().strip()

                if next_action == 's':
                    same_operation = True
                    break  #Returns to something
                elif next_action == 'a':
                    same_operation = False
                    break   #Returns to something
                elif next_action == 'e':
                    print("Thanks for using the calculator. Have a nice day")
                    return  #Exits from main function
                else:
                    print("INVALID input. Enter again") #Returns to exit 
            
            #same_operation = True, returns to same_operation
            #same_operation = Fasle, returns to all_operations
            if not same_operation:  #flag = something
                print()
                break   

if __name__ == "__main__":
    main()