# This file builds a csv from mapping_results_vapor and mapping_results_novapor results

echo FNAME,N_MAPPED_NO_VAPOR,N_MAPPED_VAPOR,N_SURVIVING_READS
for f in mapping_results_novapor/*; do 
    fname=${f##*/}
    novapor=$(cat mapping_results_novapor/$fname)
    vapor=$(cat mapping_results_vapor/$fname)
    echo $fname,$novapor,$vapor
done
