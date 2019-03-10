#echo CONTIG_FILE,VAPOR_CLASSIFICATION,ALIGNMENT_LENGTH,VAPOR_LEV,VAPOR_PID,BLAST_CLASSIFICATION,BLAST_PID

for f in vapor_results/*; do
    echo "python3 code/assess_vapor_results.py $f > $f.csv"
done
