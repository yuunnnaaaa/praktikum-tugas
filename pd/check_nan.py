import pandas as pd
import numpy as np

# mencari data yang NaN
# NaN kepanjangan dari Not a Number
tmp = pd.DataFrame({
'nama': ['Budi', 'Siti','Agus'],
'jenis': ['Laki-laki', 'Perempuan','Laki-laki'],
'usia': [22, 21,np.nan]
})
# cek yang mengandung NaN pada kolom usia
print(tmp[pd.isnull(tmp.usia)])