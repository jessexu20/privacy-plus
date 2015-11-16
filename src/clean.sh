python handleInvalid.py $1 "temp.csv"
python CSVParser.py "temp.csv" $2
rm "temp.csv"
