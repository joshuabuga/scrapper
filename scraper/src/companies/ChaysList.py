from ..properties.ChaysListProperty import ChaysListProperty
from BaseCompanyExcel import BaseCompanyExcel
class ChaysList(BaseCompanyExcel):
	name ='Chay\'s List'
	city ='Austin'
	state ='TX'
	
	def setup(self):
		self.set_col_headers( [
							('status', 'status'),
							('property', 'property'),
							('type', 'property type'),
							('address', 'address'),
							('available', 'avail'), 
							('bedroom', 'br'), 
							('bathroom', 'ba'), 
							('monthly_rent', 'rent'), 
							('price_bedroom', ''), 
							('area', ''),
							('description', ''),		
							('tenant_phone', ''),
							('commission', '')   ,
							('bonus', '')      
							], 'default')
		self.set_exempted_rows( [
							'ONE BEDROOMS',
							'TWO BEDROOOMS',
							'TWO BEDROOMS',
							'THREE BEDROOMS',
							'FOUR BEDROOMS',
							'FIVE BEDROOMS',
							'SIX BEDROOMS',
							'SEVEN BEDROOMS',
							'EIGHT BEDROOMS',
							], 'default', 20)

	def new_property(self, property_data):
		prop = ChaysListProperty(property_data, self)	
		return prop