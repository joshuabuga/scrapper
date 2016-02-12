import csv
from BaseCompany import BaseCompany
class BaseCompanyCsv(BaseCompany):
	"""docstring for BaseCompanyCsv"""
	
	def extract_data(self):
		
		data_list=[]
		with open(self.get_file_path(), "rb") as f:
			for line in f:
				line=line.lower()
				line=line.replace(" ","")
				line=str(line)
				line=line.strip()
				
				if self.get_col_headers('default', True, True, ',') in line:
					break
		
			reader=csv.DictReader(f,fieldnames=self.get_col_header_fields('default'), restval=None,delimiter=",",quoting=csv.QUOTE_ALL,quotechar='|')
			
			for row in reader:
				row_data = { 'meta': [], 'values': row }
				data_list.append(row_data)

		self.properties_data=data_list	
	
		return self.properties_data
	



	