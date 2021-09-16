"""
Javier Navarro
Parallel Matrix Multiply
"""

from matrixUtils import *
import time
import pymp

def main():
    size = input("Enter the size of the matrices you would like to use:\n")

    m1Value = input("Enter the value you would like to use for Matrix 1:\n")
    m2Value = input("Enter the value you would like to use for Matrix 2:\n")

    m1 = genMatrix(int(size), int(m1Value))
    m2 = genMatrix(int(size), int(m2Value))

    multTime1 = time.monotonic()
    product = pMatrixMult(m1, m2)
    multTime1 = time.monotonic() - multTime1
    printSubarray(product)
    print("Time Elapsed: " + str(multTime1))

"""
Multiplies 2 given matrices and returns the product2
(Parallel Version)
"""
def pMatrixMult(m1, m2):
    length = len(m1) # 1 length since square matrices only
    product = genMatrix(length, 0) # create resulting matrix
    sharedProduct = pymp.shared.list(product)

    with pymp.Parallel() as p:
        for i in p.range (length):    # keeps track of m1 rows
            for j in p.range(length): # keeps track of m2 columns
                for k in p.range(length): # used for both matrices
                    sharedProduct[i][j] += m1[i][k] * m2[k][j]
                    #print("mult: " + str(m1[i][k] * m2[k][j]))
                    #print("matValue: " + str(sharedProduct[i][j]))
        #print(f'list for thread {p.thread_num} {sharedProduct}')
    return sharedProduct

"""
Multiplies 2 given matrices and returns the product
(Serial Version)
"""
def sMatrixMult(m1, m2):
    length = len(m1) # 1 length since square matrices only
    product = genMatrix(length, 0) # create resulting matrix

    for i in range (length):    # keeps track of m1 rows
        for j in range(length): # keeps track of m2 columns
            for k in range(length): # used for both matrices
                product[i][j] += m1[i][k] * m2[k][j]
    return product

if __name__ == '__main__':
    main()
