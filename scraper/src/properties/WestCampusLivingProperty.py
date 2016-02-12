from BaseCompanyProperty import BaseCompanyProperty
class WestCampusLivingProperty(BaseCompanyProperty):
	def setup(self):
		self.forms ='TAA + ADDENDA'
		self.deposit_paid_to = '24th Street Realty | $250 Admin Fee/Person | Deposit = $200/1 Bedroom and $300/2 Bedroom'
		self.address='711 W 32nd'
		self.zip_code='78705'
		self.parking_space='Included'
		self.area='NC/HP'
		self.type='Condo'
		self.description='12 Monthly installments. $50/month for double occ. This quiet pet-friendly 57 unit community isn\'t for \
		you unless you like Central location, tranquility, and A-class luxury. A hidden gem in Austin\'s prestigious Heritage neighborhood \
		on 32nd street North Campus, it\'s walking distance to Seton Medical, UT Austin and HEB\'s Central Market (711 W. 32nd Street in Austin, TX 78705). \
		 All townhouse style floor plans are 2-story and boast wood plank flooring, custom cabinets, plush berber carpet upstairs and recessed lighting throughout. \
		 Constructed with contemporary european influence the exterior walls are Austin limestone and classic stucco. Parking, in-unit washer and dryer, trash, and \
		 Internet and Time Warner cable is ALL included. '
		
		self.paid_utilities='Cable, Internet, and Trash'
		self.pets='Yes'
		self.pets_info='$300 Deposit, $150 Non-Refundable'
		self.tenant_phone='Vacant 1 Bed Show Unit #139'
		self.commission='60%'
		self.gate_code='0'

	
	
	def set_status(self, value):
		self.status = 'Active' if "available" in  str(self.data['values']['b_status']).lower() else 'Leased' 

	def set_title(self, value):
		self.title = "Buckingham Squre" +' '+ self.get_attribute('unit') 
	def set_price_bedroom(self, value):
		
		rent = 0 if len(self.get_attribute('monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('monthly_rent').replace(',','').replace(' ', '').replace('$',''))
		
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	


	