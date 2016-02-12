from BaseCompanyProperty import BaseCompanyProperty
class RealtyProsProperty(BaseCompanyProperty):
	def setup(self):
		self.commission = '.4'
		self.deposit_paid_to = 'Realty Pros | $75/person App Fees paid to Realty Pros of Austin, Deposit = 1 Month\'s Rent paid to Austin Manage, LLC'
		
	def set_status(self, value):
		self.status = 'Leased' if self.is_highlighted() and not self.is_highlighted(None,'white') else 'Active'

	def set_unique_master_id(self, value):
		self.unique_master_id = self.get_attribute('company') + ' ' + self.get_attribute('address') + ' ' + self.get_attribute('unit')

	def set_title(self, value):
		self.title = self.data['values']['property'] + ' ' + self.get_attribute('unit')
	def set_monthly_rent(self,value):
		try:
			self.monthly_rent=str(self.data['values']['pros_monthly_rent'])
		except:
			self.monthly_rent=0

	def set_price_bedroom(self, value):
		try:
			rent = 0 if len(self.get_attribute('pros_monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('pros_monthly_rent').replace(',','').replace(' ', ''))
		
		except:
			rent=0
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	