import subprocess as sp
import sys
import os

A_segs = {"M1":"A_M1_allsp_nfu.fa",
"NA":"A_NA_allsp_nfu.fa",
"NS1":"A_NS1_allsp_nfu.fa",
"NP":"A_NP_allsp_nfu.fa",
"PA":"A_PA_allsp_nfu.fa",
"HA":"A_HA_allsp_nfu.fa",
"PB1":"A_PB1_allsp_nfu.fa",
"PB2":"A_PB2_allsp_nfu.fa"}

B_segs = {"M1":"B_M1_nfu.fa",
"NA":"B_NA_nfu.fa",
"NS1":"B_NS1_nfu.fa",
"NP":"B_NP_nfu.fa",
"PA":"B_PA_nfu.fa",
"HA": "B_HA_nfu.fa",
"PB1":"B_PB1_nfu.fa",
"PB2": "B_PB2_nfu.fa"}

with open("metadata/sample_types.csv") as sample_types:
    typesd = {l.strip().split(",")[0] : l.strip().split(",")[1] for l in sample_types}

for fn in os.listdir("single_full_length_assembled_contigs/"):
    sample_name = "_".join(fn.split("_annot_")[0].split("_")[:-1])
    # Get Flu type from metadata
    sample_type = typesd[sample_name]
    # Get segment type
    seg = fn.split("_annot_")[0].split("_")[-1]
    if sample_type == "A":
        ref = "refs/"+A_segs[seg]
    elif sample_type == "B":
        ref = "refs/"+B_segs[seg]
    readsf1 = "reads/"+fn.split("_%s_" % seg)[0] + "_R1_001.fastq.gz"
    readsf2 = "reads/"+fn.split("_%s_" % seg)[0] + "_R2_001.fastq.gz"
    outf = "vapor_results/"+sample_name+"_"+seg+".vpout"
    # Finally build command
    print("vapor.py --return_seqs -fa %s -fq %s %s > %s" % (ref, readsf1, readsf2, outf))
