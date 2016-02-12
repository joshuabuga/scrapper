from BaseCompanyProperty import BaseCompanyProperty
class AustinCentricProperty(BaseCompanyProperty):
	def setup(self):
		self.forms = 'TAR'
		self.deposit_paid_to = 'Austin Centric Realty | $50 App Fee, $50 Guarantor, $200 Admin Fee/Group, Deposit = 1 Month\'s Rent All Checks Payable to Austin Centric Realty'
	
	def set_status(self, value):
		self.status = 'Leased' if self.is_highlighted(None,'orange') or self.is_highlighted(None,'orange_four') and not self.is_highlighted(None,'white') else 'Active' 

	def set_title(self, value):
		self.title = self.get_attribute('address')  + ' ' + self.get_attribute('unit') 
	def set_price_bedroom(self, value):
		rent = 0 if len(self.get_attribute('monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('monthly_rent').replace(',','').replace(' ', '').replace('$',''))
		
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	
	def set_type(self,value):
		self.type= str(self.get_attribute('property_area').split('-',1)[0])
		if "house" in str(self.get_attribute('property_area')).replace(' ','').lower():
			self.type="House/Duplex"
		elif "duplex" in str(self.get_attribute('property_area')).replace(' ','').lower():
			self.type="House/Duplex"
	def set_area(self,value):
		self.area='NC/HP' if str(self.get_attribute('property_area').split('-',1)[1]).lower().replace(' ','')=='hydepark/nc' else ''

