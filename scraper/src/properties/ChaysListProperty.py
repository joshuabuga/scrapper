from BaseCompanyProperty import BaseCompanyProperty
class ChaysListProperty(BaseCompanyProperty):
	def setup(self):
		self.forms ='TAR + ADDENDA'
		self.deposit_paid_to = 'Metro Realty | $100 App Fees, Deposit = 1st Month\'s Rent'
	
	
	def set_status(self, value):
		self.status = 'Active' if value == 'A' else 'Leased' 

	def set_title(self, value):
		self.title = self.get_attribute('property') 

	def set_address(self, value):

		self.address = '' if len(self.data['values']['address']) == 0 else self.data['values']['address'].split(' ', 1 )[1]

	def set_unit(self, value):
		self.unit = '' if len(self.data['values']['address']) == 0 else self.data['values']['address'].split(' ', 1)[0]

	def set_price_bedroom(self, value):
		
		rent = 0 if len(self.get_attribute('monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('monthly_rent').replace(',','').replace(' ', ''))
		
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	
	