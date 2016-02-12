from properties.ColorProperty import ColorProperty
from BaseCompanyExcel import BaseCompanyExcel
class Color(BaseCompanyExcel):
	name =''
	city =''
	state =''
	
	def setup(self):
		self.set_col_headers( [
							('status', 'status')
							  
							], 'default')

	def new_property(self, property_data):
		prop = ColorProperty(property_data, self)	
		return prop

	#def get_row_data(self, sheet, row, cols = None):
		


u=Color('color.xls')
u.print_csv()



