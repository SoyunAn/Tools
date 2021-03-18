#!/bin/bash

## -- Write JSON analyer -- PANDAS must be installed
if [ ! -f "read_json.py" ]
then
cat << EOF > "read_json.py"
import pandas as pd
idx_list = ['name','num_lumi','num_file','nevents','nlumis','nfiles','nblocks','size']
df = pd.read_json('temp.json')
#print(df['file'][0][0]['nevents'])
print(df['file'][0][0]['size'])
EOF
fi


## Run DAS Query
echo "Begin"
file_list=`dasgoclient --query="file dataset=/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15_ext1-v2/MINIAODSIM"`


cnt=1
sum=0
for f in $file_list
do


dasgoclient --query=$f --json > temp.json
size=`python read_json.py`

echo $cnt , $f , $size
sum=$(($sum+$size))

rm temp.json

cnt=$(($cnt+1))
done

echo $sum
