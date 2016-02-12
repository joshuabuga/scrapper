from ..properties.UptownProperty import UptownProperty
from BaseCompanyExcel import BaseCompanyExcel
class UptownExcel(BaseCompanyExcel):
	name ='Uptown'
	city ='Austin'
	state ='TX'
	
	def setup(self):
		self.set_col_headers( [
							('uptown_status', 'status'),
							('m', 'm'),
							('property', 'property'),
							('uptown_address', 'address'), 
							('parking_space', 'pk'), 
							('uptown_area', 'area'), 
							('uptown_type', ''),
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
		# self.set_col_headers( [
							    
		# 					], 1)
		# self.set_col_headers( [
							    
		# 					], 2)
		self.set_col_headers( [
							('uptown_status', 'status'),
							('m', 'm'),
							('property', 'property'),
							('uptown_address', 'address'), 
							('parking_space', 'pk'), 
							('uptown_area', 'area'), 
							('uptown_type', ''),
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
		self.set_exempted_rows( [

							'609 Elmwood place',
							'MOVE IN DATE',
							'------------'
							], 'default', 100)

	def new_property(self, property_data):
		prop = UptownProperty(property_data, self)	
		return prop


		
