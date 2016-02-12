from scraper.Master import Master
def go():
	


	companies = {


				'metro'					: { 
				 				'class'			: 'Metro',
				 				'file'  		: 'Metro Realty--4-8-14.xls' 
				 					},

				'campus-condos'			: { 
								'class'			: 'CampusCondos', 	
								'file'		 	: 'Campus Condos - 11-5-14.xls'
								},

				'austin-centric'			: { 
				 				'class'			: 'AustinCentric',
				 				'file'  		: 'Austin Centric- Pre Lease List- 10.24.2014.xls' 
				 					},

				 'realty-pros'				: { 
				 				'class'			: 'RealtyPros', 	
				 				'file'		 	: '2015-16 Realty Pros Pre-Lease List.xls'
				 				},

				 'uptown'					: { 
				  				'class'			: 'UptownExcel', 	
				  				'file'		 	: 'Uptown Pre-Lease List 14-15.xls'
				  				},

				'chays-list'				: { 
								'class'			: 'ChaysList', 	
				 				'file'		 	: 'Chay\'s List 4_29_14.xls'
								},

				'acr'						: { 
								'class'			: 'Acr', 	
								'file'		 	: 'ACR Pre Lease List.xls'
								},

				'premier-realty'			: { 
				 				'class'			: 'PremierRealty', 	
				 				'file'		 	: 'Premier Realty - 11-5-14.xls'
				 				},

				  # 'tower-realty'			: { 
				  # 				'class'			: 'TowerRealty', 	
				  # 				'file'		 	: 'Tower Realty Availability List Office 2015-2016.xls'
				  # 				},

				 # 'kline-properties'		: { 
				 # 				'class'			: '', 	
				 # 				'file'		 	: ''
				 # 				},

				'ely'						: { 
								'class'			: 'Ely', 	
				 				'file'		 	: 'Ely Properties Availability 2015-16.xls'
								},

				 'campus-central'			: { 
				 				'class'			: 'CampusCentral', 	
				 				'file'		 	: 'Campus & Central Properties Availability .xls'
				 				},

				 '21-pearl-lee-properties'	: { 
				 				'class'			: 'PearlLee', 	
				 				'file'		 	: '21 Pearl 14-15 Availability List.xls'
				 				},

				 'university-realty'		: { 
				 				'class'			: 'UniversityRealty', 	
				 				'file'		 	: 'University Realty - 11-5-14.xls'
				 				},

				 'west-campus-living'		: { 
				 				'class'			: 'WestCampusLiving', 	
				 				'file'		 	: '2014 Buckingham Availability.xls'
				 				},

				  'master-list'		: { 
			 				'class'			: 'MasterList', 	
			 				'file'		 	: 'Master_List.xls'
			 				},


				 '900-west-23rd'			: { 
				 				'class'			: 'West_900_23rd', 	
				 				'file'		 	: '900 W 23rd--3-6-14.xls'
				 				},

				 'lee-properties'			: { 
				 				'class'			: 'LeeProperties', 	
				 				'file'		 	: '-24th Street Realty & Lee Properties Pre-lease and Current list 15-16-.xls'
				 				},

				 '512-realty'				: { 
				 				'class'			: 'Realty512', 	
				 				'file'		 	: '512 Realty Preleasing List 10.29.14 (2).xls'
				 				}

					}


	master = Master(companies)
	master.extract_properties(['campus-central'])
	master.write_master_list(['campus-central'])
	master.extract_properties(['university-realty'])
	master.write_master_list(['university-realty'])
	master.extract_properties(['west-campus-living'])
	master.write_master_list(['west-campus-living'])
	master.extract_properties(['900-west-23rd'])
	master.write_master_list(['900-west-23rd'])
	master.extract_properties(['lee-properties'])
	master.write_master_list(['lee-properties'])
	master.extract_properties(['chays-list'])
	master.write_master_list(['chays-list'])

	master.extract_properties(['campus-condos'])
	master.write_master_list(['campus-condos'])
	master.extract_properties(['ely'])
	master.write_master_list(['ely'])
	master.extract_properties(['metro'])
	master.write_master_list(['metro'])

	master.extract_properties(['austin-centric'])
	master.write_master_list(['austin-centric'])
	master.extract_properties(['512-realty'])
	master.write_master_list(['512-realty'])

	master.extract_properties(['acr'])
	master.write_master_list(['acr'])
	master.extract_properties(['21-pearl-lee-properties'])
	master.write_master_list(['21-pearl-lee-properties'])

	master.extract_properties(['premier-realty'])
	master.write_master_list(['premier-realty'])
	master.extract_properties(['uptown'])
	master.write_master_list(['uptown'])
	master.extract_properties(['master-list'])
	master.write_master_list(['master-list'])





