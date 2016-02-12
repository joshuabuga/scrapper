from BaseCompanyProperty import BaseCompanyProperty
import re
class ElyProperty(BaseCompanyProperty):
	def setup(self):
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = 'Ely Properties  | $100/Applicant, Deposit = 1 Month\'s Rent'
		self.commission=.4
	
	
	def set_status(self, value):
		self.status = 'Leased' if "pending" in str(self.get_attribute('description')).lower() or "leased" in  str(self.get_attribute('description')).lower()  else 'Active'

	def set_title(self, value):
		self.title = str(self.data['values']['name'] + ' ' + self.get_attribute('unit')).replace('.0','').replace('-','')
	def set_bedroom(self, value):
		self.bedroom = self.data['values']['size'].split('x', 1 )[0] if 'x' in self.data['values']['size'] else self.data['values']['size']
		if str(self.data['values']['size']).lower()=='studio':
			self.bedroom=0
	def set_bathroom(self, value):
		self.bathroom = self.data['values']['size'].split('x', 1 )[1] if 'x' in self.data['values']['size'] else self.data['values']['size']
		if str(self.data['values']['size']).lower()=='studio':
			self.bathroom=1
	def set_price_bedroom(self, value):
		try:
			rent = 0 if len(self.get_attribute('monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('monthly_rent').replace(',','').replace(' ', ''))
		except:
			rent=0
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	


	
	