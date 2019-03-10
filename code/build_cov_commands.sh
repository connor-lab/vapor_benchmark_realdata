segs="HA NA M1 PB1 PB2 PA NS1 NP"
for seg in $segs; do
    for f in single_full_length_assembled_contigs/*_"$seg"_*.fa; do
        samp=${f##*/}
        token=_"$seg"_annot_fullL.fa
        r1=reads/${samp/$token/_R1_001.fastq.gz}
        r2=reads/${samp/$token/_R1_001.fastq.gz}
        echo "minimap2 -ax sr $f $r1 $r2 | samtools view -bS -F 260 | samtools sort | samtools depth -a -d 0 - > cov_results/"$samp".cov"
    done
done
