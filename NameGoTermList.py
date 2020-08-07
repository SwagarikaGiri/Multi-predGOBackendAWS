import pickle
import numpy as np
import pandas as pd
import csv


df = pd.DataFrame(columns=['accession_no', 'original_name', 'combined_name'])
ont = dict()
k=0
with open("data/go.obo", 'r') as f:
    i = 0
    lines = f.readlines()
    while i < len(lines):
        line = lines[i]
        line = line.strip()
        if line == '[Term]':
            id = lines[i+1].split(': ')[1].strip()
            name = lines[i+2].split(': ')[1]
            temp_name = name.split()
            name = []
            for j in temp_name:
                name.append(j.title())
            org_name = " ".join(name)
            name = id+"("+org_name+")"
            # name = f"{id} ({org_name})"
            df.loc[k] = [id] + [org_name] + [name]
            k += 1
        i = i+1

df = df.set_index('accession_no')
print(df)
df.to_pickle("GotermNameFile.pkl")