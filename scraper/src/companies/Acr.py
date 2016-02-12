from ..properties.AcrProperty import AcrProperty
from BaseCompanyExcel import BaseCompanyExcel
class Acr(BaseCompanyExcel):
	name ='ACR'
	city ='Austin'
	state ='TX'

	def setup(self):
		self.set_col_headers( [
							('property_name', 'Property Name'),
							('acr_address', 'address'),
							('available', 'Availability'),
							('acr_type', 'type'), 
							('bedroom', 'BR'), 
							('study', 'study'), 
							('price_bedroom', ''),
							('monthly_rent', ''), 
							('bathroom', ''), 
							('acr_area', ''), 
							('description', ''), 
							('tenant_phone',''),
							('deposit',''), 
							('prop_id',''), 
							], 0)

		# self.set_col_headers( [
		# 					('property_name', 'Property Name'),
		# 					('acr_address', 'address'),
		# 					('available', 'Availability'),
		# 					('acr_type', 'type'), 
		# 					('bedroom', 'BR'), 
		# 					('study', 'study'), 
		# 					('price_bedroom', ''),
		# 					('monthly_rent', ''), 
		# 					('bathroom', ''), 
		# 					('acr_area', ''), 
		# 					('description', ''), 
		# 					('tenant_phone',''),
		# 					('deposit',''), 
		# 					('prop_id',''), 
		# 					], 1)

		self.set_exempted_rows( [
							'bedrooms',
							'bedrooms + study',
							'eff'
							], 'default', 5)


	def new_property(self, property_data):
		prop = AcrProperty(property_data, self)	
		return prop

