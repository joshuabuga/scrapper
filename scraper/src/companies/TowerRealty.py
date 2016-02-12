from ..properties.TowerRealtyProperty import TowerRealtyProperty
from BaseCompanyExcel import BaseCompanyExcel
class TowerRealty(BaseCompanyExcel):
	name ='Tower Realty'
	city ='Austin'
	state ='TX'
	
	def setup(self):
		self.set_col_headers( [
							('property', 'property'),
							('address', 'address'),
							('unit', 'unit'), 
							('tower_type', 'type'), 
							('size', 'size'), 
							('monthly_rent', 'price'), 
							('available', 'avail'), 
							('phone_one', 'phone 1'),
							('phone_two', 'phone 2'),		
							('phone_three', 'phone 3'),
							('agent', 'agent')   ,
							('key_number', 'key'),
							('description', 'comments'),
							('tower_commission', 'commission'),
			     
							], 1)
		self.set_col_headers( [
							('property', 'property'),
							('address', 'address'),
							('unit', 'unit'), 
							('tower_type', 'type'), 
							('size', 'size'), 
							('monthly_rent', 'price'), 
							('available', 'avail'), 
							('phone_one', 'phone 1'),
							('phone_two', 'phone 2'),		
							('phone_three', 'phone 3'),
							('agent', 'agent')   ,
							('key_number', 'key'),
							('description', 'comments'),
							('tower_commission', 'commission'),
			     
							], 0)
		self.set_exempted_rows( [
							'HOUSES & DUPLEXES',
							'H O U S E S   A N D   D U P L E X E S',
							'AVAILABLE NOW',
							'PRE-LEASE',
							'CONDOS $ APARTMENTS',
							'Property',
							'Renewing',
							'Pending',
							'DEPOSIT EQUAL',
							'APPLICATION FEE',
							'Chesney Coker:',
							
							], 'default', 100)

	def new_property(self, property_data):
		prop = TowerRealtyProperty(property_data, self)	
		return prop