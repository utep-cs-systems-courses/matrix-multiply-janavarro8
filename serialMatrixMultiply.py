from matrixUtils import *
import time

def main():
    size = input("Enter the size of the matrices you would like to use:\n")

    m1Value = input("Enter the value you would like to use for Matrix 1:\n")
    m2Value = input("Enter the value you would like to use for Matrix 2:\n")

    m1 = genMatrix(int(size), int(m1Value))
    m2 = genMatrix(int(size), int(m2Value))

    multTime1 = time.monotonic()
    product = matrixMult(m1, m2)
    multTime1 = time.monotonic() - multTime1
    printSubarray(product)
    print(multTime1)

    multTime2 = time.monotonic()
    product2 = blockedMatMult(m1, m2)
    multTime2 = time.monotonic() - multTime2
    printSubarray(product2)
    print(multTime2)
    

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

"""
Multiples 2 given matrices using a step
"""
def blockedMatMult(m1, m2):
    length = len(m1)
    tile_size = 16
    output = genMatrix(length, 0)
    sum = 0

    for kk in range(0, length, tile_size):
        for jj in range(0, length, tile_size):
            for i in range(length): 
                j_end_val = jj + tile_size 
                for j in range(jj, j_end_val): 
                    k_end_val = kk + tile_size 
                    sum = output[i][j] 
                    for k in range(kk, k_end_val): 
                        sum = sum + m1[i][k] * m2[k][j] 
                    output[i][j] = sum 

if __name__ == '__main__':
    main()
