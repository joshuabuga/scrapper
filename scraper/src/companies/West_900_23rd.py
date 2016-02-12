from ..properties.West_900_23rdProperty import West_900_23rdProperty
from BaseCompanyExcel import BaseCompanyExcel
from ..lib.helpers import *
class West_900_23rd(BaseCompanyExcel):
	name ='900 W 23rd'
	city ='Austin'
	state ='TX'
	def setup(self):
		self.set_col_headers( [
							('floor_plan', 'UNIT/FLOORPLAN'),
							('monthly_rent', 'rent'),
							('west_status', 'status') ,
							('tenant_phone', '') 
							
							], 'default')

		self.set_exempted_rows( [

							'SCHOOL YEAR',
							'MOVE IN DATE',
							'------------'
							], 'default', 1000)

	def new_property(self, property_data):
		prop = West_900_23rdProperty(property_data, self)	
		return prop

	def get_phone(self, row_values):
		last_col = len(row_values) - 1
		phone = row_values[last_col]
		if no_space_lower(phone) == no_space_lower( collection_to_str(row_values, '') ):
			return phone
		return False


	def get_row_data(self, sheet, row, cols = None):
		row_data = self.read_row_data(sheet,row,cols)
		phones = self.get_phone(row_data['values'])
		if phones != False:
			row_data['empty_cells'] += 1
			return row_data
		phones = row_data['values'][len(row_data['values']) - 1] 
		has_phone = True
		row = row + 1
		while has_phone:
			if row >= sheet.nrows:
				has_phone = False
				break
			next_row = self.read_row_data(sheet, row, cols)['values']
			phone = self.get_phone(next_row)
			if phone != False:
				phones = phones + ', ' + phone
			else:
				has_phone = False
			row = row + 1

		row_data['values'][len(row_data['values']) - 1] = phones
		return row_data