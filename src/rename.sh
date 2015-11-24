temp="T"
python renameOrg.py $1 $temp$1
python renamePlace.py $temp$1 $2
rm $temp$1
echo $temp$1