from ..properties.WestCampusLivingProperty import WestCampusLivingProperty
from BaseCompanyExcel import BaseCompanyExcel
class WestCampusLiving(BaseCompanyExcel):
	name ='Buckingham Square'
	city ='Austin'
	state ='TX'
	def setup(self):
		self.set_col_headers( [
							('unit', 'unit'),
							('type', 'type'),
							('countertops_color', 'Countertops Color') ,
							('bedroom', 'Beds'),
							('bathroom', 'Baths'),
							('square_feet', ''),
							('monthly_rent', ''),
							('deposit', ''),
							('available', ''),
							('b_status', ''),


							
							], 'default')

		self.set_exempted_rows( [

							'	Necessary Application ',
							'	Click Here to Download',
							'	Click Here to Download',
							'	Click Here for ',
							], 'default', 500)

	def new_property(self, property_data):
		prop = WestCampusLivingProperty(property_data, self)	
		return prop
