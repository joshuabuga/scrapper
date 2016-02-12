from  scraper.Master_one import MasterOne

class companiesFactoryOne(object):
	master = None
	companies = {}
	def __init__(self):
		self.set_companies()
		self.master = MasterOne({})

	def all(self):
		return self.companies

	def set_file(self, company, fileName):
		self.companies[company]['file'] = fileName
		self.master.add_company(company, self.companies[company])
		return self.companies[company]

	def save_company_data(self, company):
		self.master.extract_properties([company])
		self.master.write_master_list([company])
		
	def set_companies(self):
		self.companies = {
				
				 'master-list'				: { 
								
				 				'class'			: 'MasterList' 	
				 				
				 				}

					}
