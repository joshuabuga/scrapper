import importlib
import csv
import json
import os,sys
import psycopg2
import unicodedata
from scrapper.settings import *
sys.path.insert(0, '/var/www/scrapper/scrapper/scrapper')
sys.path.append( MEDIA_ROOT +'/')



class  Master(object):
	companies = {}
	class_key = 'class'
	file_key = 'file'
	instance_key = 'instance'
	properties_key = 'properties'
	companies_sub_pkg = 'scraper.src.companies'

	files_dir = MEDIA_ROOT + '/'
	output_file = 'Master_List.csv'
	property_fields = [
	    'external_id',
		'status',
		'company',
		'm',
		'title',
		'address',
		'unit',
		'city',
		'state',
		'zip_code',
		'square_feet',
		'forms',
		'parking_space',
		'area',
		'type',
		'bedroom',
		'bathroom',
		'monthly_rent',
		'price_bedroom',
		'available',
		'paid_utilities',
		'pets',
		'pets_info',
		'laundry',
		'web_description',
		'tenant_phone',
		'gate_code',
		'key_number',
		'email',
		'commission',
		'bonus',
		'deposit_paid_to',
		'description',
		'double_occupancy',
		'dbl_occ_info',
		'listing_type',
		'pool',
		

		]

	output_field_headers = {
		'external_id'				: 'External ID',
		'status' 					: 'Status',
		'company'					: 'Company',
		'm'							: 'M',
		'title'						: 'Title',
		'address'					: 'Address',
		'unit'						: 'Unit',
		'city'						: 'City',
		'state'						: 'State',
		'zip_code'					: 'Zip',
		'square_feet'				: 'Square Feet',
		'forms'						: 'Forms',
		'parking_space'			    : 'Parking Space',
		'area'						: 'Area',
		'type'						: 'Type',
		'bedroom'					: 'Bedroom',
		'bathroom'					: 'Bathroom',
		'monthly_rent'				:'Monthly Rent',
		'price_bedroom'				: 'Price per Bedroom',
		'available'					: 'Available',
		'paid_utilities'			: 'Paid Utilities',
		'pets'						: 'Pets',
		'pets_info'					: 'Pets Info',
		'laundry'					: 'Laundry',
		'web_description'			: 'Web Description',
		'tenant_phone'				: 'Phone',
		'gate_code'					: 'Gate Code',
		'key_number'				: 'Key Number',
		'email'						: 'Email',
		'commission'				: 'Commission',
		'bonus'						: 'Bonus',
		'deposit_paid_to'			: 'Deposit and 1st Month\'s Rent Paid To',
		'description'				: 'Description',
		'double_occupancy'			: 'Double Occupancy',
		'dbl_occ_info'				: 'Dbl Occ Info',
		'listing_type'				: 'Listing Type',
		'pool'						: 'Pool'


		}
	
	def __init__(self, companies = {}):
		self.companies = companies

	def add_company(self, company, data):
		self.companies[company] = data

	def get_module(self, company):
		class_name = self.get_company_item(company, self.class_key)
		return self.companies_sub_pkg + '.' + class_name if class_name != None else self.companies_sub_pkg

	def company_exists(self,company):
		return True if self.companies.has_key(company) else False


	def get_company_dict(self, company):
		return self.companies[company] if self.company_exists(company) else None
	
	def get_company_item(self, company, item = None ):
		company_dict = self.get_company_dict(company)
		if item == None:
			return company_dict
		return company_dict[item] if  company_dict != None and company_dict.has_key(item) else None

	def set_company_item(self, company, item, value):
		self.companies[company][item] = value

	def company_file_path(self, company):
		company_file = self.get_company_item(company, self.file_key)
		if isinstance(company_file, unicode):
			company_file = unicodedata.normalize('NFKD', company_file).encode('ascii','ignore')
		company_file = str(company_file)
		return self.files_dir + company_file if company_file != None else None

	def get_instance(self, company):
		instance = self.get_company_item(company, self.instance_key)
		if instance != None:
			return instance
		return self.new_company_instance(company)


	def new_company_instance(self, company):
		if self.company_exists(company):
			module_ = importlib.import_module( self.get_module( company ) )
		
			class_ = getattr(module_, self.get_company_item(company, self.class_key))
			new_instance = class_( self.company_file_path(company), self.property_fields )
			self.companies[company][self.instance_key] = new_instance
			return new_instance
		return None

	def extract_properties(self, companies = None):
		companies = companies if isinstance( companies, list ) else self.companies.keys()
		for company in companies:
			self.extract_company_propeties(company)
			

	def get_company_propeties(self, company):
		properties = self.get_company_item(company, self.properties_key)
		if properties != None:
			return properties

		return self.extract_company_propeties(company)

	def extract_company_propeties(self, company):
		instance = self.get_instance( company )
		if instance != None:
			properties = instance.to_list()
			
			self.set_company_item(company, self.properties_key, properties)
			return properties
		return []

	def get_master_list_headers(self):
		headers = []
		for header in self.property_fields:
			headers.append(self.output_field_headers[header])

		return headers


	def write_master_list(self, companies = None):
		companies = companies if isinstance( companies, list ) else self.companies.keys()
		with open(self.output_file, 'wb') as f:
			writer = csv.writer(f)
			writer.writerow(self.get_master_list_headers())

			for company in companies:
				company_instance = self.get_instance(company)


			properties = company_instance.to_list()
			for property_ in properties:
				writer.writerow(property_)
		# Open database connection
		conn = psycopg2.connect(database="uptown_properties", user="postgres", password="scrapper!scrapper", host="localhost", port="5433")
		
			# prepare a cursor object using cursor() method
		cursor = conn.cursor()
		status_tempo='Leased'
		company_tempo=str(property_[2]).strip()
		cursor.execute("UPDATE master_csv SET status=%s WHERE company=%s",(status_tempo,company_tempo,))
		
		for property_ in properties:
			status=str(property_[1]).strip()
			company=str(property_[2]).strip()			
			m=property_[3]
			title=str(property_[4]).strip()
			address=str(property_[5]).strip()
			unit=str(property_[6]).strip().replace('.0','')
			city=str(property_[7]).strip()
			state=str(property_[8]).strip()
			zip_code=property_[9]
			square_feet=property_[10]
			form=property_[11]
			parking_space=property_[12]
			area=property_[13]
			types=property_[14]
			bedroom=str(property_[15]).strip().replace('.0','')
			bathroom=str(property_[16]).strip().replace('.0','')
			monthly_rent=str(property_[17]).strip().replace('.0','')
			price_bedroom=str(property_[18]).strip().replace('.0','')
			available=property_[19]
			paid_utilities=property_[20]
			pets=property_[21]
			pets_info=property_[22]
			laundry=property_[23]
			web_description=property_[24]
			tenant_phone=property_[25]
			gate_code=property_[26]
			key_number=property_[27]
			email=property_[28]
			commission=property_[29]
			bonus=property_[30]
			deposit_paid_to=property_[31]
			description=property_[32]
			double_occupancy=property_[33]
			dbl_occ_info=property_[34]
			listing_type=property_[35]
			pool=property_[36]
			
			
			if company=='ACR':
				cursor.execute("SELECT * FROM master_csv WHERE company=%s AND address=%s AND unit=%s AND title=%s AND bedroom=%s\
					AND bathroom=%s",
				           (company,address,unit,title,bedroom,bathroom,))
			 	exist=cursor.fetchone()
				if exist:
					cursor.execute("UPDATE master_csv SET status=%s WHERE company=%s AND title=%s AND address=%s AND unit=%s \
					 AND price_bedroom=%s AND bedroom=%s AND bathroom=%s",
				           (status,company,title,address,unit,price_bedroom,bedroom,bathroom,))
		
				else:

					cursor.execute('INSERT INTO master_csv\
											(status,company, m, title,\
											address,unit,city,state,zip_code,\
											square_feet,forms,parking_space,area,type,\
									        bedroom,bathroom,monthly_rent,price_bedroom,available,\
									        paid_utilities,pets,pets_info,laundry,web_description,tenant_phone,gate_code,\
									        key_number,email,commission,bonus,deposit_paid_to,\
									        description) \
									       VALUES \
									       (%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s)',(status,company, m, title,\
											address,unit,city,state,zip_code,\
											square_feet,form,parking_space,area,types,\
									        bedroom,bathroom,monthly_rent,price_bedroom,available,\
									        paid_utilities,pets,pets_info,laundry,web_description,tenant_phone,gate_code,\
									        key_number,email,commission,bonus,deposit_paid_to,\
									        description))
		
			else:
		# Prepare SQL query to INSERT a record into the database.
				cursor.execute("SELECT * FROM master_csv WHERE company=%s AND address=%s AND unit=%s AND title=%s",
					           (company.strip(),address.strip(),unit.strip().replace('.0',''),title.strip(),))
				exist=cursor.fetchone()
				if exist:
					cursor.execute("UPDATE master_csv SET status=%s,monthly_rent=%s,price_bedroom=%s,commission=%s,\
					bonus=%s,tenant_phone=%s,email=%s,paid_utilities=%s \
					 WHERE company=%s AND title=%s AND address=%s AND unit=%s",
					           (status.strip(),monthly_rent,price_bedroom,commission,bonus,tenant_phone,email,paid_utilities,company.strip(),title.strip(),address.strip(),unit.strip().replace('.0',''),))
			
				else:

					cursor.execute('INSERT INTO master_csv\
											(status,company, m, title,\
											address,unit,city,state,zip_code,\
											square_feet,forms,parking_space,area,type,\
									        bedroom,bathroom,monthly_rent,price_bedroom,available,\
									        paid_utilities,pets,pets_info,laundry,web_description,tenant_phone,gate_code,\
									        key_number,email,commission,bonus,deposit_paid_to,\
									        description,double_occupancy,dbl_occ_info,listing_type,pool) \
									       VALUES \
									       (%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,\
									        %s,%s,%s,%s,%s,%s,%s)',(status,company, m, title,\
											address,unit,city,state,zip_code,\
											square_feet,form,parking_space,area,types,\
									        bedroom,bathroom,monthly_rent,price_bedroom,available,\
									        paid_utilities,pets,pets_info,laundry,web_description,tenant_phone,gate_code,\
									        key_number,email,commission,bonus,deposit_paid_to,\
									        description,double_occupancy,dbl_occ_info,listing_type,pool))
					




		cursor.execute("DELETE FROM master_csv\
			            WHERE title='' AND address='' AND monthly_rent=''")
		cursor.execute("DELETE FROM master_csv\
			            WHERE address='' AND unit=''")
		cursor.execute("DELETE FROM master_csv\
			            WHERE title='Complex' AND address='Address:'")
		cursor.execute("DELETE FROM master_csv\
			            WHERE company='Ely' AND address='Address'AND unit='Unit'")
		cursor.execute("DELETE FROM master_csv\
			            WHERE company='CampusCondos' AND address='Address'")

	
		
	
		
	
	
	



			

			
	
		   
		   # Commit your changes in the database
		conn.commit()
		
		# disconnect from server
		conn.set_isolation_level(0)
		cursor.execute("VACUUM FULL");
		conn.close()
		os.system('apache2 restart')

	
