from BaseCompanyProperty import BaseCompanyProperty
from ..companies.BaseCompanyExcel import BaseCompanyExcel
class MetroProperty(BaseCompanyProperty):
	def setup(self):
		self.commission = '.4'
		self.bonus = ''
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = 'Metro Realty | $100 App Fees, Deposit = 1st Month\'s Rent'
		
	def set_status(self,value):
		self.status='Leased' if str(self.get_attribute('leased')).strip()=='yes' else 'Active'
	def set_monthly_rent(self,value):
		self.monthly_rent=str(self.data['values']['metro_monthly_rent'])
	def set_title(self, value):
		self.title = str(self.data['values']['property_name'] + ' ' + self.get_attribute('unit')).replace('.0','') if self.data['values']['property_name'] !='' else str(self.data['values']['address'] + ' ' + self.get_attribute('unit')).replace('.0','')

	def set_bedroom(self, value):
		self.bedroom = self.data['values']['size'].split('-', 1 )[0]

	def set_bathroom(self, value):
		size = self.data['values']['size'].split('-', 1)
		self.bathroom = size[1] if len(size) > 1 else '0'

	def set_price_bedroom(self, value):
		try:
			rent = 0 if len(self.get_attribute('metro_monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('metro_monthly_rent').replace(',','').replace(' ', ''))
		
		except:
			rent=0
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	

