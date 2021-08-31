from matrixUtils import *

def main():
    size = input("Enter the size of the matrices you would like to use:\n")

    m1Value = input("Enter the value you would like to use for Matrix 1:\n")
    m2Value = input("Enter the value you would like to use for Matrix 2:\n")

    m1 = genMatrix(int(size), int(m1Value))
    m2 = genMatrix(int(size), int(m2Value))

    product = matrixMult(m1, m2)
    printSubarray(product)

"""
Multiplies 2 given matrices and returns the product
"""
def matrixMult(m1, m2):
    length = len(m1) # 1 length since square matrices only
    product = [[0] * length for i in range(length)] # create resulting matrix 

    for i in range (length):    # keeps track of m1 rows
        for j in range(length): # keeps track of m2 columns    
            for k in range(length): # used for both matrices
                product[i][j] += m1[i][k] * m2[k][j]
    return product

if __name__ == '__main__':
    main()