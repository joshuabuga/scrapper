from BaseCompanyProperty import BaseCompanyProperty
class TowerRealtyProperty(BaseCompanyProperty):
	def setup(self):
		self.forms ='TAR + ADDENDA'
		self.deposit_paid_to = 'Tower Realty | $100/person App Fees, Deposit = 1 Month\'s Rent'
		self.commission="0.4"
	
	
	def set_status(self, value):
		self.status = 'Leased' if self.is_highlighted() and not self.is_highlighted(None,'white') else 'Active'
	def set_tenant_phone(self,value):
		self.tenant_phone=self.data['values']['phone_one'] + '\n' + self.data['values']['phone_two'] + '\n' + self.data['values']['phone_three']

	def set_title(self, value):
		self.title = self.get_attribute('property') + ' ' + self.get_attribute('unit').replace('.0','')
	def set_bedroom(self, value):
		try:
			self.bedroom = self.data['values']['size'].split('-', 1 )[0].replace('bed','')
		except:
			self.bedroom=' '

	def set_bathroom(self, value):
		try:
			self.bathroom = self.data['values']['size'].split('-', 1)[1].replace('bed','')
		except:
			self.bathroom=' '
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
	
	def set_type(self,value):
		self.type =str(self.data['values']['tower_type'])
		if str(self.data['values']['tower_type']).lower().replace(' ','')=='a':
			self.type='Apartment'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='c':
			self.type='Condo'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='apt':
			self.type='Apartment'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='condo/apartment':
			self.type='Condo'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='d':
			self.type='House/Duplex'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='f':
			self.type='Condo'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='g-apt':
			self.type='House/Duplex'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='duplex':
			self.type='House/Duplex'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='garageapartments':
			self.type='House/Duplex'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='m':
			self.type='Condo'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='h':
			self.type='House/Duplex'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='house':
			self.type='House/Duplex'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='2-plex':
			self.type='House/Duplex'
		elif str(self.data['values']['tower_type']).lower().replace(' ','')=='4-plex':
			self.type='House/Duplex'
	def set_bonus(self,value):
		if '+' in self.data['values']['tower_commission']:
			self.bonus=self.data['values']['tower_commission'].split('+',2)[1].replace('Bonus','')
		else:
			self.bonus=''




