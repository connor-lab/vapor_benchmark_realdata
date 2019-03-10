fwd=$1
rev=$2
outf=$3
X=${outf##*/}
vapor_tmp=tmp/${X%%.*}.map.vp

# head 2 to take top result from outputted fasta, note vapor uses a single line per sequence
echo "vapor.py -o $vapor_tmp -fa refs/AuB_HA_allsp_nfu.fa -fq $fwd $rev"
vapor.py -o $vapor_tmp -fa refs/AuB_HA_allsp_nfu.fa -fq $fwd $rev
head -2 $vapor_tmp.fa > $vapor_tmp".fa_h"

# This quick counting procedure will work for minimap, but not BWA
# Here it is equivalent to retrieving and counting read .fq file
nmapped=$(minimap2 -ax sr $vapor_tmp".fa_h" $fwd $rev | samtools view -c -F 260)
nreads=$(cut -f5 "$vapor_tmp.out")

echo $nmapped,$nreads > $outf
