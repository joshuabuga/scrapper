from BaseCompanyProperty import BaseCompanyProperty
class CampusCentralProperty(BaseCompanyProperty):
	def setup(self):
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = 'Campus and Central Properties | $75 App Fee/person, $75 Admin Fee'
		self.commission ='.4'
	
	def set_status(self, value):
		self.status = 'Leased' if self.is_highlighted() and not self.is_highlighted(None,'white') else 'Active'
	def set_address(self,value):
		if 'house' in self.data['values']['ccp_address'].lower():
			self.address= self.data['values']['complex'].replace(self.get_attribute('unit'),'').replace('Unit','').replace('unit','')
		else:
			self.address= self.data['values']['ccp_address'].replace('Unit','').replace('unit','')

	def set_title(self, value):
		self.title = self.data['values']['complex'] 

	def set_unit(self, value):
		try:
			if 'ave' in self.data['values']['complex'].split()[-1].lower():

				self.unit=''
			elif '52nd' in self.data['values']['complex'].split()[-1].lower():
			
				self.unit=''
			elif 'room' in self.data['values']['complex'].split()[-1].lower():
			
				self.unit='A 1 room'
			elif '1/2' in self.data['values']['complex'].split()[-1].lower():
			
				self.unit=''
			elif 'king' in self.data['values']['complex'].split()[-1].lower():
			
				self.unit=''


			else:
				self.unit =self.data['values']['complex'].split()[-1] if len(self.data['values']['complex'].split()[-1]) < 5 else ''
		except:
			self.unit=''
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
	
