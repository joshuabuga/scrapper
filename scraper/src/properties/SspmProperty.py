from BaseCompanyProperty import BaseCompanyProperty
class SspmProperty(BaseCompanyProperty):
	def setup(self):
		self.commission='50%'
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = 'State Street Property Management | $50 App Fee to State Street Property Management | Deposit = 1 Month\'s Rent to State Street Property Management'
	

	def set_title(self, value):
		self.title = self.get_attribute('address') + ' ' + str(self.get_attribute('unit')).replace('.0','')
	def set_status(self,value):
		self.status = 'Leased' if self.is_highlighted() and not self.is_highlighted(None,'white') else 'Active'
