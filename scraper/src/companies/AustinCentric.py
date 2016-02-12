from ..properties.AustinCentricProperty import AustinCentricProperty
from BaseCompanyExcel import BaseCompanyExcel
class AustinCentric(BaseCompanyExcel):
	name ='Austin Centric'
	city ='Austin'
	state ='TX'
	
	def setup(self):
		self.set_col_headers( [
							('property_area', 'Type / Area'),
							('monthly_rent', ''),
							('address', ''),
							('unit', ''),
							('bedroom', ''), 
							('bathroom', ''), 
							('available', ''), 
							('key_number', ''),
							('mls', ''), 
							('tenant_phone', ''), 
							('description', ''),
							('bonus', ''),
							('commission', ''),		
							('rent_payable_to', '')   ,
							('fee_payable_to', '')   ,      
							], 0)

	def new_property(self, property_data):
		prop = AustinCentricProperty(property_data, self)	
		return prop