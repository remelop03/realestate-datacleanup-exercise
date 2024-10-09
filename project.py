import pandas as pd
import numpy as np
# This CSV file contains semicolons instead of comas as separator
ds=pd.read_csv('assets/real_estate.csv', sep=';')
prices=ds["price"]
max_price=np.max(prices)
print(ds.loc[ds["price"]==max_price])