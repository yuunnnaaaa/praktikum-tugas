import numpy as np

# membuat vektor
A = np.array([1,2,3]) # vektor baris 1x3
print("Vektor A",A)
# membuat matriks 2 dimensi dengan ukuran 3x3
B = np.array([
 [1,2,1],
 [2,1,3],
 [3,2,2]
])
print("Matriks B",B)
# penjumlahan vektor/matriks
C = np.add(A,B)
print(C)
# inisiasi array
A = np.zeros((3,4)) # membuat matriks dengan ukuran 3x4 di mana setiap elemen 
# bernilai nol
print(A)
A = np.ones((3,4)) # membuat matriks dengan ukuran 3x4 di mana setiap elemen 
# bernilai 1
print(A)
# Matriks Tranpose
BT = np.transpose(B)
print(BT)
# atau
BT = B.T
print(BT)