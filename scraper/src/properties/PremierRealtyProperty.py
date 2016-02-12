from BaseCompanyProperty import BaseCompanyProperty
class PremierRealtyProperty(BaseCompanyProperty):
	def setup(self):
		self.forms = 'TAA + Addenda'
	def set_status(self,value):
		self.status='Leased' if self.is_highlighted() and not self.is_highlighted(None,'white') else 'Active'
	def set_unit(self,value):
		self.unit=str(self.get_attribute('premier_unit')).replace('.0','')
	def set_address(self,value):
		self.address=self.get_attribute('premier_address')

	
	def set_title(self, value):
		self.title = str(self.data['values']['premier_address'] + ' ' + self.get_attribute('premier_unit')).replace('.0','')
	def set_deposit_paid_to(self,value):
		string="Certified Funds Only, $50 App Fees, $50 Guarantor, $200 Admin Payable to Listing Agent. First full month's rent due at lease signing in one cashier's check/money order paid to"
		self.deposit_paid_to= string + '' + self.data['values']['deposit_paid_to'] + ' ' + self.get_attribute('admin_fee_payable_to')
	
