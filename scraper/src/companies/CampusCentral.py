from ..properties.CampusCentralProperty import CampusCentralProperty
from BaseCompanyExcel import BaseCompanyExcel
class CampusCentral(BaseCompanyExcel):
	name ='Campus and central'
	city ='Austin'
	state ='TX'
	
	def setup(self):
		self.set_col_headers( [
							('monthly_rent', 'Rent:'),
							('complex', 'complex'),
							('ccp_address', 'Address:'), 
							('bedroom', 'bed'), 
							('bathroom', 'bath'), 
							('parking_space', 'parking'), 
							('pets', ''), 
							('available', ''),		
							('tenant_phone', ''),
							('description', ''),      
							], 0)
		self.set_exempted_rows( [
							'Rent:	Complex	Address:',
							'ONE BEDROOMS',
							'TWO BEDROOMS',
							'THREE BEDROOMS',
							'FOUR BEDROOMS',
							'FIVE BEDROOMS',
							'SIX BEDROOMS',
							'SEVEN BEDROOMS',
							'EIGHT BEDROOMS',
							'PRE-LEASE LIST',
							'Studios',
							'Rooms',
				

							
							], 'default', 55)

	def new_property(self, property_data):
		prop = CampusCentralProperty(property_data, self)	
		return prop


	