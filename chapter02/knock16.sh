n=$(wc -l popular-names.txt | awk '{print $1}')
ln=$((n / 1))
split -l $ln popular-names.txt knock16/