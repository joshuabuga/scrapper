from ..lib.helpers import *
class BaseCompany():
	"""docstring for BaseCompany"""
	name=''
	city=''
	state=''
	properties_data=[]
	company_properties=[]
	column_headers = { 'default': []}
	
	file_path = ''

	def __init__(self, file_path, property_fields):
		self.file_path = file_path
		self.property_fields  = property_fields
		self.setup()
		self.extract_data()
		self.set_properties()

	def setup(self):
		pass

	def get_file_path(self):
		return self.file_path

	def extract_data(self):
		return self.properties_data


	def set_properties(self):
		for property_data in self.properties_data:
			self.company_properties.append(self.new_property(property_data))
		
	def new_property(self, property_data):
		pass
	
	def set_col_headers(self, headers, key = 'default'):
		self.column_headers[key] = headers

	def get_col_headers(self, key = 'default', clean = True, tostr = False, delimiter = ',' ):
		key = key if self.column_headers.has_key(key) else 'default'
		headers = self.column_headers[key]
		return collection_to_str(headers , delimiter, 1, clean) if tostr else tuple_to_str_list( headers, 1, clean)
	
	def get_col_header_fields(self, key = 'default', clean = True, tostr = False, delimiter = ','):
		key = key if self.column_headers.has_key(key) else 'default'
		fields = self.column_headers[key]
		return collection_to_str( fields, delimiter, 0, clean ) if tostr else tuple_to_str_list( fields, 0, clean)

	def to_list(self):
		property_list = []
		for property_ in self.company_properties:
			property_list.append(property_.to_list())

		return property_list
