from BaseCompanyProperty import BaseCompanyProperty
class UptownProperty(BaseCompanyProperty):

	def setup(self):
		self.commission = '.5'
		self.forms='TAR + Addenda'
		self.deposit_paid_to = 'Uptown Realty | $50 App Fee, $50 Guarantor, $100 Admin Fee, Deposit = 1 Month\'s Rent'

	
	def set_status(self, value):
		self.status = 'Active' if str(self.data['values']['uptown_status']).strip()=='A' else 'Leased' 

	def set_title(self, value):
		self.title = self.get_attribute('address') + ' ' + self.get_attribute('unit') if len(self.data['values']['property']) == 0 else self.data['values']['property'] + ' ' + self.get_attribute('unit')

	def set_address(self, value):
		if '#' in self.data['values']['uptown_address']:
			self.address=self.data['values']['uptown_address'].split('#', 1 )[0]
		elif "5100 bruning" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "5100 avenue" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "905 w. 22nd 1/2 st" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "speedway" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "$" in str(self.data['values']['uptown_address']).lower():
			self.address=self.data['values']['uptown_address'].split('$', 1 )[0]
		elif "106 east 38th st." in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "5209 evans" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "chestnut" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "winsted" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "2931 east mlk" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')

		elif "west north loop" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "harris" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "1708 e. 17th street" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "5501 duval" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "5402 duval" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "106 nelray" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
		elif "3558 rr" in str(self.data['values']['uptown_address']).lower():
			self.address=str(self.data['values']['uptown_address']).replace(str(self.data['values']['uptown_address']).split()[-1],'')
						
	


		else:
			self.address = '' if len(self.data['values']['uptown_address']) == 0 else self.data['values']['uptown_address']

	def set_unit(self, value):
		if '#' in self.data['values']['uptown_address']:
			self.unit=self.data['values']['uptown_address'].split('#', 1 )[1]
		elif "5100 bruning " in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "5100 avenue" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "905 w. 22nd 1/2 st" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "speedway" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "$" in str(self.data['values']['uptown_address']).lower():
			self.unit=self.data['values']['uptown_address'].split('$', 1 )[1]
			
		elif "106 east 38th st." in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "5209 evans" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "chestnut" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "winsted" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "2931 east mlk" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "west north loop" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "park" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "1708 e. 17th street" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "5501 duval" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "5402 duval" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "3558 rr" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		elif "106 nelray" in str(self.data['values']['uptown_address']).lower():
			self.unit=str(self.data['values']['uptown_address']).split()[-1]
		  


		else:
			self.unit = ''
	def set_price_bedroom(self, value):
		try:
			rent = 0 if len(self.get_attribute('monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('monthly_rent').replace(',','').replace(' ', ''))
		except:
			rent=0
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	

	def set_pets(self, value):
		self.pets = 'No' if value.lower() == 'no' else 'Yes'

	def set_pets_info(self, value):
		self.pets_info = self.data['values']['pets']
	def set_area(self,value):

		if str(self.data['values']['uptown_area']).lower().replace(' ','')=='westcampus':
			self.area='WC'

		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='tarrytown':
			self.area='EF/TT'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='tt/ef':
			self.area='EF/TT'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='hp/nc':
			self.area='NC/HP'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='northcampus':
			self.area='NC/HP'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='northcampus/hydepark':
			self.area='NC/HP'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='hydepark':
			self.area='NC/HP'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='hydepark/northloop':
			self.area='NC/HP'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='eastcampus':
			self.area='EC'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='th/soco':
			self.area='SOCO/TH'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='rs':
			self.area='Riverside/East Oltorf'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='south':
			self.area='S'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='southaustin':
			self.area='S'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='eastaustin':
			self.area='EC'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='abr/fw':
			self.area='ABR/FW'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='central':
			self.area='NC/HP'
		elif str(self.data['values']['uptown_area']).lower().replace(' ','')=='nc':
			self.area='NC/HP'
		else:
			self.area =str(self.data['values']['uptown_area'])
	def set_type(self,value):
		self.type =str(self.data['values']['uptown_type'])
		if str(self.data['values']['uptown_type']).lower().replace(' ','')=='a':
			self.type='Apartment'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='c':
			self.type='Condo'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='condo/apartments':
			self.type='Condo'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='d':
			self.type='House/Duplex'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='f':
			self.type='Condo'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='g-apt':
			self.type='House/Duplex'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='duplex':
			self.type='House/Duplex'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='garageapartments':
			self.type='House/Duplex'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='m':
			self.type='Condo'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='h':
			self.type='House/Duplex'
		elif str(self.data['values']['uptown_type']).lower().replace(' ','')=='house':
			self.type='House/Duplex'



