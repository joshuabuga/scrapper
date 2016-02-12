from ..properties.PearlLeeProperty import PearlLeeProperty
from BaseCompanyExcel import BaseCompanyExcel
class PearlLee(BaseCompanyExcel):
	name ='21 Pearl Lee Properties'
	city ='Austin'
	state ='TX'
	def setup(self):
		self.set_col_headers( [
							('unit', 'Unit #'),
							('floor_plan', 'Floor Plan'),
							('plan_description', 'Plan Description'),
							# ('type', 'type'), 
							# ('b_b', 'B/B'), 
							('floor', ''),
							('square_feet', ''), 
							('monthly_rent', ''), 
							('price_bedroom', ''), 
							('pearl_status', ''), 
							('available', '')      
							], 0)
		self.set_col_headers( [
							('unit', 'unit number'),
							('size', 'size'),
							('p', 'P'),
							('', 'amount'), 
							('available', ''), 
							('lease_signed', ''),
							('leased_by what_company', ''), 
							('parking_space', ''), 
							('c', ''), 
							('s', ''), 
							('ws', ''),
							('tr', ''), 
							('charging', ''), 
							('monthly_rent', '')     
							], 1)

	def new_property(self, property_data):
		prop = PearlLeeProperty(property_data, self)	
		return prop





	