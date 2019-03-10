import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
sns.set_style("ticks")
import sys
import pandas as pd

fig = plt.figure(figsize=(10,10))

df = pd.read_csv(sys.argv[1])
fnames = df['FNAME']

df.fillna(value=0, inplace=True)

arr = df.values[:,1:].astype(int)
gain = arr[:,1]-arr[:,0]

print("Rows with negative gain:")
for ri in range(len(gain)):
    if gain[ri] < 0:
        print(ri, arr[ri])

print("Mean gain", np.mean(gain))
plt.hist(gain, color='#dd5134',bins=20)
plt.ylabel("Count",labelpad=10,size=14)
plt.xlabel("Additional Mapped Reads",labelpad=10,size=14)

plt.savefig("mapping_with_and_without_vapor_realdata.pdf", format="pdf", dpi=900)
