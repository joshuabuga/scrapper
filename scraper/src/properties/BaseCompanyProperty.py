import inspect
from ..lib.color_helpers import *
class BaseCompanyProperty():
	"""docstring for CompanyProperty"""
		
	def __init__(self, data, company):
	
		self.company_obj = company
		self.property_fields = self.company_obj.property_fields
		self.data = data
		self.setup()
		self.set_company_attributes()
		self.set_attributes()
		
	def setup(self):
		pass
		
	def set_attributes(self):
		for attribute in self.property_fields:
			if not hasattr(self, attribute):
				self.set_attribute(attribute)
	
	def set_attribute(self, attribute, value = "" ):

		value = value if not attribute in self.data['values'] else self.data['values'][attribute]
		if hasattr(self, 'set_' + attribute) and inspect.ismethod(getattr(self, 'set_' + attribute)):
			getattr(self, 'set_' + attribute)(value)
		else:
			self.__dict__[attribute] = value
	
	def get_attribute(self, attribute):
		if not hasattr(self, attribute):
			self.set_attribute(attribute)
		return getattr(self, attribute)

	def set_company_attributes(self):
		self.company = self.company_obj.name
		self.city = self.company_obj.city
		self.state = self.company_obj.state

	def to_list(self):
		data_list= []
		for attribute in self.property_fields:
			data_list.append(self.__dict__[attribute])

		return data_list
	
	def is_highlighted(self, attributes = None, color = None):
		attributes = self.data['meta'].keys() if attributes == None else [attributes]	
		highlighted = 0
		for attribute in attributes:
			color_name = get_color_name(self.data['meta'][attribute]['bg_color']['rgb'])
			
			if color_name != None:
				
				highlighted += 1 if color == None or color != None and color == color_name else 0

		
		return True if highlighted == len(attributes) else False

				
	def get_exempted_rows(self, key = 'default'):
		return self.exempted_rows[key] if self.exempted_rows.has_key(key) else self.exempted_rows['default']

	def set_exempted_rows(self, rows,  key = 'default', tolerate = 0 ):
		self.exempted_rows[key] = { 'rows' : rows, 'tolerate' : tolerate }

			
