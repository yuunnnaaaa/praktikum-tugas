import numpy as np

# mengakses elemen dari vektor/matriks
A = np.array([1,2,3])
a = A[2] # angka 2 adalah indeks. Indeks dimulai dari 0
print("Elemen ke-2 dari vektor A adalah",a)
B = np.array([
 [1,2,1],
 [2,1,3],
 [3,2,2]
])
# karena B adalah matriks 2 dimensi, maka untuk mengakses suatu elemen 
# membutuhakan 2 parameter yaitu baris dan kolom
# x = B[0,2] # baris ke-0 berisi [1,2,1], kolom ke-2 dari baris ke-0 adalah 1
# print(x)
# # Slicing array 
# x = A[0:2]
# print(x)
# # memilih semua elemen sebanyak pada baris ke 0
# x = B[:1]
# print(x)


# mengubah matriks 2 dimensi ke vektor
vB = B.ravel()
print(vB)
D = np.array([
 [1,2,1],
 [2,1,3],
 [3,2,2],
 [4,5,6]
])
# mengubah bentuk array
vC = D.reshape(6, 2) # mengubah bentuk array dari 3x4 menjadi 6x2
print(vC)
# mengubah bentuk array ke vektor 1D
vC = D.reshape(1, -1) # sama dengan ravel()
print(vC)