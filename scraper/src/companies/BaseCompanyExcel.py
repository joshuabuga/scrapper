from __future__ import with_statement
from xlrd import *
import xlrd
import datetime 
import unicodedata
from ..lib.helpers import *
from BaseCompany import BaseCompany


class BaseCompanyExcel(BaseCompany):
	"""docstring for BaseCompanyCsv"""
	
	workbook = None 
	current_sheet = None
	exempted_rows = { 'default' : { 'tolerate' : 0, 'rows' : [] } }

	def extract_data(self):
		
		data_list=[]
		self.open_workbook()
		sheets = self.workbook.sheet_names()
		for index, sh in enumerate(sheets):
			self.current_sheet = index
			sheet = self.workbook.sheet_by_index(index)
			if not self.sheet_is_empty(sheet):
				header_row = self.get_header_row(sheet)
				print header_row
	
				
				if type(header_row) == int:
					for row in range(header_row + 1, sheet.nrows):
						row_data = self.get_row_data(sheet, row, self.sheet_ncols(sheet))
						
						if row_data and not self.row_is_empty(row_data, self.sheet_ncols(sheet)) and not self.should_exempt_row(row_data):
							data_list.append({'meta': self.set_property_values(row_data['meta']), 'values': self.set_property_values(row_data['values'])})
							
						
				
		self.properties_data=data_list
	

		
		return self.properties_data

	def set_property_values(self, values):
		values_dict = {}
		index = 0
		for field in self.get_col_header_fields(self.current_sheet, False):
			values_dict[field] = values[index]
			index+=1

		return values_dict

	def open_workbook(self):
		
		self.workbook = open_workbook(self.get_file_path(), formatting_info = True)
		

	def read_sheet_data(self, sheet):
		for row in range(s.nrows):
			values = []
			for col in range(s.ncols):
				values.append(s.cell(row,col).value)

	def sheet_is_empty(self, sheet):
		empty_rows = 0
		cols = self.sheet_ncols(sheet)
		for row in range(sheet.nrows):
			row_data = self.read_row_data(sheet, row, cols )
			empty_rows += 1 if  self.row_is_empty(row_data, cols) else 0
		
		return True if empty_rows == sheet.nrows  else False


	def get_row_data(self, sheet, row, cols = None):
		return self.read_row_data(sheet,row,cols)

	def sheet_ncols(self, sheet, sheet_index = None):
		sheet_index = sheet_index if sheet_index else self.current_sheet

		fields_len = len(self.get_col_header_fields(sheet_index, False))
		return fields_len #if fields_len <= sheet.ncols else sheet.ncols

	def row_is_empty(self, row_data, cols ):
		return True if row_data['empty_cells'] >= cols else False

	def should_exempt_row(self, row_data):
		str_values = collection_to_str(row_data['values'], '')
		exempted_rows = self.get_exempted_rows(self.current_sheet)
		for row in exempted_rows['rows']:
			search_row = no_space_lower(row)
			search_str_vals = no_space_lower(str_values)
			tolerate = len(search_str_vals) - len(search_row)
			if search_row in search_str_vals and tolerate <= exempted_rows['tolerate']:
				return True 
			
		return False

	def read_row_data(self, sheet, row, cols = None):
		values = []
		meta = []
		cols = cols if cols and cols <= sheet.ncols else sheet.ncols
		empty_cells = cols
		for col in range(cols):
			cell =  sheet.cell(row, col)
			cellvalue = self.get_cell_value(cell)
			if cellvalue != None:
				values.append(cellvalue)
				empty_cells -= 1
			else:
				values.append('')
				
			meta.append(self.get_cell_meta(cell))



		return { 'values' : values, 'meta': meta, 'empty_cells' : empty_cells  }
	
	def get_cell_value(self, cell):
		if cell.ctype == xlrd.XL_CELL_DATE:
			try:
				datetuple = xlrd.xldate_as_tuple(cell.value, self.workbook.datemode)
				if datetuple[3:] == (0, 0, 0):
					return str(datetuple[0]) + '/' + str(datetuple[1]) + '/' + str(datetuple[2])

				return str(datetuple[0]) + '/' + str(datetuple[1]) + '/' + str(datetuple[2]) + '/' + str(datetuple[3]) + '/' + str(datetuple[4]) + '/' + str(datetuple[5])

			except:
				pass

		if cell.ctype == xlrd.XL_CELL_EMPTY or cell.ctype == xlrd.XL_CELL_BLANK:
			return None

		value = cell.value
		if isinstance(value, unicode):
			value = unicodedata.normalize('NFKD', value).encode('ascii','ignore')
		value = str(value).strip() if len(str(value).strip()) > 0 else None
		return value



	def get_cell_meta(self, cell):
		xf = self.workbook.xf_list[cell.xf_index]
		bgx = xf.background.pattern_colour_index
		rgb = self.workbook.colour_map[bgx]
		# f=open('C:\Users\Josh\Desktop\scrapper\out.txt','a')
		# f.write(str(rgb))
		# f.close()
		return {'bg_color': { 'index' : bgx, 'rgb' : rgb }}


	def get_header_row(self, sheet):
		matched_cols = 0
		for row in range(sheet.nrows):
			matched_cols = 0
			row_data = self.read_row_data(sheet, row, self.sheet_ncols(sheet))
			
			index = 0
			col_headers = self.get_col_headers(self.current_sheet, True)
			
			for cell_value in col_headers:
				if row_data['values'][index] and row_data['values'][index].lower() == cell_value.lower():
					matched_cols +=1
				elif len(cell_value) > 0 and len(cell_value.replace(' ', '')) == 0:
					matched_cols +=1
				index+=1
			if matched_cols == len(col_headers):
				return row
		return False

	def get_exempted_rows(self, key = 'default'):
		return self.exempted_rows[key] if self.exempted_rows.has_key(key) else self.exempted_rows['default']

	def set_exempted_rows(self, rows,  key = 'default', tolerate = 0 ):
		self.exempted_rows[key] = { 'rows' : rows, 'tolerate' : tolerate }
