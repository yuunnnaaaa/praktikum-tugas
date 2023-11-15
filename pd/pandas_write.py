import pandas as pd

df = pd.DataFrame({
 'nama': ['Budi', 'Siti'],
 'jenis': ['Laki-laki', 'Perempuan'],
 'usia': [22, 21]
})
df.to_csv('fileku.csv',index=False)