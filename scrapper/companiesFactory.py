from  scraper.Master import Master

class companiesFactory(object):
	master = None
	companies = {}
	def __init__(self):
		self.set_companies()
		self.master = Master({})

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


				'metro'					: { 
				 				'class'			: 'Metro'
				 				 
				 					},

				'campus-condos'			: { 
								'class'			: 'CampusCondos' 	
								
								},

				'austin-centric'			: { 
				 				'class'			: 'AustinCentric'
				 				 
				 					},

				 'realty-pros'				: { 
				 				'class'			: 'RealtyPros'	
				 				
				 				},

				 'uptown'					: { 
				  				'class'			: 'UptownExcel'	
				  				
				  				},

				'chays-list'				: { 
								'class'			: 'ChaysList' 	
				 				
								},

				'acr'						: { 
								'class'			: 'Acr', 	
								
								},

				'premier-realty'			: { 
				 				'class'			: 'PremierRealty'	
				 				
				 				},

				  'tower-realty'			: { 
				  				'class'			: 'TowerRealty'	
				  				
				  				},

				 # 'kline-properties'		: { 
				 # 				'class'			: '', 	
				 # 				'file'		 	: ''
				 # 				},

				'ely'						: { 
								'class'			: 'Ely' 	
				 				
								},

				 'campus-central'			: { 
				 				'class'			: 'CampusCentral' 	
				 				
				 				},

				 '21-pearl-lee-properties'	: { 
				 				'class'			: 'PearlLee', 	
				 				
				 				},

				 'university-realty'		: { 
				 				'class'			: 'UniversityRealty'	
				 				
				 				},

				 'west-campus-living'		: { 
				 				'class'			: 'WestCampusLiving' 	
				 				
				 				},

				  'master-list'		: { 
			 				'class'			: 'MasterList' 	
			 				
			 				},


				 '900-west-23rd'			: { 
				 				'class'			: 'West_900_23rd'	
				 				
				 				},

				 'lee-properties'			: { 
				 				'class'			: 'LeeProperties', 	
				 				
				 				},

				 '512-realty'				: { 
				 				'class'			: 'Realty512' 	
				 				
				 				},
				 'consolidated-list'				: { 
				 				'class'			: 'ConsolidatedList' 	
				 				
				 				},
				 'sspm'				: { 
				 				'class'			: 'Sspm' 	
				 				
				 				}

					}

