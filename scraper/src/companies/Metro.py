from ..properties.MetroProperty import MetroProperty
from BaseCompanyExcel import BaseCompanyExcel

class Metro(BaseCompanyExcel):
	name ='Metro'
	city ='Austin'
	state ='TX'
	
	
	def setup(self):
		self.set_col_headers( [
							('property_name', 'Property Name'),
							('unit', 'unit'),
							('address', 'address'), 
							('size', 'size'), 
							('metro_monthly_rent', 'rent'), 
							('available', ''),
							('tenant_phone', ''), 
							('description', ''), 
							('gate_code', ''), 
							('agent', ''),
							('paid_utilities', '')     
							], 0)

		self.set_col_headers( [
							('property_name', 'Property Name'),
							('unit', 'unit'),
							('address', 'address'), 
							('size', 'size'), 
							('metro_monthly_rent', 'rent'), 
							('available', 'Avail.'),
							('tenant_phone', ''), 
							('description', ''), 
							('gate_code', ''), 
							('agent', ''),
							('paid_utilities', '')     
							], 1)
		self.set_col_headers( [
							('property_name', 'Property Name'),
							('unit', 'unit'),
							('address', 'address'), 
							('size', 'size'), 
							('metro_monthly_rent', 'rent'), 
							('available', 'Avail.'),
							('tenant_phone', 'PH#'), 
							('description', 'Comments'), 
							('gate_code', 'Gate Code'), 
							('agent', 'Agent'),
							('paid_utilities', 'Utils'),
							(' ',' '),
		
							('leased','Leased')    
							], 2)
		self.set_exempted_rows( [
							'SUMMER SUBLEASING ',
							'one bedroom',
							'two bedroom',
							'three bedroom',
							'four bedroom',
							'five + bedroom',
							'studio'
							], 'default', 40)

	

	def new_property(self, property_data):
		
		prop = MetroProperty(property_data, self)	
		return prop
	
	