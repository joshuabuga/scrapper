from BaseCompanyProperty import BaseCompanyProperty
from collections import Counter
class Realty512Property(BaseCompanyProperty):
	def setup(self):
		self.forms ='TAA+ ADDENDA'
		self.pets = 'Yes'
		self.commission='.4'
		self.pets_info='$300 Deposit if under 40 lbs, $500 if heavier.'
		self.deposit_paid_to = '512 Realty | $65/Applicant, $65/Guarantor, $100 Admin/Max $300 | Deposit = 1 Month\'s Rent, First full Month\'s Rent paid at Lease Signing'
	
	
	def set_status(self, value):
		self.status = 'Leased' if 'application pending' in self.data['values']['512_description'].lower() or 'renewed' in self.data['values']['512_description'].lower() or 'leased' in self.data['values']['512_description'].lower() or 'renewal pending' in self.data['values']['512_description'].lower() or 'renewal' in self.data['values']['512_description'].lower() or 'lease pending' in self.data['values']['512_description'].lower()  else 'Active'
	# def set_unit(self,value):
	# 	self.unit='' if not self.get_attribute('realty_address').strip().split()[0] else self.get_attribute('realty_address').strip().split()[0]  
	# # def set_address(self,value):
	# 	self.unit=self.get_attribute('realty_address').split()[-1]
		
	def set_area(self,value):
		self.area =str(self.data['values']['512_area'])
		if str(self.data['values']['512_area']).lower().replace(' ','')=='westcampus':
			self.area='WC'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='tarrytown':
			self.area='EF/TT'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='tt/ef':
			self.area='EF/TT'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='hp/nc':
			self.area='NC/HP'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='northcampus':
			self.area='NC/HP'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='northcampus/hydepark':
			self.area='NC/HP'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='th/soco':
			self.area='SOCO/TH'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='rs':
			self.area='Riverside/East Oltorf'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='south':
			self.area='S'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='southaustin':
			self.area='S'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='eastaustin':
			self.area='EC'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='abr/fw':
			self.area='ABR/FW'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='central':
			self.area='NC/HP'
		elif str(self.data['values']['512_area']).lower().replace(' ','')=='NC':
			self.area='NC/HP'
	def set_address(self,value):
		try:
			length=len(str(self.data['values']['realty_address'].split()[-1]))		
			s=self.data['values']['realty_address']
			#w=s[s.rfind(" "):].isdigit()
			hash_value='#'
			ave_string_1='avenue'
			ave_string_2='ave'
			ave_string_3='Avenue'
			ave_string_4='Ave.'
			comma_string=','
			unit_string="UNIT"
			if hash_value in s:
				self.address=s.split('#',2)[0]
			elif s.split()[-1].isdigit():
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif comma_string in s:
				self.address=s.split(',',2)[0].replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_1  not in s.lower().strip():
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_2  not in s.lower().strip():
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_3  not in s.strip():
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_4  not in s.strip():
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_1  not in s.lower():
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_2  not in s.lower():
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_3  not in s:
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_4  not in s:
				self.address=s.replace(s.split()[-1],'').replace(unit_string,'')
			elif len(s.split()[-1])==1 and ave_string_1 in s.lower().replace('.',''):
				self.address=s
			elif len(s.split()[-1])==1 and ave_string_3 in s:
				self.address=s
			elif '2520 Elmont Dr.' in s:
				self.address=s.split('.',2)[0]
			elif '3704 Speedway' in s:
				self.address=s.split()[0] + ' ' + s.split()[1]
			elif '1200 E 52nd' in s:
				self.address=s.replace(s.split()[-1],'')
			elif '1302 Parker Lane' in s:
				self.address=s.split()[0] + ' ' + s.split()[1] + ' ' + s.split()[2]
			elif '2506 Manor Circle' in s:
				self.address=s.replace(s.split()[-1],'')
			elif '7200 Duval' in s:
				self.address=s.replace(s.split()[-1],'')
			
			 
			
			

			# elif "swisher" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[2],'')
			# elif "speedway" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[2],'')
			# elif "red river" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[3],'')
			# elif "alpine" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[3],'')
			# elif "walnut" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[2],'')
			# elif "w 38th" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[3],'')
			# elif "w 26th" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[3],'')
			# elif "2513 san gabriel" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "1909 san gabriel b" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			
			# elif "shadow valley" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "803 tirado" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "809 tirado" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "burns" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "w 39th" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "whitis" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "5305 roosevelt a" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "helms" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "4400 ave" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "7302 duval" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "7304 duval" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "ave." in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "north hills" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "3405 cedar b" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "east riverside" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "404 w. 35th" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "e 34th" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "guadalupe" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "w. 35th" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "avenue b" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			
			# elif "avenue a" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "1011 w. 23rd" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "4558 ave a " in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "516 e 40th " in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "quail valley " in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "croslin" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# # elif "highland terrace" in str(self.data['values']['realty_address']).lower():
			# # 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "3405 cedar St" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "1907 san gabriel" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
			# elif "1909 san gabriel a" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "1500 hartford a" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "lamar place" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "10011 quail valley" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "7200 duval" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "1302 parker lane" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "6505 shirley" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "elmont dr." in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split(".",2)[1],'')
	 	# 	elif "parker lane" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "taylor gaines" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif "parker" in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 	# 	elif " 10700 topperwein dr." in str(self.data['values']['realty_address']).lower():
			# 	self.address=str(self.data['values']['realty_address']).replace(str(self.data['values']['realty_address']).split()[-1],'')
	 		                                           
	         
	      
	 

			else:
				self.address=self.data['values']['realty_address']
		except:
			self.address=''
			
	
	def set_unit(self,value):
		try:
			length=len(str(self.data['values']['realty_address'].split()[-1]))
			
			s=self.data['values']['realty_address']
			#w=s[s.rfind(" "):].isdigit()
			hash_value='#'
			ave_string_1='avenue'
			ave_string_2='ave'
			ave_string_3='Ave.'
			ave_string_4='Avenue'
			comma_string=','
			if hash_value in s:
				self.unit=s.split('#',2)[1]
			elif s.split()[-1].isdigit():
				self.unit=s.split()[-1]
			elif comma_string in s:
				self.unit=s.split(',',2)[1]
			elif len(s.split()[-1])==1 and ave_string_1 not in s.lower().strip():
				self.unit=s.split()[-1]
			elif len(s.split()[-1])==1 and ave_string_2 not in s.lower().strip():
				self.unit=s.split()[-1]
			elif len(s.split()[-1])==1 and ave_string_3 not in s.strip():
				self.unit=s.split()[-1]
			elif len(s.split()[-1])==1 and ave_string_4 not in s.strip():
				self.unit=s.split()[-1]
			elif len(s.split()[-1])==1 and ave_string_1 not in s.lower():
				self.unit=s.split()[-1]
			elif len(s.split()[-1])==1 and ave_string_2 not in s.lower():
				self.unit=s.split()[-1]
			elif len(s.split()[-1])==1 and ave_string_3 not in s:
				self.unit=s.split()[-1]
			elif len(s.split()[-1])==1 and ave_string_4 not in s:
				self.unit=s.split()[-1]
			elif len(s.split()[-1])==1 and ave_string_1 in s.lower().replace('.',''):
				self.unit=''
			elif len(s.split()[-1])==1 and ave_string_3 in s:
				self.unit=''
			elif '2520 Elmont Dr.' in s:
				self.unit=s.split('.',2)[1]
			elif '3704 Speedway' in s:
				self.unit=s.replace(s.split()[0] + ' ' + s.split()[1],'')
			elif '1200 E 52nd' in s:
				self.unit=s.split()[-1]
			elif '1302 Parker Lane' in s:
				self.unit=s.replace(s.split()[0] + ' ' + s.split()[1] + ' ' + s.split()[2],'')
			elif '2506 Manor Circle' in s:
				self.unit=s.split()[-1]
			elif '7200 Duval' in s:
				self.unit=s.split()[-1]
		
		
		
	
		# elif "swisher" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "speedway" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "red river" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "803 tirado" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "809 tirado" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "red river" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "walnut" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "w 38th" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "w 26th" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "2513 san gabriel " in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "shadow valley" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "burns" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "w 39th" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "whitis" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "5305 roosevelt a" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "helms" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "4400 ave" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "ave." in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "7302 duval" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "7304 duval" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "alpine" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "north hills" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "3405 cedar b" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "east riverside" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "404 w. 35th" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "e 34th" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "guadalupe" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "w. 35th" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "avenue b" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "avenue a" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "1011 w. 23rd " in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "4558 ave a " in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "516 e 40th " in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "quail valley " in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "croslin" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# # elif "highland terrace" in str(self.data['values']['realty_address']).lower():
		# # 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "3405 cedar st " in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "1907 san gabriel" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "1909 san gabriel b" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "1909 san gabriel a" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "1500 hartford a" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "lamar place" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "10011 quail valley" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "7200 duval" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "1302 parker lane" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "6505 shirley" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "parker lane" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "taylor gaines" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "elmont dr." in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split(".",2)[1]
		# elif "parker" in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		# elif "10700 topperwein dr." in str(self.data['values']['realty_address']).lower():
		# 	self.unit=str(self.data['values']['realty_address']).split()[-1]
		

			else:
				self.unit=''
		except:
			self.unit=''
		
		
	def set_title(self, value):
		if '#' in self.data['values']['realty_address'].lower().strip() and "house/duplex" in self.get_attribute('property').lower() or self.get_attribute('property').lower()=="":
			self.title=self.data['values']['realty_address']
		else:
			self.title = self.get_attribute('address')+ ' ' + self.get_attribute('unit') if "house/duplex" in self.get_attribute('property').lower() or self.get_attribute('property').lower()=="" else self.get_attribute('property') + ' ' + self.get_attribute('unit')
	def set_type(self,value):
		self.type=self.get_attribute('property') if "house/duplex" in self.get_attribute('property').lower() else "Condo"
	def set_available(self,value):
		self.available= '8/1/15' if str(self.get_attribute('512_available').lower().replace(' ',''))=='summer2015' else self.get_attribute('512_available')
	def set_description(self,value):
		self.description=self.data['values']['512_description'] + ' ' + ',' + 'Laundry ' + self.data['values']['laundry']
