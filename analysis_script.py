import csv
import pandas as pd

def read_csv():
  df= pd.read_csv("PPP.csv",sep=';')
  print(df)

