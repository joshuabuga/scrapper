from ..properties.ConsolidatedProperty import ConsolidatedProperty
from BaseCompanyExcel import BaseCompanyExcel
class ConsolidatedList(BaseCompanyExcel):
	city ='Austin'
	state ='TX'
	def setup(self):
		self.set_col_headers( [
							('status','status'),
							('company_name','Company'),
							('m',''),
							('title',''),
							('address',''),
							('unit',''),
							('city',''),
							('state',''),
							('zip_code',''),
							('square_feet',''),
							('forms',''),
							('parking_space',''),
							('area',''),
							('type',''),
							('bedroom',''),
							('bathroom',''),
							('monthly_rent',''),
							('price_bedroom',''),
							('available',''),
							('paid_utilities',''),
							('pets',''),
							('pets_info',''),
							('laundry',''),
							('web_description',''),
							('tenant_phone',''),
							('gate_code',''),
							('key_number',''),
							('email',''),
							('commission',''),
							('bonus',''),
							('deposit_paid_to',''),
							('description',''),
							('double_occupancy',''),
							('dbl_occ_info',''),
							('listing_type',''),
							('pool','')
							 
							], 'default')

		

		
	def new_property(self, property_data):
		prop = ConsolidatedProperty(property_data, self)	
		return prop

