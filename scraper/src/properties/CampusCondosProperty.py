from BaseCompanyProperty import BaseCompanyProperty
from ..lib.helpers import *
class CampusCondosProperty(BaseCompanyProperty):
	
	def setup(self):
		self.commission = '.4'
		self.bonus = ''
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = 'Campus Condos | App Fee $100, Deposit = 1 Month\'s Rent'
		self.pets='NO'
		self.pets_info='NO'

	def set_status(self, value):
		self.status = 'Leased' if self.is_highlighted() and not self.is_highlighted(None,'white') else 'Active'

	
	def set_title(self, value):
		self.title = str(self.data['values']['bed_bath'] + ' ' + self.get_attribute('unit')).replace('.0','')

	def set_bedroom(self, value):
		self.bedroom = self.data['values']['size'].split('/', 1 )[0]

	def set_bathroom(self, value):
		size = self.data['values']['size'].split('/', 1)
		self.bathroom = size[1] if len(size) > 1 else '0'

	def set_price_bedroom(self, value):
		rent = str_to_float(self.get_attribute('monthly_rent')) 
		bedroom = str_to_float(self.get_attribute('bedroom'))
		
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)