from ..properties.Realty512Property import Realty512Property
from BaseCompanyExcel import BaseCompanyExcel
class Realty512(BaseCompanyExcel):
	name =' 512 Realty '
	city ='Austin'
	state ='TX'
	def setup(self):
		self.set_col_headers( [], 0)
		
		self.set_col_headers( [], 1)
		self.set_col_headers( [], 2)

		
		self.set_col_headers( [
							('property', 'property'),
							('realty_address', 'address'),
							('512_available', 'avail'),
							('bedroom', ''), 
							('bathroom', ''), 
							('monthly_rent', ''),
							('price_bedroom', ''), 
							('512_area', ''), 
							('laundry', ''), 
							('512_description', ''),
							('prop_manager', ''),
							('model', ''),
							('paid_utilities', ''), 
							('tenant_phone', ''),
							('email', ''), 
							('bonus', '')      
							], 3)
		# self.set_col_headers( [
		# 					('property', 'property'),
		# 					('address', 'address'),
		# 					('512_available', 'avail'),
		# 					('bedroom', 'br'), 
		# 					('bathroom', 'ba'), 
		# 					('monthly_rent', 'rent'),
		# 					('price_bedroom', '$/br'), 
		# 					('512_area', 'area'), 
		# 					('laundry', 'laundry'), 
		# 					('description', 'description'),
		# 					('prop_manager', ''),
		# 					('paid_utilities', ''), 
		# 					('tenant_phone', ''),
		# 					('email', ''), 
		# 					('bonus', '')  ], 4)
		# self.set_col_headers( [('property', 'property'),
		# 					('address', 'address'),
		# 					('512_available', 'avail'),
		# 					('bedroom', 'br'), 
		# 					('bathroom', 'ba'), 
		# 					('monthly_rent', 'rent'),
		# 					('price_bedroom', '$/br'), 
		# 					('512_area', 'area'), 
		# 					('laundry', 'laundry'), 
		# 					('description', 'description'),
		# 					('prop_manager', ''),
		# 					('paid_utilities', ''), 
		# 					('tenant_phone', ''),
		# 					('email', ''), 
		# 					('bonus', '')  ], 5)
		# self.set_col_headers( [('property', 'property'),
		# 					('address', 'address'),
		# 					('512_available', 'avail'),
		# 					('bedroom', 'br'), 
		# 					('bathroom', 'ba'), 
		# 					('monthly_rent', 'rent'),
		# 					('price_bedroom', '$/br'), 
		# 					('512_area', 'area'), 
		# 					('laundry', 'laundry'), 
		# 					('description', 'description'),
		# 					('prop_manager', ''),
		# 					('paid_utilities', ''), 
		# 					('tenant_phone', ''),
		# 					('email', ''), 
		# 					('bonus', '')  ], 6)
		# self.set_col_headers( [('property', 'property'),
		# 					('address', 'address'),
		# 					('512_available', 'avail'),
		# 					('bedroom', 'br'), 
		# 					('bathroom', 'ba'), 
		# 					('monthly_rent', 'rent'),
		# 					('price_bedroom', '$/br'), 
		# 					('512_area', 'area'), 
		# 					('laundry', 'laundry'), 
		# 					('description', 'description'),
		# 					('prop_manager', ''),
		# 					('paid_utilities', ''), 
		# 					('tenant_phone', ''),
		# 					('email', ''), 
		# 					('bonus', '')  ], 7)
		# self.set_col_headers( [('property', 'property'),
		# 					('address', 'address'),
		# 					('512_available', 'avail'),
		# 					('bedroom', 'br'), 
		# 					('bathroom', 'ba'), 
		# 					('monthly_rent', 'rent'),
		# 					('price_bedroom', '$/br'), 
		# 					('512_area', 'area'), 
		# 					('laundry', 'laundry'), 
		# 					('description', 'description'),
		# 					('prop_manager', ''),
		# 					('paid_utilities', ''), 
		# 					('tenant_phone', ''),
		# 					('email', ''), 
		# 					('bonus', '')  ], 8)
		# self.set_col_headers( [('property', 'property'),
		# 					('address', 'address'),
		# 					('512_available', 'avail'),
		# 					('bedroom', 'br'), 
		# 					('bathroom', 'ba'), 
		# 					('monthly_rent', 'rent'),
		# 					('price_bedroom', '$/br'), 
		# 					('512_area', 'area'), 
		# 					('laundry', 'laundry'), 
		# 					('description', 'description'),
		# 					('prop_manager', ''),
		# 					('paid_utilities', ''), 
		# 					('tenant_phone', ''),
		# 					('email', ''), 
		# 					('bonus', '')  ], 9)
		# self.set_col_headers( [('property', 'property'),
		# 					('address', 'address'),
		# 					('512_available', 'avail'),
		# 					('bedroom', 'br'), 
		# 					('bathroom', 'ba'), 
		# 					('monthly_rent', 'rent'),
		# 					('price_bedroom', '$/br'), 
		# 					('512_area', 'area'), 
		# 					('laundry', 'laundry'), 
		# 					('description', 'description'),
		# 					('prop_manager', ''),
		# 					('paid_utilities', ''), 
		# 					('tenant_phone', ''),
		# 					('email', ''), 
		# 					('bonus', '')  ], 10)
		self.set_exempted_rows( [
							'7 + Bedrooms',
							'6 Bedrooms',
							'5 Bedrooms',
							'4 Bedrooms',
							'3 Bedrooms',
							'2 Bedrooms',
							'1 Bedrooms',
							'studios'
							], 'default', 10)






	def new_property(self, property_data):
		prop = Realty512Property(property_data, self)	
		return prop



	