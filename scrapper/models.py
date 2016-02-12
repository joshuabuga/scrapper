from __future__ import unicode_literals

from django.db import models

class Uploaded_file(models.Model):
	file=models.FileField(upload_to='files',blank=True, null=True)
	class Meta:
		db_table='Uploaded_file'
class MasterCsv(models.Model):
	external_id=models.IntegerField(null=True)
	status=models.CharField(max_length=1000)
	company=models.CharField(max_length=1000,null=True,blank=True)
	m=models.CharField(max_length=1000,null=True,blank=True)
	title=models.CharField(max_length=1000,null=True,blank=True)
	address=models.CharField(max_length=1000,null=True,blank=True)
	unit=models.CharField(max_length=1000,null=True,blank=True)
	city=models.CharField(max_length=1000,null=True,blank=True)
	state=models.CharField(max_length=1000,null=True,blank=True)
	zip_code=models.CharField(max_length=1000,null=True,blank=True)
	square_feet=models.CharField(max_length=1000,null=True,blank=True)
	forms=models.CharField(max_length=1000,null=True,blank=True)
	parking_space=models.CharField(max_length=1000,null=True,blank=True)
	area=models.CharField(max_length=1000,null=True,blank=True)
	type=models.CharField(max_length=1000,null=True,blank=True)
	bedroom=models.CharField(max_length=1000,null=True,blank=True)
	bathroom=models.CharField(max_length=1000,null=True,blank=True)
	monthly_rent=models.CharField(max_length=1000,null=True,blank=True)
	price_bedroom=models.CharField(max_length=1000,null=True,blank=True)
	available=models.CharField(max_length=1000,null=True,blank=True)
	paid_utilities=models.CharField(max_length=1000,null=True,blank=True)
	pets=models.CharField(max_length=1000,null=True,blank=True)
	pets_info=models.CharField(max_length=1000,null=True,blank=True)
	laundry=models.CharField(max_length=1000,null=True,blank=True)
	web_description=models.CharField(max_length=10000,null=True,blank=True)
	tenant_phone=models.CharField(max_length=1000,null=True,blank=True)
	gate_code=models.CharField(max_length=1000,null=True,blank=True)
	key_number=models.CharField(max_length=1000,null=True,blank=True)
	email=models.CharField(max_length=1000,null=True,blank=True)
	commission=models.CharField(max_length=1000,null=True,blank=True)
	bonus=models.CharField(max_length=1000,null=True,blank=True)
	deposit_paid_to=models.CharField(max_length=1000,null=True,blank=True)
	description=models.CharField(max_length=1000,null=True,blank=True)
	double_occupancy=models.CharField(max_length=1000,null=True,blank=True)
	dbl_occ_info=models.CharField(max_length=1000,null=True,blank=True)
	listing_type=models.CharField(max_length=1000,null=True,blank=True)
	pool=models.CharField(max_length=1000,null=True,blank=True)
	class Meta:
		db_table='master_csv'

