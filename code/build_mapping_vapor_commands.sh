for fwd in reads/*_R1_*; do
    rev="${fwd/_R1_/_R2_}" 
    x=results/"${fwd%.*}".out
    outf=mapping_results_vapor/${x##*/}
    echo bash code/vapor_then_map.sh $fwd $rev $outf
done
