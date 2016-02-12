from ..properties.UptownProperty import UptownProperty
from BaseCompanyCsv import BaseCompanyCsv
class Uptown(BaseCompanyCsv):
	name ='Uptown'
	city ='Austin'
	state ='TX'
	file_name = 'Uptown.csv'
	
	def setup(self):
		self.set_col_headers( [
							('status', 'status'),
							('m', 'm'),
							('property', 'property'),
							('address', 'address'), 
							('parking_space', 'pk'), 
							('uptown_area', 'area'), 
							('type', ''),
							('bedroom', ''), 
							('bathroom', ''), 
							('monthly_rent', ''), 
							('available', ''),
							('paid_utilities', ''), 
							('pets', ''),
							('tenant_phone', ''),		
							('description', ''),
							('key_number', ''),
							('gate_code',  '')      
							], 0)
		# self.set_col_headers( [], 1)
		self.set_col_headers( [
							('status', 'status'),
							('m', 'm'),
							('property', 'property'),
							('address', 'address'), 
							('parking_space', 'pk'), 
							('uptown_area', 'area'), 
							('type', ''),
							('bedroom', ''), 
							('bathroom', ''), 
							('monthly_rent', ''), 
							('available', ''),
							('paid_utilities', ''), 
							('pets', ''),
							('tenant_phone', ''),		
							('description', ''),
							('key_number', ''),
							('gate_code',  '')     
							], 1)
		# self.set_col_headers( [     
		# 					], 2)

	def new_property(self, property_data):
		prop = UptownProperty(property_data, self)	
		return prop







	