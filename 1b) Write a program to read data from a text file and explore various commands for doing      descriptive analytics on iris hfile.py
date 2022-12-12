import pandas as pd
 
# Reading the txt file

df = pd.read_csv("Iris.txt")
# Printing top 5 rows
df.head()
df.shape
df.info()
df.describe()
