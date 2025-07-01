#IMPORTING NECESSARY LIBRARIES
from Class_MtxCalc import MatrixCalculator as mc
import scipy.linalg as sclinalg


def main():   
    intro_text = """Enter an element of a matrix, separarted by space, in the input field, so that a row is entered at once
Enter x to stop entering the rows for a matrix
Enter u to undo the last entry"""
    invalid_text = "Invalid choice. Enter again"
    new_mtx = True       # A new matrix will be entered by user
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
        print()

        # LOGIC FOR CHOICES
        while True:     # flag = same_operation
            if choice == 1: # Addition
                print("You chose Addition")
                print()
                result = mc.add_multiply(dim_checker=mc.dim_check_add, is_add=True)

            elif choice == 2:   # Multiplication
                print("You chose Multiplication")
                print()
                result = mc.add_multiply(dim_checker=mc.dim_check_mul, is_add=False)

            elif choice in (i for i in range(3,9)):

                if new_mtx:
                    #Introduction text, extracting and displaying matrix to the user. Removes redundancy of code
                    print(intro_text)
                    print()
                    mtx = mc.matrix_extractor()

                print(f"Matrix: \n{mtx}")
                print()
                mtx_instance = mc(mtx)  # Creating an instance of MatrixCalculator class

                if choice == 3:     # Inverse
                    print("Computing Inverse...")
                    print()
                    result = mtx_instance.inverse()

                elif choice == 4:   # Determinant
                    print("Calculating Determinant...")
                    print()
                    result = mtx_instance.determinant()

                elif choice == 5:   # Diagonalisation
                    print("Diagonalising Matrix...")
                    print()
                    result = mtx_instance.diagonalise()

                elif choice == 6:   # Eigenvalues/eigenvectors
                    print("Computing Eigenvalues/Eigenvectors...")
                    print()
                    eigen_data = mtx_instance.eigen()
                    result = ""

                    # Extracting the eigenvalues/eigenvectors and displaying in simplified format
                    for i in range(len(eigen_data)):
                        eigenvals = eigen_data[i][0]
                        eigenvects = eigen_data[i][1]
        
                        val = f"Eigenvalue {i+1}: {eigenvals}\n"
                        vect = f"Eigenvector {i+1}: {eigenvects}\n"
                        result += val + vect + '\n'

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

                        while True:     # flag = same_func
                            if option == 1:
                                print("Calculating sin...")
                                result = sclinalg.sinm(mtx)
                            elif option == 2:
                                print("Generating cos matrix...")
                                result = sclinalg.cosm(mtx)
                            elif option == 3:
                                print("Computing exponential...")
                                result = sclinalg.expm(mtx)
                            elif option == 4:
                                print("Calculating logarithm...")
                                result = sclinalg.logm(mtx)
                            elif option == 5:
                                print("Computing sinh...")
                                result = sclinalg.sinhm(mtx)
                            elif option == 6:
                                print("Applying cosh to matrix...")
                                result = sclinalg.coshm(mtx)
                            else:
                                print(invalid_text)     
                                break       # Returns to invalid option
                            
                            print(f"Result:\n{result}")
                            print()

                            # Next action of user
                            print("What do you want to do next?")
                            print("1. Perform the same function")
                            print("2. Perform a different function")
                            print("3. Exit this category of operations")
                            print()

                            while True:     # flag = invalid next_choice
                                next_choice = int(input())
                                print()

                                if next_choice == 1:
                                    same_func = True
                                    all_func = False
                                    break
                                elif next_choice == 2:
                                    same_func = False
                                    all_func = True
                                    break
                                elif next_choice == 3:
                                    same_func = False
                                    all_func = False
                                    break
                                else:
                                    print(invalid_text)     # Returns to invalid next_choice

                            # Matrix choice of user
                            print("Which matrix do you want to operate on?")
                            print("1. Modified matrix")
                            print("2. Original matrix")
                            print("3. New matrix")
                            print()

                            while True:     # flag = invalid matrix_choice
                                matrix_choice = int(input())
                                print()

                                if matrix_choice == 1:
                                    mtx = result
                                    break
                                elif matrix_choice == 2:
                                    break
                                elif matrix_choice == 3:
                                    mtx = mc.matrix_extractor()
                                    break
                                else:
                                    print(invalid_text)     # Returns to invalid matrix_choice
                            
                            # same_func = True, Returns to same_func
                            # same_func = Fasle, Returns to check
                            if not same_func:
                                break
                        
                        # all_func = False, Breaks from matrix functions category
                        # all_func = True, Returns to all_func
                        if not all_func:    # flag = check
                            break

            else:   # INVALID input
                print(invalid_text)
                break   #Returns to all_operations
                
            #Printing the result of all operations at the end to reduce redundancy of code
            if choice != 8:     # Result of functions is printed earlier
                print(f"Result:\n{result}")
                print()

            #Asking what user wants to do next
            print("What's next on your mind?")
            print("1. Perform the same operation")
            print("2. Choose from all available operations")
            print("3. Exit ")
            print()

            while True:     # flag = exit
                next_action = int(input())
                print()

                if next_action == 1:
                    same_op = True
                    break  #Returns to something
                elif next_action == 2:
                    same_op = False
                    break   #Returns to something
                elif next_action == 3:
                    print("Thanks for using the calculator. Have a nice day")
                    return  # Exits from main function
                else:
                    print(invalid_text)     # Returns to exit 

            print("Which matrix do you want to operate on?")

            if choice in [1,2,3,7,8]:      # Modified matrix is generated only in thse cases
                print("1. Original Matrix")
                print("2. New Matrix")
                print("3. Modified Matrix")
            else:
                print("1. Original Matrix")
                print("2. New Matrix")
            
            print()

            while True:
                matrix_choice = int(input())
                print()

                if matrix_choice == 1:
                    new_mtx = False     # A new matrix will be entered by user
                    break
                elif matrix_choice == 2:
                    new_mtx = True
                    break
                elif matrix_choice == 3 and choice in [1,2,3,7,8]:
                    new_mtx = False
                    mtx = result
                    break
                else:
                    print(invalid_text)

            #same_operation = True, returns to same_operation
            #same_operation = False, returns to all_operations
            if not same_op:  # flag = something
                print()
                break   

if __name__ == "__main__":
    main()