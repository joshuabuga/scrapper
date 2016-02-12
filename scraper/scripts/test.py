import csv
def read_csv():
		data_list=[]
		file_name='pearl21_pending.csv'

		with open(file_name, "rb") as f:
			for line in f:
				line=line.lower()
				line=line.replace(" ","")
				line=str(line)
				line=line.strip()
				print line
				if "unitnumber,size,p,amount,date,leasesigned,leasedbywhatcompany,updatedplan,t,c,s,ws,tr,charging,totalrent" in line:
	
					print "header found file will be processed"
					break
				else:
					print "dint find header"
			
			field_names=['Unit Number',	'size',	'P'	,'amount',	'date',	'lease signed',	'leased by what company','updated plan','T'	,'C','S','WS','TR','charging','total rent','empty_val']			

			reader=csv.DictReader(f,fieldnames=field_names, restval=None,delimiter=",")
			
			for row in reader:
				print row
				data_list.append(row)
		return data_list
		
		
read_csv()
print read_csv()
for x in read_csv():
	y=x['Unit Number']
	print y
