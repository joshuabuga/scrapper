from ..properties.ElyProperty import ElyProperty
from BaseCompanyExcel import BaseCompanyExcel
class Ely(BaseCompanyExcel):
	name ='Ely'
	city ='Austin'
	state ='TX'
	
	def setup(self):
		self.set_col_headers( [
							('prop_no', 'Prop #'),
							('name', 'Name'),
							('address', 'Address'),
							('unit', ''),
							('size', ''), 
							('key_number', ''), 
							('monthly_rent', ''), 
							('deposit', ''),
							('square_feet', ''),
							('available', ''), 
							('description', ''), 	
							('tenant_phone', ''),  
							], 0)
		self.set_exempted_rows( [
							'Prop #	Name	Address	Unit		Size',
							'2813 Rio Grande St',
							], 'default', 70)

	def new_property(self, property_data):
		prop = ElyProperty(property_data, self)	
		return prop