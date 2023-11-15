import pandas as pd

data = pd.read_csv('harga_rumah.csv')
print (data.head())


# # membaca salah satu kolom berdasarkan nama kolom
df = pd.DataFrame(data)
# #print(df.jml_lantai)
# #print(df['jml_lantai'])
# # membaca baris pertama saja
# #print(df.iloc[0])
# # membaca semua baris pada kolom tertentu berdasarkan index
# #print(df.iloc[:,1]) # iloc[:,1] -> tanda : artinya semua baris, 1 artinya index 
# #kolom ke-1
# # membuat kolom tertentu untuk mengambil sisa kolom yang lain
# # axis = 1 artinya hanya mengambil kolom
# # bentuk dari X adalah matriks 2D
#menghapus kolom yang dipilih
X = df.drop(['harga'],axis=1)
print(X.head())

#menampilkan kolom harga saja
print(df.harga)
#print(df['harga'])


# print(df.jml_lantai.dtype)
# print(df.harga.dtype)
# melihat tipe data semua kolom/atribut
# print(df.dtypes)
# konvert tipe data pada kolom tertentu
# tipe data jml_lantai sebelumnya adalah int64
# di sini akan diconvert ke float64
# print(df.jml_lantai.astype('float64'))

# # mengubah nama kolom
# df = df.rename(columns={'jml_lantai':'lantai'})
# print(df.head())

