import numpy as np

A = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

B = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

#penjumlahan vektor/matriks
C = np.add(A,B)
print(C)

#perkalian vektor/matriks
D = np.dot(A,B)
print(D)