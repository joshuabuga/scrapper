from ..properties.SspmProperty import SspmProperty
from BaseCompanyExcel import BaseCompanyExcel
class Sspm(BaseCompanyExcel):
	name ='State Street Property Management'
	city ='Austin'
	state ='TX'

	def setup(self):
		self.set_col_headers( [
							('property', 'property'),
							('zip_code', 'zip'),
							('address', 'address'),
							('unit', 'unit'), 
							('bedroom', ''), 
							('monthly_rent', ''),
							('price_bedroom', ''),  
							('description', ''), 
							('available', ''), 
							('lease_end', ''),
							('showing_instructions',''), 
							('tenant_phone',''),
							 
							], 1)

		self.set_col_headers( [
							('property', 'property'),
							('zip_code', 'zip'),
							('address', 'address'),
							('unit', 'unit'), 
							('bedroom', ''), 
							('monthly_rent', ''),
							('price_bedroom', ''),  
							('description', ''), 
							('available', ''), 
							('lease_end', ''),
							('showing_instructions',''), 
							('tenant_phone',''),
							 
							], 3)

		self.set_exempted_rows( [
							'ELMWOOD APARMTMENTS - 16 unit complex on the corner',
							'CAMPUS CROSSING - 30 unit complex on the corner',
							'STUDIOS',
							'Houses/Condos',
							], 'default', 70)


	def new_property(self, property_data):
		prop = SspmProperty(property_data, self)	
		return prop