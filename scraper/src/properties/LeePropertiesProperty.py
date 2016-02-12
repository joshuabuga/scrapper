from BaseCompanyProperty import BaseCompanyProperty
class LeePropertiesProperty(BaseCompanyProperty):
	def setup(self):
		self.forms ='TAR + ADDENDA'
		self.deposit_paid_to = 'Lee Properties | $100 App Fees, $100 Admin Fee ($200 Cap), Deposit = 1 Month\'s Rent | Rental Increase for Double Occupancy'
	
	
	def set_status(self, value):
		self.status = 'Leased' if self.is_highlighted() and not self.is_highlighted(None,'white') else 'Active'

	def set_bedroom(self,value):
		self.bedroom ='' if len(str(self.data['values']['size']))==0 else self.data['values']['size'].split('/',1)[0]
	def set_unit(self,value):
		self.unit='' if len(str(self.data['values']['title']))==0 else self.data['values']['title'].split()[0]
	def set_bathroom(self,value):
		self.bathroom='' if len(str(self.data['values']['size']))==0 else self.data['values']['size'].split('/',1)[0]
	def set_address(self,value):
		self.address='' if len(str(self.data['values']['title']))== 0 else str(self.data['values']['title']).replace(str(self.data['values']['title']).split()[0],'')