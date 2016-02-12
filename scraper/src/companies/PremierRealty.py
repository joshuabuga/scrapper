from ..properties.PremierRealtyProperty import PremierRealtyProperty
from BaseCompanyExcel import BaseCompanyExcel
class PremierRealty(BaseCompanyExcel):
	name ='Premier Realty'
	city ='Austin'
	state ='TX'

	def setup(self):
		self.set_col_headers( [
							('monthly_rent', 'rent'),
							('price_bedroom', '$/bed'),
							('property_type', 'property type'), 
							('premier_address', 'address'),
							('premier_unit', 'unit'), 	 
							('bedroom', 'bed'),
							('bathroom', 'bath'), 
							('available', 'move-in'), 
							('key_number', 'key'), 
							('tenant_phone', 'resident phone'),
							('description', ''),
							('website', ''),
							('virtual_tour', ''),
							('commission', ''),
							('bonus', ''),
							('deposit_paid_to', ''),
							('admin_fee_payable_to', '') 

							], 0)

		self.set_col_headers( [
							('monthly_rent', 'rent'),
							('price_bedroom', '$/bed'),
							('property_type', 'property type'), 
							('premier_address', 'address'), 
							('premier_unit', ''), 
							('bedroom', ''),
							('bathroom', ''), 
							('available', ''), 
							('key_number', ''),
							('mls', ''), 
							('tenant_phone', ''),
							('description', ''),
							('website', ''),
							('virtual_tour',''),
							('bonus', ''),
							('commission', ''),
							('deposit_paid_to', ''),
							('admin_fee_payable_to', '') 

							], 1)

	def new_property(self, property_data):
		prop = PremierRealtyProperty(property_data, self)	
		return prop
