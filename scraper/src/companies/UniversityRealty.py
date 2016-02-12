from ..properties.UniversityRealtyProperty import UniversityRealtyProperty
from BaseCompanyExcel import BaseCompanyExcel
class UniversityRealty(BaseCompanyExcel):
	name ='University Realty'
	city ='Austin'
	state ='TX'

	def setup(self):
		self.set_col_headers( [
							('university_zip_code', 'zip'),
							('property', 'property'), 
							('address', ''), 
							('university_unit', ''), 
							('monthly_rent', ''),
							('size', ''), 
							('tenant_phone', ''),
							('available', ''),
							('end'       , ''),
							('description', ''),
						    ], 'default')
		# self.set_exempted_rows( [
		# 					'Houses / Multiplex',
		# 					'Rooms Rooms' ,
		# 					'Efficiencies Effs',
		# 					'1 Bedrooms 1 Bd',
		# 					'1 Bedroom 1-Bd',
		# 					'2 bedroom 2-Bd',
		# 					'Condos/Apts',
		# 					'Condos/Apts 2 Bd',
		# 					'3 Bedroom 3Bd',
		# 					'3 Bedroom 3-Bds',
		# 					'3 Bedroom 3-Bd',
		# 					'4-7 Bedroom 4-7 Bds'
		# 					], 'default', 5)
	

	def new_property(self, property_data):
		prop =UniversityRealtyProperty(property_data, self)	
		return prop
