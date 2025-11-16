import numpy as np
import itertools

def random_matrix(dim):
    """
    Generates a dim x dim array of integers
    between 0 and 9.
    """
    matrix = np.random.randint(10, size=(dim, dim))
    return matrix

def get_permutations(dim):
    """
    Creates a list of all possible permutations
    of indices for a given dimension.
    """
    indices = range(dim)
    permutations = list(itertools.permutations(indices))
    return permutations

def calculate_product(matrix, perm):
    """
    Calculates the product of matrix elements
    along a given permutation.
    """
    product = 1
    dim = matrix.shape[0]
    for i in range(dim):
        product *= matrix[i, perm[i]]
    return product

def get_permutation_sign(perm):
    """
    Determines the sign (parity) of the permutation.
    Returns +1 for even, -1 for odd.
    """
    inversions = 0
    length = len(perm)
    for i in range(length):
        for j in range(i + 1, length):
            if perm[i] > perm[j]:
                inversions += 1
    
 
    return (-1) ** inversions

def calculate_determinant(matrix):
    """
    Calculates the determinant using the
    Leibniz formula (permutation method).
    """
    dim = matrix.shape[0]
    det_sum = 0
    
    all_permutations = get_permutations(dim)
    
    for perm in all_permutations:
        sign = get_permutation_sign(perm)
        product = calculate_product(matrix, perm)
        det_sum += sign * product
        
    return det_sum

def main():
    """
    Main function to run the program.
    """
    while True:
        dim_str = input("Enter the dimension of the square matrix: ")
        try:
     
            dim = int(dim_str)
            if dim < 1:
                print("Dimension must be a positive integer (>= 1).")
            else:
            
                break
        except ValueError:
       
            print("Error: Please enter a valid integer.")


    matrix = random_matrix(dim) 
    determinant = calculate_determinant(matrix)
    determinant_numpy = np.linalg.det(matrix)

    print("\n--- Result ---")
    print("Generated matrix:")
    print(matrix)
    print(f"\nDeterminant (permutation method): {determinant}")
    print(f"Check (np.linalg.det): {determinant_numpy}")


    if np.isclose(determinant, determinant_numpy):
        print("Results match!")
    else:
        print("Results do not match.")

if __name__ == "__main__":
    main()