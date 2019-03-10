for fwd in reads/*_R1_*; do
    rev="${fwd/_R1_/_R2_}" 
    x=results/"${fwd%.*}".out
    outf=mapping_results_novapor/${x##*/}
    echo "minimap2 -ax sr refs/vaccine_references_HA.fa $fwd $rev | samtools view -c -F 260  > $outf"
done
