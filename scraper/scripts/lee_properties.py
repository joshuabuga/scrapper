import csv
class getLeePropertiesData():
	
	"""docstring for getRealtyProsData"""
	company="Realty Pros"
	city="Austin"
	state="TX"
	description=[]
	
	def __init__(self):

		#initialize attributes
		self.city=getRealtyProsData.city
		self.state=getRealtyProsData.state
		self.company=getRealtyProsData
		self.status=[]
		self.m=[]
		self.title=[]
		self.address=[]
		self.unit=[]
		self.zip_code=[]
		self.square_feet=[]
		self.forms=[]
		self.parking_spaces=[]
		self.area=[]
		self.property_type=[]
		self.bedroom=[]
		self.bathroom=[]
		self.monthly_rent=[]
		self.price_bedroom=getRealtyProsData.price_bedroom
		self.available=[]
		self.paid_utilities=[]
		self.pets=[]
		self.tenant_phone=[]
		self.description=[]
		print "global ",self.description
		self.gate_code=[]
		self.key_number=[]
		self.email=[]
		self.commission=[]
		self.bonus=[]
		self.deposit_and_1st_month_rent_paid_to=[]
	def read_csv():
		data_list=[]
		file_name='lee_properties1.csv'

		with open(file_name, "rb") as f:
			for line in f:
				line=line.lower()
				line=line.replace(" ","")
				line=str(line)
				line=line.strip()
				print line 
				if "property,size,approx.sqftg.,parking,avail.,leaseend,rent,bybed,form,comm.,tenantinformation,propertyinfo,contact" in line:
	
					print "header found file will be processed"
					break
				else:
					print "dint find header"
			
			field_names=['property','size','approx sq ft','parking','available','lease end','rent','by end','form','commission','tenant information','property information','contact','empty_val']
			reader=csv.DictReader(f,fieldnames=field_names, restval=None,delimiter=",")
			
			for row in reader:
				data_list.append(row)
		return data_list

	def get_status(self):
		default="Available"
		self.state.append(default)
	def m():
		default=" "
		self.m.append(default)
	def title(self):
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			title.append(y)


	def address(self):
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			address.append(y)
	def unit():
		data=self.read_csv()
		for x in data:
			y=['unit']
			self.unit.append(y)

	def zip(self):
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			zip_code.append(y)
	def get_square_feet(self):
		square_feet=[]
		data=self.read_csv()
		for x in data:
			y=x['approx sq ft']
			square_feet.append(y)
			self.square_feet.append(y)
	def forms(self):
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			forms.append(y)
	def get_bedroom(self):
		bedroom=[]
		data=self.read_csv()
		for x in data:
			y=x['bed']
			bedroom.append(y)
		return bedroom
	def get_bathroom(self):
		bathroom=[]
		data=self.read_csv()
		for x in data:
			y=x['bath']
			bathroom.append(y)
		return bathroom

	def parking_spaces():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			data.append(y)
	def area():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			area.append(y)
	def property_type(self):

		data=self.read_csv()
		for x in data:
			y=['empty_val']
			property_type.append(y)
	def monthly_rent():
		monthly_rent=[]
		data=self.read_csv()
		for x in data:
			y=x['by bed']
			self.monthly_rent.append(y)

	def price_bedroom(self):
		data=self.read_csv()
		for x in data:
			y=['']
			price_bedroom.append(y)
	def available(self):
		available[]
		data=self.read_csv()
		for x in data:
			y=['available']
			available.append(y)
			self.available.extend(y)
	def paid_utilities():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			paid_utilities.append(y)
	def pets():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			pets.append(y)
	def tenant_phone(self):
		data=self.read_csv()
		for x in data:
			y=['']
	def get_description(self):
		description=[]
		data=self.read_csv()
		for x in data:
			y=x['description']
			description.append(y)
		self.description.extend(description)
		return description

	def gate_code():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			gate_code.append(y)
	def key_number():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			key_number.append(y)
	def email():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			email.append(y)
	
	def commission():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			commission.append(y)
	def bonus(self):
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			bonus.append(y)
	def deposit_and_1st_month_rent_paid_to():
		data=self.read_csv()
		for x in data:
			y=['empty_val']
			bonus.append(y)
p=getRealtyProsData()
print p.city
print p.get_description()
print p.get_bathroom()
print p.get_bedroom()
print p.description



		

		