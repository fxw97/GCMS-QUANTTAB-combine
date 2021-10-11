import csv
import glob
import pandas as pd

def get_files(path):
    files=glob.glob(path)
    return files

path=r'./example data/2019出口数据/*/QUANTTAB.CSV'
files = get_files(path)
df_concat = pd.DataFrame()
columns=[]
for file in files:
    with open(file) as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        data_temp = pd.DataFrame(rows[19:])
        columns_temp = rows[3][0]
        df_concat = pd.concat([df_concat,data_temp[1]],axis=1)
        columns.append(columns_temp)

# 整合输出数据
df_concat.columns = columns
df_concat.insert(0,'compounds',data_temp[0])
# print(df_concat)
df_concat.to_csv('combined results.csv',index=None)