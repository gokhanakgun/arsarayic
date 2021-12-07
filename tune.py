import os
import pandas as pd

root = 'beyoglu'
root2 = 'beyoglu_new'
for filename in os.listdir(root):
    df = pd.read_csv(root+'/'+filename)
    df = df.pivot_table(values='rayic', index=df.sokak, columns='yil', aggfunc='first')
    df.to_csv(root2+'/'+filename)
