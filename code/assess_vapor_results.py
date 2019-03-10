from Bio import pairwise2
from Bio import SeqIO
import sys
from Bio.pairwise2 import format_alignment
import subprocess as sp

vaporoutf = sys.argv[1]

# Retrieve the relevant contig file
contigf = "single_full_length_assembled_contigs/" + vaporoutf.split(".")[0].split("/")[1]+"_annot_fullL.fa"
contig = [r for r in SeqIO.parse(contigf, "fasta")][0]
contigseq = str(contig.seq)
contigh = contig.description
# Retrieve the first VAPOR classification
vpr = [r for r in SeqIO.parse(vaporoutf, "fasta")][0]
vpseq = str(vpr.seq)
vph = vpr.description
# Get Lev distance and PID
aln = pairwise2.align.globalms(contigseq, vpseq, 0, -1, -1, -1,penalize_end_gaps=(True, False), one_alignment_only=True)[0]
alnscore = aln[2]
alnlen = len(aln[0])
pid = (1+float(alnscore)/alnlen)*100
# Classify the contig with BLAST
bout = sp.getoutput("python3 code/blast_classify_contig.py %s" % contigf).split(",")[1:]
blast_classification, blast_pid = bout
#sys.stderr.write("python3 code/blast_classify_contig.py %s \n" % contigf)


print(contigf.split("/")[-1]+","+vph+","+str(alnlen)+","+str(alnscore)+","+str(pid)+","+blast_classification+","+blast_pid)
