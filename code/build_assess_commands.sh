
for f in vapor_results/*; do
    echo "python3 code/assess_vapor_results.py $f > $f.csv"
done
