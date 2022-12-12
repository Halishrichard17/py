import pandas as pd
 #ttt
# Reading the CSV file
df = pd.read_csv("Iris.csv")
 
# Printing top 5 rows
df.head()
df.shape
df.info()
df.describe()
