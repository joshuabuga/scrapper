from ..properties.RealtyProsProperty import RealtyProsProperty
from BaseCompanyExcel import BaseCompanyExcel
class RealtyPros(BaseCompanyExcel):
	name ='Realty Pros'
	city ='Austin'
	state ='TX'
	def setup(self):
		self.set_col_headers( [
							('property', 'property'),
							('unit', 'unit'),
							('address', 'address'),
							('pros_monthly_rent', 'price'), 
							('bedroom', 'bed'), 
							('bathroom', ''),
							('description', ''), 
							('key_number', ''), 
							('available', ''), 
							('end_date', ''),
							('empty','')       
							], 0)
		self.set_col_headers( [
							('property', 'property'),
							('address', 'address'),
							('unit', 'unit'),
							('pros_monthly_rent', 'price'), 
							('bedroom', ''), 
							('bathroom', ''),
							('description', ''), 
							('tenant_phone', ''), 
							('available', ''),
							('move_out',''),
							('empty','        ')    
							], 1)
		self.set_exempted_rows( ['Property	Address',
								 'Bed	Bath',
								 'Coming SOON',
								'ONE BEDROOMS',
								'Property	Unit Address',
								'TWO BEDROOMS',
								'',
								'Bedrooms',
								'AUGUST 2015 ',
								'THREE + BEDROOMS',
								'THREE  BEDROOMS',
								'STUDIOS',

								], 
							'default', 100)


	def new_property(self, property_data):
		prop = RealtyProsProperty(property_data, self)	
		return prop



	