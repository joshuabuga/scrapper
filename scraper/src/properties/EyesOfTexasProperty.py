from BaseCompanyProperty import BaseCompanyProperty
class EyesOfTexasProperty(BaseCompanyProperty):
	def setup(self):
		self.forms ='Eyes Of Texas'
		self.deposit_paid_to = 'Campus and Central Properties | $75 App Fee/person, $75 Admin Fee'
		self.commission ='.3'
	def set_status(self, value):
		self.status = 'Leased'
	