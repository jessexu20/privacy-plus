import csv

import csv
    #Read in the file  
cr = csv.reader(open('final_overall.csv',"rb"))

cw1 = csv.writer(open("feature_overall.csv","wb"))

cr.next()
for row in cr:
	if len(row) > 26: 
	#	print row[25],row[26], row[4]
		count = 0
		pro = 0
		while count < 26:
			if row[count]!= ' ':
				pro += 1	
			count += 1
		if row[8] == "female":
			gender = 0
		else:
			gender = 1 

		print row
		level = 0
		if (row[4] != ' ') and (int)(row[4]) < 762:
			level = 1

		#cw.writerow([gender,level,(float)(pro/25.0)])
		#cw.writerow([gender,row[10],(float)(pro/25.0)])
		cw1.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],(float)(pro/25.0)])
