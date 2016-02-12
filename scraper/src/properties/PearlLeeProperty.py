from BaseCompanyProperty import BaseCompanyProperty
class PearlLeeProperty(BaseCompanyProperty):
	def setup(self):
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = 'Lee Properties Deposit:  $250PP | Application: $100 PP | Admin: $250 PP |'
		
		self.address ='2104 Pearl Street'
		self.zip ='78705'
		self.parking_space ='Standard $95/Wide Standard $105/Truck $115'
		self.area='WC'
		self.type ='Apartment'
		self.paid_utilities='Cable and Internet'
		self.pets='Yes'
		self.address='2104 Pearl Street'
		self.commission='.4'
		
		self.pets_info='Pet Deposit: $300 Non-refundable (No Dogs)'
	
	def set_status(self, value):
		self.status = 'Active' if self.get_attribute('pearl_status').lower().strip()=='available' else 'Leased'
	def set_title(self,value):
		self.title= '21 Pearl' + ' ' + self.get_attribute('unit').replace('.0','')

	def set_bedroom(self,value):
		bedroom='' if len(self.get_attribute('plan_description'))==0 else self.get_attribute('plan_description').split('/',1)[0][0]
		if 'loft' in self.get_attribute('plan_description').lower():
			self.bedroom=int(bedroom) + 1
		else:
			self.bedroom=bedroom

	def set_bathroom(self,value):
		self.bathroom='' if len(self.get_attribute('plan_description'))==0 else self.get_attribute('plan_description').split('/',1)[1].strip()[0]
	def set_price_bedroom(self, value):
		rent = 0 if len(self.get_attribute('monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('monthly_rent').replace(',','').replace(' ', ''))
		
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	def set_description(self,value):
		self.description=self.get_attribute('floor_plan') + ',' + self.get_attribute('plan_description') + ',' + 'Floor' + ' ' + self.get_attribute('floor') + ',' + 'Internet included | Washer & Dryer | Concrete Floors | 24 hour Fitness  | Covered Parking & Storage Rooms | Renter\'s Insurance Required'
	


