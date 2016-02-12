from BaseCompanyProperty import BaseCompanyProperty
class UniversityRealtyProperty(BaseCompanyProperty):
	def setup(self):
		self.commission='.4'
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = 'University Realty | $75 App Fees, Deposit = 1st Month\'s Rent'
	
	
	def set_status(self, value):
		self.status = 'Leased' if self.is_highlighted() and not self.is_highlighted(None,'white') else 'Active'
	def set_unit(self,value):
		self.unit=str(self.get_attribute('university_unit')).replace('.0','')
	def set_zip_code(self,value):
		self.zip_code=str(self.get_attribute('university_zip_code')).replace('.0','')

	def set_title(self, value):
		self.title = str(self.get_attribute('property') + ' ' + self.get_attribute('unit')).replace('.0','')

	def set_bedroom(self,value):
		try:
			if '_' in self.data['values']['size']:
				self.bedroom=self.data['values']['size'].split('_',1)[0]
			else:
				self.bedroom = 0 if self.data['values']['size'].lower()=="room" or self.data['values']['size'].lower()=="eff" else self.data['values']['size'].split('-',1)[0] 
		except:
			self.bedroom=0
	def set_bathroom(self,value):
		try:
			if '_' in self.data['values']['size']:
				self.bathroom=self.data['values']['size'].split('_',1)[1]
			else:
				self.bathroom = 1 if self.data['values']['size'].lower()=="room" or self.data['values']['size'].lower()=="eff" else self.data['values']['size'].split('-',1)[1]
		except:
			self.bathroom=0
	def set_price_bedroom(self, value):
		
		rent = 0 if len(self.get_attribute('monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('monthly_rent').replace(',','').replace(' ', ''))
		
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	
	
	