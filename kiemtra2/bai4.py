import  numpy as np
import pandas as pd
df = pd.read_csv('Data.csv')
print(df['Salary'].max())