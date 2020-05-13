
# my_script2.py


import pandas as pd

from my_lambdata.my_mod2 import check_nulls


df1 = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
print(df1.head())

print(check_nulls(df1))
