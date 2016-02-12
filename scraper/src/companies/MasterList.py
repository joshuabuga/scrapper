from ..properties.MasterListProperty import MasterListProperty
from BaseCompanyExcel import BaseCompanyExcel
class MasterList(BaseCompanyExcel):
	
	def setup(self):
		self.set_col_headers( [
							('external_id', 'External ID'),
							('status','status'), 
							('company', 'Company'), 
							('m', ''), 
							('title', ''),
							('address', ''), 
							('unit', ''),
							('city', ''),
							('state',''),
							('zip_code', ''),
							('square_feet', ''), 
							('forms', ''),
							('parking_space', ''), 
							('area', ''),
							('type', ''),
							('bedroom',''),
							('bathroom',''),
							('monthly_rent',''), 
							('price_bedroom', ''),
							('available', ''), 
							('paid_utilities', ''),
							('pets', ''),
							('pets_info',''),
							('laundry',''),
							('web_description',''), 
							('tenant_phone',''),
							('gate_code', ''), 
							('key_number', ''),
							('email', ''),
							('commission', ''),
							('bonus', ''),
							('deposit_paid_to', ''), 
							('description', ''),
							('double_occupancy', ''),
							('dbl_occ_info', ''),
							('listing_type', ''), 
							('pool', '')
						    ], 0)

		# self.set_exempted_rows( [
		# 					'     '
							
		# 					], 'default', 5)
	


	def new_property(self, property_data):
		prop =MasterListProperty(property_data, self)	
		return prop
