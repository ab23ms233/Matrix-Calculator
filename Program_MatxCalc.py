#IMPORTING NECESSARY LIBRARIES
import numpy as np
from sympy import Matrix
from Class_MtxCalc import MatrixCalculator as mc
import scipy.linalg as sclinalg


def main():   
    intro_text = """Enter an element of a matrix, separarted by space, in the input field, so that a row is entered at once
    Enter x to stop entering the rows for a matrix
    Enter u to undo the last entry\n"""
    invalid_text = "Invalid choice. Enter again"

    print()
    print("Welcome to the Matrix Calculator")

    while True: # flag = all_operations

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

        # LOGIC FOR CHOICES
        while True:     #flag = same_operation
            if choice == 1: # Addition
                print("You chose Addition")
                print()
                result = mc.add_multiply(dim_checker=mc.dim_check_add, is_add=True)

            elif choice == 2:   # Multiplication
                print("You chose Multiplication")
                print()
                result = mc.add_multiply(dim_checker=mc.dim_check_mul, is_add=False)

            elif choice in (i for i in range(3,9)):

                #Introduction text, extracting and displaying matrix to the user. Removes redundancy of code
                print(intro_text)
                print()
                mtx = mc.matrix_extractor()
                print(f"Matrix: \n{mtx}")
                print()

                mtx_instance = mc(mtx)  # Creating an instance of MatrixCalculator class

                if choice == 3:     # Inverse
                    print("You chose to compute Inverse")
                    print()
                    result = mtx_instance.inverse()

                elif choice == 4:   # Determinant
                    print("You chose to evaluate Determinant")
                    print()
                    result = mtx_instance.determinant()

                elif choice == 5:   # Diagonalisation
                    print("You chose to Diagonalise")
                    print()
                    result = mtx_instance.diagonalise()

                elif choice == 6:   # Eigenvalues/eigenvectors
                    print("You chose to find Eigenvalues/Eigenvectors")
                    print()
                    eigen_data = mtx_instance.eigen()
                    result = ""

                    # Extracting the eigenvalues/eigenvectors and displaying in simplified format
                    for i in range(len(eigen_data)):
                        eigenvals = eigen_data[i][0]
                        eigenvects = eigen_data[i][1]
        
                        val = f"Eigenvalue {i+1}: {eigenvals}\n"
                        vect = f"Eigenvector {i+1}: {eigenvects}\n"
                        result = val + vect + '\n'

                elif choice == 7:   # Powers of mtx
                    print("You choose to compute Powers of Matrix")
                    print()
                    pow = int(input("Enter the power to which you want to raise the matrix: "))
                    result = mtx_instance.power(pow)

                else:   # Functions on matrices
                    while True:     #flag = all_func
                        print("Choose from one of the following operations: ")
                        print("(1) sin")
                        print("(2) cos")
                        print("(3) exponential")
                        print("(4) logarithm")
                        print("(5) sinh")
                        print("(6) cosh")
                        print()
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
                                print(invalid_text)
                                break   #Returns to all_func

                            print("What do you want to do next?")
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