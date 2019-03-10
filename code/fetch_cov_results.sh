for f in error_results/*; do
    samp=${f##*/}
    samp=${samp/_HA_annot_fullL.fa.out/}
    error=$(grep error $f | cut -f 3;)
    typo=$(grep "$samp", metadata/sample_types.csv)
    echo $typo,$error
    
done
