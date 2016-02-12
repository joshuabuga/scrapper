from BaseCompanyProperty import BaseCompanyProperty
class ColorProperty(BaseCompanyProperty):

	def set_status(self, value):
		self.status = "ACTIVE" if self.is_highlighted() else "LEASED"
