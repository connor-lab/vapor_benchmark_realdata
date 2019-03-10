for f in single_full_length_assembled_contigs/*_HA_*.fa; do
    samp=${f##*/}
    token=_HA_annot_fullL.fa
    r1=reads/${samp/$token/_R1_001.fastq.gz}
    r2=reads/${samp/$token/_R1_001.fastq.gz}
    echo "minimap2 -ax sr $f $r1 $r2 | samtools view -bS -F 260 | samtools stats | grep "^SN" > error_results/"$samp".out"
done
