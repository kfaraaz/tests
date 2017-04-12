import fastparquet
import pandas as pd
import numpy as np

N=1000

columns_data=['c_int8_signed', 'c_uint8']

df = pd.DataFrame({'c_uint8':np.random.randint(0, 255, size=N) ,'c_int8_signed':np.random.randint(-128, 127, size=N)},columns=columns_data)
df = df.astype(dtype={"c_int8_signed":"int8", "c_uint8":"uint8"})

fastparquet.write('frmPandas_9.parquet', df, compression='GZIP')
