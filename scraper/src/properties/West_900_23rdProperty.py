from BaseCompanyProperty import BaseCompanyProperty
import re
class  West_900_23rdProperty(BaseCompanyProperty):
	def setup(self):
		
		self.commission ='' if  len(self.get_attribute('floor_plan'))==0 else '.4'
		self.pets ='' if  len(self.get_attribute('floor_plan'))==0 else 'NO'
		self.gate_code='' if  len(self.get_attribute('floor_plan'))==0 else '0822'
		self.key_number ='' if  len(self.get_attribute('floor_plan'))==0 else 'MLS'
		self.zip_code = '' if  len(self.get_attribute('floor_plan'))==0 else '78705'
		self.address='' if  len(self.get_attribute('floor_plan'))==0 else '900 W 23rd'
		self.forms ='' if  len(self.get_attribute('floor_plan'))==0 else 'TAA'
		self.available ='' if  len(self.get_attribute('floor_plan'))==0 else '8/19/2014'
		self.bathroom= '' if  len(self.get_attribute('floor_plan'))==0 else 2
		self.area='' if  len(self.get_attribute('floor_plan'))==0 else 'WC'
		self.type='' if  len(self.get_attribute('floor_plan'))==0 else 'Condo'
		self.deposit_paid_to = '' if  len(self.get_attribute('floor_plan'))==0 else 'Austin Investments | $50 App Fee to Austin Investments | Deposit=1 Month\'s Rent to White/Coffee LTD. | 1st Month\'s Rent paid to Austin Investments.'


	
	def set_unit(self, value):
		self.unit = '' if len(self.get_attribute('floor_plan'))==0 else self.get_attribute('floor_plan').split('/',3)[0]
	def set_square_feet(self,value):
		
		self.square_feet='' if len(str(self.get_attribute('floor_plan')))==0 else str(self.get_attribute('floor_plan')).split('/',3)[2].replace(' ','').replace('Sq.Ft.','')
		
	def set_title(self, value):
		self.title = '' if  len(self.get_attribute('floor_plan'))==0 else '900 W 23rd' + ' ' + self.get_attribute('unit')
	
	def set_status(self, value):
		if  len(self.get_attribute('west_status'))==0:
			self.status=''
		else:
			self.status= 'Active' if str(self.get_attribute('west_status')).lower().replace(' ','')=='available' else 'Leased' 
 

	
	def  set_bedroom(self,value):
		self.bedroom = '' if len(self.get_attribute('floor_plan'))==0 else self.get_attribute('floor_plan').split('/',3)[1][1]
	def set_description(self,value):
		self.description='' if len(self.get_attribute('floor_plan'))==0 else self.get_attribute('floor_plan').split('/',3)[1]
	def set_parking_space(self,value):
		if len(self.get_attribute('floor_plan'))==0:
			self.parking_space= ''
		elif str(self.get_attribute('floor_plan').split('/',3)[1][1])=='2':
			self.parking_space='2 RSVD'
		else:
			self.parking_space=" 2 RSVD 1 Unassigned"
	def set_price_bedroom(self, value):
		rent = 0 if len(self.get_attribute('monthly_rent').replace(' ', '')) == 0 else float(self.get_attribute('monthly_rent').replace(',','').replace(' ', ''))
		
		try:
			bedroom = float(self.get_attribute('bedroom'))
		except:
			bedroom = 0
			
		self.price_bedroom = rent if bedroom == 0 else round(rent / bedroom , 2)
	
