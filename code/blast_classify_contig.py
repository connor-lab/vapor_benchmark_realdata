import sys
import subprocess as sp
import itertools as it
from Bio import pairwise2
from Bio import SeqIO

def lev(s1, s2):
    return pairwise2.align.globalms(s1, s2, 0, -1, -1, -1, penalize_end_gaps=(True, False), one_alignment_only=True)

""" This script externally calls BLAST, then sorts the output, firstly on evalue (lowest), then on bitscore (highest) """
""" Takes two arguments; a database, and a query fasta """
""" Assumes there is only a single sequence in the query fasta; i.e. one full length contig """

queryf = sys.argv[1]
db = "refs/AuB_all_allsp_nf.fa"
blstr = "blastn -query %s -db %s -outfmt '6 qseqid sseqid evalue score length'" % (queryf, db)
#sys.stderr.write(blstr+"\n")
queryseq = str([r for r in SeqIO.parse(queryf, "fasta")][0].seq)
dbseqs = {r.description.split()[0]:str(r.seq) for r in SeqIO.parse(db, "fasta")}
rawblastres = [l.strip() for l in sp.check_output(blstr, shell=True).decode("utf-8").split("\n") if l !=  '']
results = []
for l in rawblastres:
    spl = l.split("\t")
    query, ref, evalue, score, length = spl
    evalue = float(evalue)
    score = float(score)
    length = int(length)
    results.append([ref, evalue, score, length])

#sys.stderr.write("Got BLAST results\n")
#sys.stderr.write("Sorting results\n")

bestrefs = []
# Sorting on a tuple uses both indices, the first, then second
# Negative because higher bitscore is better, so taking min we use negative
besteval, bestbitscore, bestlength = min(results, key = lambda x: (x[1], -x[2], -x[3]))[1:]

for result in results:
    ref, evalue, bitscore, length = result
    if evalue == besteval and bitscore == bestbitscore and length == bestlength:
        refseq = dbseqs[ref]
        aln = lev(queryseq, refseq)[0]
        pid = 100.*(1+aln[2]/float(len(aln[0])))
        print(queryf+","+ref+","+str(pid))
        # Only output one result
        break

			
