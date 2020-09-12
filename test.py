import numpy as np
import pandas as pd
import csv

data = open("train_data.txt",mode='r', encoding='utf-8')
f = open('pre.csv', mode='w', encoding='utf-8')

wr = csv.writer(f)

look = [(i.rstrip("\n")).split("\t") for i in data]


for i in np.arange(0,len(look)): wr.writerow(look[i])



df = pd.DataFrame(look)
print(df)
