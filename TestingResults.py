
import pandas as pd
import pickle



input_bp='data/Resultsbp.pkl'
input_mf='data/Resultsmf.pkl'
input_cc='data/Resultscc.pkl'

bp = pd.read_pickle(input_bp)
mf = pd.read_pickle(input_mf)
cc = pd.read_pickle(input_cc)



print(bp.loc['Q13137'])
print(mf.loc['Q13137'])
print(cc.loc['Q13137'])


input_accession='data/AccessionNumber_Structure_StatusFileWithAccessionIndex.pkl'
df = pd.read_pickle(input_accession)
print(df.iloc[1])
df=df[df['status']==True]
print(df)
for i in range(0, len(df)):
    print(df.iloc[i])
    # raw_input()
