import pandas as pd
import csv

df=pd.read_csv("brightstars.csv")

g=["Luminosity","Star_name"]

for i in g :
    del df[i]

df.to_csv("brightstars.csv")