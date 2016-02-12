from ..properties.LeePropertiesProperty import  LeePropertiesProperty
from BaseCompanyExcel import BaseCompanyExcel
class LeeProperties(BaseCompanyExcel):
	name ='Lee Properties'
	city ='Austin'
	state ='TX'
	
	def setup(self):
		self.set_col_headers( [
							('title', 'Property'),
							('size', 'size'),
							('square_feet', ''),
							('parking_space', ''),
							('available', ''), 
							('lease_end', ''), 
							('monthly_rent', ''), 
							('deposit', ''), 
							('form', ''),
							('commission', ''),		
							('tenant_phone', ''),
							('description', '')   ,
							('contact', '')      
							], 'default')
		self.set_exempted_rows( [
							'ONE BEDROOM',
							'STUDIO',
							'TWO BEDROOMS',
							'THREE BEDROOMS',
							'FOUR BEDROOMS',
							'FIVE BEDROOMS',
							'SIX BEDROOMS',
							'SEVEN BEDROOMS',
							'EIGHT BEDROOMS',
							'property',
							], 'default', 1000)
	    

	def new_property(self, property_data):
		prop = LeePropertiesProperty(property_data, self)	
		return prop
