from ..properties.CampusCondosProperty import CampusCondosProperty
from BaseCompanyExcel import BaseCompanyExcel
class CampusCondos(BaseCompanyExcel):
	name ='CampusCondos'
	city ='Austin'
	state ='TX'
	
	def setup(self):
		self.set_col_headers( [
							('size', 'size'),
							('monthly_rent', 'rent'),
							('bed_bath', ''),
							('unit', ''), 
							('address', ''), 
							('tenant_phone', ''), 
							('available', ''),
							('description', '')      
							], 0)

		self.set_exempted_rows(
			['Size	Rent	1 BED ',
			'Leasing Guidelines',
			'* Keys from Office',
			'* Separate Checks',
			'*All Applicants'],


			 'default', 40)


	def new_property(self, property_data):
		prop = CampusCondosProperty(property_data, self)	
		return prop
