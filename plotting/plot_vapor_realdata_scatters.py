import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; 
sns.set()
sns.set_style("ticks")
import sys
import pandas as pd
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FormatStrFormatter
np.set_printoptions(threshold=np.nan)

def plot_boxes(df1, titles="HA NA PB1 PB2 PA NP NS1 M1".split()):
    fig, axes = plt.subplots(nrows=4, ncols=2, sharey=True, sharex=True, figsize=(10,10))
    i = 0
    flat = axes.flatten()
    dfc = 0
    minvp = min(df1['VAPOR_PID'])
    minbl = min(df1['BLAST_PID'])
    mini = min([minvp, minbl])
    for i, title in enumerate(titles):
        df = df1.loc[df1['SEGMENT'] == title]
        df.fillna
        axi = flat[i]
        line = np.linspace(mini, 100)
        axi.plot(line,line,color='black')
        axi.scatter(x=df['VAPOR_PID'], y=df['BLAST_PID'], alpha=0.5, s=30)
        axi.set_title(title)

    lastax = fig.add_subplot(111, frameon=False)
    params = {'mathtext.default': 'regular' }          
    plt.rcParams.update(params)
    plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
    plt.grid(False)
    plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.07)
    lastax.set_ylabel("PID For BLAST Contig Classification",labelpad=25,size=14)
    lastax.set_xlabel("PID For VAPOR Read Classification",labelpad=15,size=14)
    plt.subplots_adjust(wspace=0.18, hspace=0.25)
    plt.savefig("realdata_blast_v_vapor_scatters.pdf", format="pdf", dpi=900)

dfs = []
for fname in sys.argv[1:]:
    df = pd.read_csv(fname, na_filter = False)
    # Create additional segment column
    segments = [l.split("_annot_")[0].split("_")[-1] for l in df['CONTIG_FILE']]
    df['SEGMENT'] = segments

plot_boxes(df)
