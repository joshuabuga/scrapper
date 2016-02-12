from BaseCompanyProperty import BaseCompanyProperty
class AcrProperty(BaseCompanyProperty):
	def setup(self):
		self.commission = '.3'
		self.bonus = ''
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = 'ACR | Deposit = 1 Month\'s Rent, App Fee $100/Applicant, Admin Fee = $100/Property'
	
	
	def set_status(self, value):
		self.status = 'Leased' if self.is_highlighted(None,'green') or  self.is_highlighted(None,'red')   else 'Active'

	def set_title(self, value):
		self.title = str(self.data['values']['property_name'])
	def set_area(self,value):

		if str(self.data['values']['acr_area']).lower().replace(' ','')=='westcampus':
			self.area='WC'

		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='tarrytown':
			self.area='EF/TT'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='tt/ef':
			self.area='EF/TT'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='hp/nc':
			self.area='NC/HP'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='northcampus':
			self.area='NC/HP'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='northcampus/hydepark':
			self.area='NC/HP'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='th/soco':
			self.area='SOCO/TH'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='rs':
			self.area='Riverside/East Oltorf'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='south':
			self.area='S'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='southaustin':
			self.area='S'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='eastaustin':
			self.area='EC'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='abr/fw':
			self.area='ABR/FW'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='central':
			self.area='NC/HP'
		elif str(self.data['values']['acr_area']).lower().replace(' ','')=='nc':
			self.area='NC/HP'
		else:
			self.area =str(self.data['values']['acr_area'])
	def set_type(self,value):
		self.type =str(self.data['values']['acr_type'])
		if str(self.data['values']['acr_type']).lower().replace(' ','')=='a':
			self.type='Apartment'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='c':
			self.type='Condo'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='condo/apartments':
			self.type='Condo'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='d':
			self.type='House/Duplex'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='f':
			self.type='Condo'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='g-apt':
			self.type='House/Duplex'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='duplex':
			self.type='House/Duplex'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='garageapartments':
			self.type='House/Duplex'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='m':
			self.type='Condo'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='h':
			self.type='House/Duplex'
		elif str(self.data['values']['acr_type']).lower().replace(' ','')=='house':
			self.type='House/Duplex'

		
		

	def set_address(self, value):
		if "3412 speedway" in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'')
		elif "107 nelray" in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'')
		elif "704 franklin" in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'')
		elif "5212 guadalupe" in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'')
		elif "500 zennia" in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'')
		elif "1038 e 43rd" in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'')
		elif "2505 seton " in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'')
		elif "unit" in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'').replace('Unit','').replace('unit','')
		elif "912 w 22 1/2" in str(self.data['values']['acr_address']).lower():
			self.address=str(self.data['values']['acr_address']).replace(str(self.data['values']['acr_address']).split()[-1],'').replace('Unit','').replace('unit','').replace('-','')
		elif "-" in self.data['values']['acr_address']:
			self.address=self.data['values']['acr_address'].split('-',2)[0]
			
		else:
			self.address = self.data['values']['acr_address'].split('#', 1)[0].strip()

	def set_unit(self, value):
		if "3412 speedway" in str(self.data['values']['acr_address']).lower():
			self.unit=str(self.data['values']['acr_address']).split()[-1].replace('#','')
		elif "107 nelray" in str(self.data['values']['acr_address']).lower():
			self.unit=str(self.data['values']['acr_address']).split()[-1].replace('#','')
		elif "704 franklin" in str(self.data['values']['acr_address']).lower():
			self.unit=str(self.data['values']['acr_address']).split()[-1].replace('#','')
		elif "5212 guadalupe" in str(self.data['values']['acr_address']).lower():
			self.unit=str(self.data['values']['acr_address']).split()[-1].replace('#','')
		elif "500 zennia" in str(self.data['values']['acr_address']).lower():
			self.unit=str(self.data['values']['acr_address']).split()[-1].replace('#','')
		elif "1038 e 43rd a" in str(self.data['values']['acr_address']).lower():
			self.unit=str(self.data['values']['acr_address']).split()[-1].replace('#','')
		elif "unit" in str(self.data['values']['acr_address']).lower():
			self.unit=str(self.data['values']['acr_address']).split()[-1].replace('#','')
		elif "912 w 22 1/2" in str(self.data['values']['acr_address']).lower():
			self.unit=str(self.data['values']['acr_address']).split()[-1].replace('#','')
		elif "-" in self.data['values']['acr_address'] and len(self.data['values']['acr_address'].split('-',2)[1]) <= 8:
			self.unit=self.data['values']['acr_address'].split('-',2)[1]
			

		
		else:
			address_lst = self.data['values']['acr_address'].split('#', 1)
			self.unit = address_lst[1].strip() if len(address_lst) > 1 else ''

	def set_bedroom(self, value):
		bdrm = float(self.data['values']['bedroom'].strip()) if len(self.data['values']['bedroom'].strip()) > 0 else 0
		study = float(self.data['values']['study'].strip()) if len(self.data['values']['study'].strip()) > 0 else 0
		bedroom_int = int( bdrm + study )
		self.bedroom=str(bedroom_int)



	