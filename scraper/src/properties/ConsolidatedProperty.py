from BaseCompanyProperty import BaseCompanyProperty
class ConsolidatedProperty(BaseCompanyProperty):
	def setup(self):
		pass

	def set_company_attributes(self):
		self.company = self.get_attribute('company_name')
		self.city = self.company_obj.city
		self.state = self.company_obj.state
