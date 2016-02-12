from __future__ import unicode_literals
from xlrd import open_workbook,XL_CELL_TEXT,colname,xldate_as_tuple
from itertools import izip
import xlrd
import datetime
import time
import csv

	#-----------------------------------------------------------------------------------------------------------
	#scrap data from chay's list xls file and format it for output
def getFormatChayslistdata():	
			
	"""
	mine data from different files,format the data and export it to mainlist csv file
	"""
	#-------------------------------------------------------------------------------------------------------------------
	# create headers for masterlist file(will go in row index 0 of file)
	status=["STATUS"]
	company=['COMPANY']
	individual_identifier=['UNIQUE IDENTIFIER FROM INDIVIDUAL LIST']
	master_identifier=['UNIQUE IDENTIFIER FROM MASTER LIST']
	m=['M']
	title=['TITLE']
	address=['ADDRESS']
	unit_list=['UNIT']
	city=['CITY']
	state=['STATE']
	zip_code=['ZIP']
	square_feet=['SQUARE FEET']
	forms=['FORMS']
	parking_space=['PARKING SPACE']
	area=['AREA']
	property_type=['TYPE']
	bedroom=['BEDROOM']
	bathroom=['BATHROOM']
	monthly_rent=['MONTHLY RENT']
	price_per_bedroom=['PRICE PER BEDROOM']
	available=['AVAILABLE']
	paid_utilities=['PAID UTILITIES']
	pets=['PETS']
	phone=['PHONE']
	description=['DESCRIPTION']
	gate_code=['GATE CODE']
	key_number=['KEY NUMBER']
	email=['EMAIL']
	bonus=["BONUS"]
	commission=['COMMISSION']
	depo_and_first_month_rent=['DEPOSIT AND FIRST MONTH\'S RENT PAID TO']
	blank_cells=['','','','','','']
	book = open_workbook('Chay\'s List 4_29_14.xls') # open workbook for read operation
	book_condos= open_workbook('Campus Condos--4-30-14.xls')#open campus condos book for read
	book_premier= open_workbook('Premier Realty--4-30-14.xlsx')#open campus condos book for read
	book_austin_centric=open_workbook('Austin Centric- Pre Lease List 05-01-14.xls')
	book_university=open_workbook('University Realty--4-30-14.xlsx')
	book_west_23rd=open_workbook('900 W 23rd--3-6-14.xlsx')
	university_sheet=book_university.sheet_by_index(0)
	austin_centric_sheet=book_austin_centric.sheet_by_index(0)
	condos_sheet=book_condos.sheet_by_index(0)
	sheet = book.sheet_by_index(0) # open individual sheet in workbook(workbook has one sheet with name sheet one and index 0)
	premier_sheet=book_premier.sheet_by_index(0)
	west_23rd_sheet=book_west_23rd.sheet_by_index(0)
	#---------------------------------------------------------------------------------------------------
	#provide default values for empty cells and repeating values
	chays_city=['Austin','Austin','Austin','Austin','Austin','Austin']
	chays_state=['TX','TX','TX','TX','TX','TX']
	chays_list_company=['CHAY\'S LIST','CHAY\'S LIST','CHAY\'S LIST','CHAY\'S LIST','CHAY\'S LIST','CHAY\'S LIST']
	forms_chays=['TAR + Addenda','TAR + Addenda','TAR + Addenda','TAR + Addenda','TAR + Addenda','TAR + Addenda']

	
	
	#------------------------------------------------------------------------------------
	# title
	for p in range(5,8):
		string_title=str(sheet.cell_value(p,1))
		title.append(string_title)
	title_string_subset_two=str(sheet.cell_value(9,1))
	title.append(title_string_subset_two)
	title_string_subset_three=str(sheet.cell_value(10,1))
	title.append(title_string_subset_three)
	title_string_subset_four=str(sheet.cell_value(13,1))
	title.append(title_string_subset_four)
	print title
	print "lenght of title at chays list",len(title)
	#------------------------------------------------------------------------------------
	# chay's property type
	for p in range(5,8):
		string_property=str(sheet.cell_value(p,2))
		property_type.append(string_property)
	property_string_subset_two=str(sheet.cell_value(9,2))
	property_type.append(property_string_subset_two)
	property_string_subset_three=str(sheet.cell_value(10,2))
	property_type.append(property_string_subset_three)
	property_string_subset_four=str(sheet.cell_value(13,2))
	property_type.append(property_string_subset_four)
	print property_type
	#------------------------------------------------------------------------------------
	#get chay's individual unique identifier
	for p in range(5,8):
		string_individual_identifier=str(sheet.cell_value(p,3))
		individual_identifier.append(string_individual_identifier)
	individual_identifier_string_subset_two=str(sheet.cell_value(9,3))
	individual_identifier.append(individual_identifier_string_subset_two)
	individual_identifier_string_subset_three=str(sheet.cell_value(10,3))
	individual_identifier.append(individual_identifier_string_subset_three)
	individual_identifier_string_subset_four=str(sheet.cell_value(13,3))
	individual_identifier.append(individual_identifier_string_subset_four)
	print "chays indiviual identifier", individual_identifier
	#------------------------------------------------------------------------------------
	#chay's unique identifier from master list(company + address + unit)
	chay_identifier_company="CHAY'S LIST"
	for a in range(5,8):
		identifier_address_string=str(sheet.cell_value(p,3))
		identifier_unit=identifier_address_string.strip()[3]
		chay_master_identifier= chay_identifier_company + " " + identifier_address_string + " " + identifier_unit
		master_identifier.append(chay_master_identifier)
	identifier_address_string2=str(sheet.cell_value(9,3))
	identifier_unit2=identifier_address_string2.strip()[3]
	chay_master_identifier2= chay_identifier_company + " " + identifier_address_string2 + " " + identifier_unit2
	master_identifier.append(chay_master_identifier2)
	identifier_address_string3=str(sheet.cell_value(10,3))
	identifier_unit3=identifier_address_string3.strip()[3]
	chay_master_identifier3= chay_identifier_company + " " + identifier_address_string3 + " " + identifier_unit3
	master_identifier.append(chay_master_identifier3)
	identifier_address_string4=str(sheet.cell_value(13,3))
	identifier_unit4=identifier_address_string4.strip()[3]
	chay_master_identifier4= chay_identifier_company + " " + identifier_address_string4 + " " + identifier_unit4
	master_identifier.append(chay_master_identifier4)
	print master_identifier

	#------------------------------------------------------------------------------------
	# get address
	for a in range(5,8):
		address_string=str(sheet.cell_value(p,3))
		stripped_address_string=address_string.split()[1] + address_string.split()[2]
		address.append(stripped_address_string)
	address_subset_two=str(sheet.cell_value(9,3))
	stripped_address_subset_two=address_subset_two.split()[1] 
	address.append(stripped_address_subset_two)
	address_subset_three=str(sheet.cell_value(10,3))
	stripped_address_subset_three=address_subset_three.split()[1]  
	address.append(stripped_address_subset_three)
	address_subset_four=str(sheet.cell_value(13,3))
	stripped_address_subset_four=address_subset_four.split()[1]
	address.append(stripped_address_subset_four)
	print address
	
	#------------------------------------------------------------------------------------
	# get status
	for s in range(5,8):
		status_string="Active"
		status.append(status_string)
	status_subset_two="Active"
	status.append(status_subset_two)
	status_subset_three="Active"
	status.append(status_subset_three)
	status_subset_four="Active"
	status.append(status_subset_four)
	print status
	#-------------------------------------------------------------------------------------
	#get unit
	for i in range(5,8):
		unit_string_subset_one=str(sheet.cell_value(i,3))
		unit_number_subset_one=unit_string_subset_one.split()[0]
		unit_list.append(unit_number_subset_one)
		
	unit_string_subset_two=str(sheet.cell_value(9,3))
	unit_number_subset_two=unit_string_subset_two.split()[0]
	unit_list.append(unit_number_subset_two)
	unit_string_subset_three=str(sheet.cell_value(10,3))
	unit_number_subset_three=unit_string_subset_three.split()[0]
	unit_list.append(unit_number_subset_three)
	unit_string_subset_four=str(sheet.cell_value(13,3))
	unit_number_subset_four=unit_string_subset_four.split()[0]
	unit_list.append(unit_number_subset_four)

	print unit_list
	print len(unit_list)
		#------------------------------------------------------------------------------------
	    # get bedroom
	for x in range(5,8):
		bedroom_string=sheet.cell_value(x,5)
		bedroom.append(bedroom_string)
	bedroom_subset_two=sheet.cell_value(9,5)
	bedroom.append(bedroom_subset_two)
	bedroom_subset_three=sheet.cell_value(10,5)
	bedroom.append(bedroom_subset_three)
	bedroom_subset_four=sheet.cell_value(13,5)
	bedroom.append(bedroom_subset_four)
	print bedroom
	#------------------------------------------------------------------------------------
	# get bathroom
	for y in range(5,8):
		bathroom_string=sheet.cell_value(y,6)
		bathroom.append(bathroom_string)
	bathroom_subset_two=sheet.cell_value(9,6)
	bathroom.append(bathroom_subset_two)
	bathroom_subset_three=sheet.cell_value(10,6)
	bathroom.append(bathroom_subset_three)
	bathroom_subset_four=sheet.cell_value(13,6)
	bathroom.append(bathroom_subset_four)
	print bathroom
	#------------------------------------------------------------------------------------
	# get monthly rent
	for z in range(5,8):
		monthly_rent_string=sheet.cell_value(z,7)
		monthly_rent.append(monthly_rent_string)
	monthly_rent_subset_two=sheet.cell_value(9,7)
	monthly_rent.append(monthly_rent_subset_two)
	monthly_rent_subset_three=sheet.cell_value(10,7)
	monthly_rent.append(monthly_rent_subset_three)
	monthly_rent_subset_four=sheet.cell_value(13,7)
	monthly_rent.append(monthly_rent_subset_four)
	print monthly_rent
	#------------------------------------------------------------------------------------
	# get price per bedroom
	for t in range(5,8):
		price_per_bedroom_string=str(sheet.cell_value(t,8))
		price_per_bedroom.append(price_per_bedroom_string)
	price_per_bedroom_subset_two=str(sheet.cell_value(9,8))
	price_per_bedroom.append(price_per_bedroom_subset_two)
	price_per_bedroom_subset_three=str(sheet.cell_value(10,8))
	price_per_bedroom.append(price_per_bedroom_subset_three)
	price_per_bedroom_subset_four=str(sheet.cell_value(13,8))
	price_per_bedroom.append(price_per_bedroom_subset_four)
	print price_per_bedroom
	#------------------------------------------------------------------------------------
	# get area and convert to unicode
	for f in range(5,8):
		area_string=sheet.cell_value(f,9)
		utf8_areastring = area_string.encode("utf-8")
		area.append(utf8_areastring)
	area_subset_two=sheet.cell_value(9,9)
	utf8_areastring_area_subset_two = area_subset_two.encode("utf-8")
	area.append(utf8_areastring_area_subset_two)
	area_subset_three=sheet.cell_value(10,9)
	utf8_areastring_area_subset_three = area_subset_three.encode("utf-8")
	area.append(utf8_areastring_area_subset_three)
	area_subset_four=sheet.cell_value(13,9)
	utf8_areastring_area_subset_four= area_subset_four.encode("utf-8")
	area.append(utf8_areastring_area_subset_four)
	print area
	#------------------------------------------------------------------------------------
	# get description and make it output friendly
	for d in range(5,8):
		description_string=str(sheet.cell_value(d,10))
		print description
		description.append(description_string)
	description_subset_two=str(sheet.cell_value(9,10))
	description_subset_two_utf8string = str(description_subset_two)
	description.append(description_subset_two)
	description_subset_three=sheet.cell_value(10,10)
	description_subset_three__utf8string = str(description_subset_three)
	description.append(description_subset_three__utf8string)
	description_subset_four=sheet.cell_value(13,10)
	description_subset_four_utf8string = str(description_subset_four)
	description.append(description_subset_four_utf8string)
	print description
	#------------------------------------------------------------------------------------
	# get phone
	for p in range(5,8):
		phone_string=str(sheet.cell_value(p,11))
		phone.append(phone_string)
	phone_subset_two=str(sheet.cell_value(9,11))
	phone.append(phone_subset_two)
	phone_subset_three=str(sheet.cell_value(10,11))
	phone.append(phone_subset_three)
	phone_subset_four=str(sheet.cell_value(13,11))
	phone.append(phone_subset_four)
	print phone
	#---------------------------------------------------------------------------------------
	#get available
	for a in range(5,8):
		available_string=str(datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(a,4),book.datemode)))[:10]
		available.append(available_string)
	available_subset_two=str(datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(a,4),book.datemode)))[:10]
	available.append(available_subset_two)
	available_subset_three=str(datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(a,4),book.datemode)))[:10]
	available.append(available_subset_three)
	available_subset_four=str(datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell_value(a,4),book.datemode)))[:10]
	available.append(available_subset_four)
	print available
	#append chays to main output stream
	city.extend(chays_city)
	print city

	company.extend(chays_list_company)
	print company
	
	m.extend(blank_cells)
	print m
	state.extend(chays_state)
	print state
	zip_code.extend(blank_cells)
	print zip_code
	square_feet.extend(blank_cells)
	print square_feet
	forms.extend(forms_chays)
	print forms
	parking_space.extend(blank_cells)
	print parking_space
	paid_utilities.extend(blank_cells)
	print paid_utilities
	pets.extend(blank_cells)
	print pets
	gate_code.extend(blank_cells)
	print gate_code
	bonus.extend(blank_cells)
	commission.extend(blank_cells)
	key_number.extend(blank_cells)
	print key_number
	email.extend(blank_cells)
	print email
	depo_and_first_month_rent.extend(blank_cells)
	print depo_and_first_month_rent
	#-----------------------------------------------------------------------------------
	

	#--------------------------------------------------------------------------------------
	# start campus condos
	#------------------------------------------------------------------------------------
	#campus condos list values
	condos_unit=[]
	condos_address=[]
	condos_rent=[]
	condos_phone=[]
	condos_description=[]
	condos_bathroom=[]
	condos_bedroom=[]
	condos_deposit_rent_paidto=[]
	condos_movein=[]
	condos_identifier_individual=[]
	condos_master_identifier=[]
	condos_status=[]
	campus_condos_title=[]
	campus_condos_column_c=[]
	condos_rent_per_bedroom=[]
	#set defaults for campus condos
	condos_default_city=['Austin','Austin','Austin','Austin','Austin','Austin','Austin','Austin','Austin','Austin','Austin','Austin']
	condos_default_state=['TX','TX','TX','TX','TX','TX','TX','TX','TX','TX','TX','TX']
	campus_condos_company=['CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS','CAMPUS CONDOS']
	condos_forms_default=['TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda','TAA + Addenda']
	condos_blank_cells=['','','','','','','','','','','','']
	condos_default_pets=['NO','NO','NO','NO','NO','NO','NO','NO','NO','NO','NO','NO']
	#campus condos commission
	condos_commission=['30%','30%','30%','30%','30%','30%','30%','30%','30%','30%','30%','30%']
	
	

	# get unit#
	for u in range(6,12):
		condos_unit_string=str(condos_sheet.cell_value(u,3))
		condos_unit.append(condos_unit_string)
	condos_unit_substring_one=str(condos_sheet.cell_value(14,3))
	condos_unit.append(condos_unit_substring_one)
	for u in range(17,21):
		condos_unit_substring_two=str(condos_sheet.cell_value(u,3))
		condos_unit.append(condos_unit_substring_two)
	condos_unit_substring_three=str(condos_sheet.cell_value(23,3))
	condos_unit.append(condos_unit_substring_three)
	print condos_unit
	print "condos unit",len(condos_unit)

	#---------------------------------------------------------------------------------------
	#get address for campus condos
	for u in range(6,12):
		condos_address_string=str(condos_sheet.cell_value(u,4))
		condos_address.append(condos_address_string)
	condos_address_substring_one=str(condos_sheet.cell_value(14,4))
	condos_address.append(condos_address_substring_one)
	for u in range(17,21):
		condos_address_substring_two=str(condos_sheet.cell_value(u,4))
		condos_address.append(condos_address_substring_two)
	condos_address_substring_three=str(condos_sheet.cell_value(23,4))
	condos_address.append(condos_address_substring_three)
	print condos_address
	print len(condos_address)
	#--------------------------------------------------------------------------------------
	#campus condos rent
	for u in range(6,12):
		condos_rent_string=float(condos_sheet.cell_value(u,1))
		condos_rent.append(condos_rent_string)
	condos_rent_substring_one=float(condos_sheet.cell_value(14,1))
	condos_rent.append(condos_rent_substring_one)
	for u in range(17,21):
		condos_rent_substring_two=float(condos_sheet.cell_value(u,1))
		condos_rent.append(condos_rent_substring_two)
	condos_rent_substring_three=float(condos_sheet.cell_value(23,1))
	condos_rent.append(condos_rent_substring_three)
	print condos_rent
	#------------------------------------------------------------------------------------
	#campus condos tenants number
	for u in range(6,12):
		condos_phone_string=str(condos_sheet.cell_value(u,5))
		condos_phone.append(condos_phone_string)
	condos_phone_substring_one=str(condos_sheet.cell_value(14,5))
	condos_phone.append(condos_phone_substring_one)
	for u in range(17,21):
		condos_phone_substring_two=str(condos_sheet.cell_value(u,5))
		condos_phone.append(condos_phone_substring_two)
	condos_phone_substring_three=str(condos_sheet.cell_value(23,5))
	condos_phone.append(condos_phone_substring_three)
	print condos_phone
	#---------------------------------------------------------------------------------------
	# campus condos description
	for u in range(6,12):
		condos_description_string=str(condos_sheet.cell_value(u,7))
		condos_description.append(condos_description_string)
	condos_description_substring_one=str(condos_sheet.cell_value(14,7))
	condos_description.append(condos_description_substring_one)
	for u in range(17,21):
		condos_description_substring_two=str(condos_sheet.cell_value(u,7))
		condos_description.append(condos_description_substring_two)
	condos_description_substring_three=str(condos_sheet.cell_value(23,7))
	condos_description.append(condos_description_substring_three)
	print condos_description
	#---------------------------------------------------------------------------------------
	#campus condos bedroom
	for u in range(6,12):
		condos_bedroom_string=int(1)
		condos_bedroom.append(condos_bedroom_string)
	condos_bedroom_substring_one=int(2)
	condos_bedroom.append(condos_bedroom_substring_one)
	for u in range(17,21):
		condos_bedroom_substring_two=int(2)
		condos_bedroom.append(condos_bedroom_substring_two)
	condos_bedroom_substring_three=int(4)
	condos_bedroom.append(condos_bedroom_substring_three)
	print "condos bedroom",condos_bedroom
	print len(condos_bedroom)
	#---------------------------------------------------------------------------------------
	#campus condos bathroom
	for u in range(6,12):
		condos_bathroom_string='1'
		condos_bathroom.append(condos_bathroom_string)
	condos_bathroom_substring_one='1'
	condos_bedroom.append(condos_bathroom_substring_one)
	for u in range(17,21):
		condos_bathroom_substring_two='2'
		condos_bathroom.append(condos_bathroom_substring_two)
	condos_bathroom_substring_three='2'
	condos_bathroom.append(condos_bathroom_substring_three)
	condos_bathroom_substring_four='2'
	condos_bathroom.append(condos_bathroom_substring_four)
	print condos_bathroom
	#-----------------------------------------------------------------------------------------
	# campus deposit and first month rent paid to
	for u in range(1,13):
		condos_deposit_rent_paidto_string=str("Campos Condos | App fee $100, Deposit= 1 Month's Rent" )
		condos_deposit_rent_paidto.append(condos_deposit_rent_paidto_string)
	print condos_deposit_rent_paidto
	print len(condos_deposit_rent_paidto)
	#-----------------------------------------------------------------------------------------
	# campus condos move in date
	for u in range(6,12):
		condos_movein_string=str(datetime.datetime(*xlrd.xldate_as_tuple(condos_sheet.cell_value(u,6),book_condos.datemode)))[:10]
		condos_movein.append(condos_movein_string)
	condos_movein_substring_one=str(datetime.datetime(*xlrd.xldate_as_tuple(condos_sheet.cell_value(14,6),book_condos.datemode)))[:10]
	condos_movein.append(condos_movein_substring_one)
	for u in range(17,21):
		condos_movein_substring_two=str(datetime.datetime(*xlrd.xldate_as_tuple(condos_sheet.cell_value(u,6),book_condos.datemode)))[:10]
		condos_movein.append(condos_movein_substring_two)
	condos_movein_substring_three=str(datetime.datetime(*xlrd.xldate_as_tuple(condos_sheet.cell_value(23,6),book_condos.datemode)))[:10]
	condos_movein.append(condos_movein_substring_three)
	print condos_movein	
	
	# unique identifier from individual list
	for u in range(6,12):
		condos_identifier_individual_string_address=str(condos_sheet.cell_value(u,4))
		condos_identifier_individual_string_unit=str(condos_sheet.cell_value(u,3))
		condos_identifier_individual1=condos_identifier_individual_string_address + " " + condos_identifier_individual_string_unit
		condos_identifier_individual.append(condos_identifier_individual1)
	condos_identifier_individual_substring_one_address=str(condos_sheet.cell_value(14,4))
	condos_identifier_individual_substring_one_unit=str(condos_sheet.cell_value(14,3))
	condos_identifier_individual2=condos_identifier_individual_substring_one_address + " " + condos_identifier_individual_substring_one_unit 
	condos_identifier_individual.append(condos_identifier_individual2)
	for u in range(17,21):
		condos_identifier_individual_substring_two_address=str(condos_sheet.cell_value(u,4))
		condos_identifier_individual_substring_two_unit=str(condos_sheet.cell_value(23,3))
		
		condos_identifier_individual3=condos_identifier_individual_substring_two_address + " " + condos_identifier_individual_substring_two_unit
		condos_identifier_individual.append(condos_identifier_individual3)
	condos_identifier_individual_substring_three_address=str(condos_sheet.cell_value(23,4))
	condos_identifier_individual_substring_three_unit=str(condos_sheet.cell_value(23,3))
	condos_identifier_individual4=condos_identifier_individual_substring_three_address + " " + condos_identifier_individual_substring_three_unit
	condos_identifier_individual.append(condos_identifier_individual4)
	print condos_identifier_individual	
	print len(condos_identifier_individual)
	#---------------------------------------------------------------------------------------
	# campus condos status
	for u in range(6,12):
		condos_status_string='Active'
		condos_status.append(condos_status_string)
	condos_status_substring_one='Active'
	condos_status.append(condos_status_substring_one)
	for u in range(17,21):
		condos_status_substring_two='Active'
		condos_status.append(condos_status_substring_two)
	condos_status_substring_three='Active'
	condos_status.append(condos_status_substring_three)
	condos_status[2]="Leased"
	print condos_status
	#campus condos master identifier
	for x,y in zip(campus_condos_company,condos_identifier_individual):
		condos_master_identifier_string= x + " " + y
		condos_master_identifier.append(condos_master_identifier_string)
	print "campus condos master_identifier",condos_master_identifier
	#get campus condos column c
	for u in range(6,12):
		condos_column_c_string=str(condos_sheet.cell_value(u,2))
		campus_condos_column_c.append(condos_column_c_string)
	condos_column_c_substring_one=str(condos_sheet.cell_value(14,2))
	campus_condos_column_c.append(condos_column_c_substring_one)
	for u in range(17,21):
		condos_column_c_substring_two=str(condos_sheet.cell_value(u,2))
		campus_condos_column_c.append(condos_column_c_substring_two)
	condos_column_c_substring_three=str(condos_sheet.cell_value(23,2))
	campus_condos_column_c.append(condos_column_c_substring_three)
	print campus_condos_column_c
	#get condos title
	for x,y in zip(campus_condos_column_c,condos_unit):
		campus_title_string= x + " " + y
		campus_condos_title.append(campus_title_string)
	print "campus condos title",campus_condos_title
	print len(campus_condos_title)
	#get campus condos rent per bedroom
	for x,y in zip(condos_rent,condos_bedroom):
		condos_rent_per_bedroom_value=x/y
		condos_rent_per_bedroom.append(condos_rent_per_bedroom_value)
	print "condos rent per bedroom",condos_rent_per_bedroom




	#------------------------------------------------------------------------------
	#append campus condos to main output stream
	status.extend(condos_status)
	print len(status)
	company.extend(campus_condos_company)
	print company
	print len(company)
	individual_identifier.extend(condos_identifier_individual)
	print individual_identifier
	print len(individual_identifier)
	master_identifier.extend(condos_master_identifier)
	print "master Identifier",master_identifier
	print "master_identifier" ,len(master_identifier)
	m.extend(condos_blank_cells)
	print m
	print len(m)
	title.extend(campus_condos_title)
	print title
	print "lenght of title at condos ",len(title)
	address.extend(condos_address)
	print address
	print len(address)
	unit_list.extend(condos_unit)
	print unit_list
	print len(unit_list)
	city.extend(condos_default_city)
	print city
	print "city at condos ",len(city)
	state.extend(condos_default_state)
	print state
	print "state at condos", len(state)
	zip_code.extend(condos_blank_cells)
	print zip_code
	print len(zip_code)
	square_feet.extend(condos_blank_cells)
	print square_feet
	print len(square_feet)
	forms.extend(condos_forms_default)
	print forms
	print len(forms)
	parking_space.extend(condos_blank_cells)
	print parking_space
	print len(parking_space)
	area.extend(condos_blank_cells)
	print area
	print len(area)
	property_type.extend(condos_blank_cells)
	print property_type
	print len(property_type)
	bedroom.extend(condos_bedroom)
	print bedroom
	print len(bedroom)
	bathroom.extend(condos_bathroom)
	print bathroom
	print len(bathroom)
	monthly_rent.extend(condos_blank_cells)
	print monthly_rent
	print len(monthly_rent)
	price_per_bedroom.extend(condos_rent_per_bedroom)
	print price_per_bedroom
	print len(price_per_bedroom)
	available.extend(condos_movein)
	print available
	print len(available)
	paid_utilities.extend(condos_blank_cells)
	print paid_utilities
	print len(paid_utilities)
	pets.extend(condos_default_pets)
	print pets
	print len(pets)
	phone.extend(condos_phone)
	print phone
	print len(phone)
	description.extend(condos_description)
	print description
	print len(description)
	gate_code.extend(condos_blank_cells)
	print gate_code
	print len(gate_code)
	key_number.extend(condos_blank_cells)
	print key_number
	print len(key_number)
	commission.extend(condos_commission)
	bonus.extend(condos_blank_cells)
	email.extend(condos_blank_cells)
	print email
	print len(email)
	depo_and_first_month_rent.extend(condos_deposit_rent_paidto)
	print condos_deposit_rent_paidto
	#----------------------------------------------------------------------------------
	#start premier realities
	#-----------------------------------------------------------------------------------
	#premier defaults
	premier_blank_cells=['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	print "lenght premier_blank cells",len(premier_blank_cells)
	premier_monthly_rent=[]
	premier_price_per_bedroom=[]
	premier_property_type=[]
	premier_unit=[]
	premier_address=[]
	premier_bed=[]
	premier_bathroom=[]
	premier_available=[]
	premier_phone=[]
	premier_description=[]
	premier_commission=[]
	premier_bonus=[]
	premier_status=[]
	premier_company=[]
	premier_state=[]
	premier_city=[]
	premier_first_month_rent=[]
	premier_forms=[]
	premier_individual_identifier=[]
	premier_master_identifier=[]
	premier_key_number=[]
	for n in range(7,54):
		premier_company_string="PREMIER REALTY"
		premier_company.append(premier_company_string)
	print "premier_company",premier_company
	print "premier company len",len(premier_company)
	for n in range(7,54):
		premier_forms_string="TAA + Addenda"
		premier_forms.append(premier_forms_string)
	print "premier_forms",premier_forms
	len(premier_forms)
	for n in range(7,54):
		premier_state_string="TX"
		premier_state.append(premier_state_string)
	print "premier_state",premier_state
	len(premier_state)
	for n in range(7,54):
		premier_city_string="Austin"
		premier_city.append(premier_city_string)
	print "premier_city",premier_city
	len(premier_city)

	for n in range (7,54):
		premier_rent=str(premier_sheet.cell_value(n,0))
		premier_monthly_rent.append(premier_rent)
	print "premier rent",premier_monthly_rent
	print len(premier_monthly_rent)
	for n in range (7,54):
		premier_rent_bed=str(premier_sheet.cell_value(n,1))
		premier_price_per_bedroom.append(premier_rent_bed)
	print "premier_price_per_bedroom",premier_price_per_bedroom 
	print len(premier_price_per_bedroom)
	for n in range (7,54):
		premier_property_type_string=str(premier_sheet.cell_value(n,2))
		premier_property_type.append(premier_property_type_string)
	print "premier property type",premier_property_type
	print len(premier_property_type)
	for n in range (7,54):
		premier_unit_string=str(premier_sheet.cell_value(n,3))
		premier_unit.append(premier_unit_string)
	print "premier unit",premier_unit
	print len(premier_unit)
	for n in range (7,54):
		premier_address_string=str(premier_sheet.cell_value(n,4))
		premier_address.append(premier_address_string)
	print "premier address",premier_address
	print len(premier_address)
	for n in range (7,54):
		premier_bed_string=str(premier_sheet.cell_value(n,5))
		premier_bed.append(premier_bed_string)
	print "premier bed",premier_bed
	print len(premier_bed)
	for n in range (7,54):
		premier_bathroom_string=str(premier_sheet.cell_value(n,6))
		premier_bathroom.append(premier_bathroom_string)
	print "premier bathroom",premier_bathroom
	print len(premier_bathroom)
	premier_available_string1="August 2014"
	premier_available.append(premier_available_string1)
	for n in range (8,18):
		premier_available_string=str(datetime.datetime(*xlrd.xldate_as_tuple(premier_sheet.cell_value(n,7),book_premier.datemode)))[:10]
		premier_available.append(premier_available_string)
	premier_available_string2=str(premier_sheet.cell_value(18,7))
	premier_available.append(premier_available_string2)
	for  n in range(19,54):
		premier_available_string3=str(premier_sheet.cell_value(n,7))
		premier_available.append(premier_available_string3)
	print "premier available",premier_available
	print len(premier_available)
	for n in range (7,54):
		premier_phone_string=str(premier_sheet.cell_value(n,9))
		premier_phone.append(premier_phone_string)
	print "premier phone",premier_phone
	print len(premier_phone)
	for n in range (7,54):
		premier_description_string=premier_sheet.cell_value(n,10).encode('utf-8')
		premier_description.append(premier_description_string)
	print "premier description",premier_description
	print len(premier_description)
	for n in range (7,54):
		premier_commission_string=str(premier_sheet.cell_value(n,15) *100)  + "%"
		premier_commission.append(premier_commission_string)
	print "premier commission",premier_commission
	print len(premier_commission)
	for n in range (7,54):
		premier_bonus_string=premier_sheet.cell_value(n,14)
		premier_bonus.append(premier_bonus_string)
	print "premier commission",premier_bonus
	print len(premier_bonus)
	#premier_first_month_rent
	for n in range (7,54):
		premier_first_month_rent_string=premier_sheet.cell_value(n,16)
		premier_first_month_rent.append(premier_first_month_rent_string)
	print "premier_first_month_rent",premier_first_month_rent
	print len(premier_first_month_rent)

	#premier status
	
	for n in range(7,54):
		premier_status_string="available"
		premier_status.append(premier_status_string)
	premier_status[8]="Leased"
	premier_status[10]="Leased"
	premier_status[21]="Leased"
	premier_status[33]="Leased"	
	premier_status[45]="Leased"
	premier_status[46]="Leased"
	print "premier status",premier_status
	print len(premier_status)
	#get premier realty unique individual identifier
	for x,y in zip(premier_address,premier_unit):
		premier_individual_identifier_string= x + " " + y
		premier_individual_identifier.append(premier_individual_identifier_string)
	print "premier individual identifier",premier_individual_identifier
	print len(premier_individual_identifier)
	#get premier master identifier
	for x,y in zip(premier_company,premier_individual_identifier):
		premier_master_identifier_string= x + " " + y
		premier_master_identifier.append(premier_master_identifier_string)
	print "premier master identifier",premier_master_identifier
	print len(premier_master_identifier)
	#get premier key number
	for n in range (7,54):
		premier_key_number_string=str(premier_sheet.cell_value(n,8))
		premier_key_number.append(premier_key_number_string)
	print "premier key number",premier_key_number 
	print len(premier_key_number)


		


	#-------------------------------------------------------------------------------------
	#append premier to output stream

	status.extend(premier_status)
	company.extend(premier_company)
	individual_identifier.extend(premier_individual_identifier)
	master_identifier.extend(premier_master_identifier)
	m.extend(premier_blank_cells)
	title.extend(premier_blank_cells)
	address.extend(premier_address)
	unit_list.extend(premier_unit)
	city.extend(premier_city)
	print "city at premier",len(city)
	state.extend(premier_state)
	print "state at premier",len(state)
	zip_code.extend(premier_blank_cells)
	square_feet.extend(premier_blank_cells)
	forms.extend(premier_forms)
	parking_space.extend(premier_blank_cells)
	area.extend(premier_blank_cells)
	property_type.extend(premier_property_type)
	bedroom.extend(premier_bed)
	bathroom.extend(premier_bathroom)
	print "bathroom at premier",len(bathroom)
	monthly_rent.extend(premier_monthly_rent)
	price_per_bedroom.extend(premier_price_per_bedroom)
	available.extend(premier_available)
	paid_utilities.extend(premier_blank_cells)
	pets.extend(premier_blank_cells)
	phone.extend(premier_phone)
	print "phone at premier",len(phone)
	description.extend(premier_description)
	gate_code.extend(premier_blank_cells)
	key_number.extend(premier_key_number)
	email.extend(premier_blank_cells)
	bonus.extend(premier_bonus)
	commission.extend(premier_commission)
	depo_and_first_month_rent.extend(premier_first_month_rent)

	#-----------------------------------------------------------------------------------
	# start austin centric
	#austin defaults
	austin_city=['Austin','Austin','Austin','Austin','Austin','Austin','Austin']
	austin_state=['TX','TX','TX','TX','TX','TX','TX']
	austin_forms=['TAR','TAR','TAR','TAR','TAR','TAR','TAR']
	austin_company=['Austin Centric','Austin Centric','Austin Centric','Austin Centric','Austin Centric','Austin Centric','Austin Centric']
	austin_rent=[]
	austin_type=[]
	austin_address=[]
	austin_bed=[]
	austin_bathroom=[]
	austin_description=[]
	austin_phone=[]
	austin_area=[]
	austin_available=[]
	austin_first_month_rent=[]
	austin_commission=[]
	austin_bonus=[]
	austin_key_number=[]
	austin_centric_status=[]
	austin_centric_unit=[]
	austin_centric_individual_identifier=[]
	austin_centric_master_identifier=[]
	#----------------------------------------------------------------------------------
	#get austin rent
	for n in range(8,15):
		austin_rent_string=str(austin_centric_sheet.cell_value(n,0))
		austin_rent.append(austin_rent_string)
	print "austin rent",austin_rent
	print len(austin_rent)
	for n in range(8,15):
		austin_type_string=str(austin_centric_sheet.cell_value(n,1))
		austin_type_string_stripped=austin_type_string[:6]
		austin_type.append(austin_type_string_stripped)
	print "austin type",austin_type
	print len(austin_type)
	#get austin address
	for n in range(8,15):
		austin_address_string=str(austin_centric_sheet.cell_value(n,3))
		austin_address.append(austin_address_string)
	print "austin address",austin_address
	print len(austin_address)
	#get austin bed
	for n in range(8,15):
		austin_bed_string=str(austin_centric_sheet.cell_value(n,4))
		austin_bed.append(austin_bed_string)
	print "austin bed",austin_bed
	print len(austin_bed)
	for n in range(8,15):
		austin_bathroom_string=str(austin_centric_sheet.cell_value(n,5))
		austin_bathroom.append(austin_bathroom_string)
	print "austin bathroom",austin_bathroom
	print len(austin_bathroom)
	#-----------------------------------------------------------------------------------
	#get austin description
	for n in range(8,15):
		austin_description_string=str(austin_centric_sheet.cell_value(n,9))
		austin_description.append(austin_description_string)
	print "austin_description",austin_description
	print len(austin_description)
	# get austin phone
	for n in range(8,15):
		austin_phone_string=str(austin_centric_sheet.cell_value(n,8))
		austin_phone.append(austin_phone_string)
	print "austin_phone",austin_phone
	print len(austin_phone)
	#get austin area
	for n in range(8,15):
		austin_area_string=str(austin_centric_sheet.cell_value(n,1))
		austin_area_string_stripped=austin_area_string[6:]
		austin_area.append(austin_area_string_stripped)
	print "austin area",austin_area
	#get austin available
	for n in range(8,11):
		austin_available_string=str(austin_centric_sheet.cell_value(n,6))
		austin_available.append(austin_available_string)
	for n in range(11,13):
		austin_available2=str(datetime.datetime(*xlrd.xldate_as_tuple(austin_centric_sheet.cell_value(n,6),book_austin_centric.datemode)))[:10]
		austin_available.append(austin_available2)
	austin_available3=str(austin_centric_sheet.cell_value(13,6))
	austin_available.append(austin_available3)
	austin_available4=str(datetime.datetime(*xlrd.xldate_as_tuple(austin_centric_sheet.cell_value(14,6),book_austin_centric.datemode)))[:10]
	austin_available.append(austin_available4)
	print "austin available",austin_available
	print len(austin_available)
	#austin commission
	for n in range(8,15):
		austin_commission_string="40%"
		austin_commission.append(austin_commission_string)
	print "austin_phone",austin_commission
	print len(austin_commission)
	for n in range(8,15):
		austin_bonus_string=str(austin_centric_sheet.cell_value(n,11))
		austin_bonus.append(austin_bonus_string)
	print "austin_bonus",austin_bonus
	print len(austin_bonus)
	#austin key_number
	for n in range(8,15):
		austin_key_number_string=str(austin_centric_sheet.cell_value(n,7))
		austin_key_number.append(austin_key_number_string)
	print "austin_bonus",austin_key_number
	print len(austin_key_number)
	#get austin centric status
	for n in range(8,15):
		austin_centric_unit_string=str(austin_centric_sheet.cell_value(n,2))
		austin_centric_unit.append(austin_centric_unit_string)
	print "austin_centric unit",austin_centric_unit
	print len(austin_centric_unit)
	for n in xrange(1,8):
		austin_centric_status_string="Available"
		austin_centric_status.append(austin_centric_status_string)
	austin_centric_status[4]='Leased'
	austin_centric_status[5]='Leased'
	print "austin centric status",austin_centric_status
	print len(austin_centric_status)
	#get austin_centric unit

	#get austin individual identifier
	for x,y in zip(austin_address,austin_centric_unit):
		austin_centric_individual_identifier_string= x + " " + y
		austin_centric_individual_identifier.append(austin_centric_individual_identifier_string)
	print "austin centric individual identifier ",austin_centric_individual_identifier
	print len(austin_centric_individual_identifier)
	#get austincentric master identifier
	for x,y in zip(austin_company,austin_centric_individual_identifier):
		austin_centric_master_identifier_string=x + " " + y
		austin_centric_master_identifier.append(austin_centric_master_identifier_string)
	print "austin centric master identifier",austin_centric_master_identifier
	print len(austin_centric_master_identifier)

	#--------------------------------------------------------------------------------------
	#-------------------------------------------------------------------------------------
	

	for n in range(1,8):
		austin_first_month_rent_string="Austin Centric Realty | $50 App Fee, $50 Guarantor, Deposit = 1 Month's Rent All Checks Payable to Austin Centric Realty"
		austin_first_month_rent.append(austin_first_month_rent_string)
	print "austin_first_month_rent",austin_first_month_rent
	print len (austin_first_month_rent)		
	austin_blank_cells=['','','','','','','']
	#append austin to main output stream
	status.extend(austin_centric_status)
	company.extend(austin_company)
	print company
	individual_identifier.extend(austin_centric_master_identifier)
	master_identifier.extend(austin_centric_master_identifier)
	m.extend(austin_blank_cells)
	title.extend(austin_blank_cells)
	print "length of title at austin ",len(title)
	address.extend(austin_address)
	unit_list.extend(austin_centric_unit)
	city.extend(austin_city)
	print "city at austin",len(city)

	state.extend(austin_state)
	print "state at austin",len(state)
	zip_code.extend(austin_blank_cells)
	square_feet.extend(austin_blank_cells)
	forms.extend(austin_forms)
	parking_space.extend(austin_blank_cells)
	area.extend(austin_blank_cells)
	property_type.extend(austin_type)
	print "length ofproperty_type ",len(property_type)
	bedroom.extend(austin_bed)
	bathroom.extend(austin_bathroom)
	monthly_rent.extend(austin_rent)
	price_per_bedroom.extend(austin_blank_cells)
	available.extend(austin_available)
	paid_utilities.extend(austin_blank_cells)
	pets.extend(austin_blank_cells)
	phone.extend(austin_phone)
	print "length of phone ",len(phone)
	description.extend(austin_description)
	gate_code.extend(austin_blank_cells)
	key_number.extend(austin_key_number)
	print "length of key_number ",len(key_number)
	email.extend(austin_blank_cells)
	bonus.extend(austin_bonus)
	commission.extend(austin_commission)
	depo_and_first_month_rent.extend(austin_first_month_rent)
	#----------------------------------------------------------------------------------
	#start university realty
	#university defaults
	university_state=[]
	university_city=[]
	university_blank_cells=[]
	university_forms=[]
	university_company=[]
	university_first_month_rent=[]
	for x in range(1,95):
		university_city_string="Austin"
		university_city.append(university_city_string)
	print "university_city", university_city
	print len(university_city)
	for x in range(1,95):
		university_state_string="TX"
		university_state.append(university_state_string)
	print "university_state", university_state
	print len(university_city)
	for x in range(1,95):
		university_blank_cells_string=' '
		university_blank_cells.append(university_blank_cells_string)
	print "university_blank_cells", university_blank_cells
	print len(university_blank_cells)
	for x in range(1,95):
		university_forms_string="TAA Addenda"
		university_forms.append(university_forms_string)
	print "university_forms", university_forms
	print len(university_forms)
	for x in range(1,95):
		university_company_string="University Realty"
		university_company.append(university_company_string)
	print "university_company", university_company
	print len(university_company)
	for x in range(1,95):
		university_first_month_rent_string="University Realty | $75 App Fees, Deposit = 1st Month's Rent"
		university_first_month_rent.append(university_first_month_rent_string)
	print "university_first_month_rent", university_first_month_rent
	print len(university_first_month_rent)
	
	university_zip=[]
	university_address=[]
	university_unit=[]
	university_rent=[]
	university_phone=[]
	university_description=[]
	university_available=[]
	university_property=[]
	university_commission=[]
	university_title=[]
	university_individual_identifier=[]
	university_master_identifier=[]
	university_bedroom=[]
	university_size=[]
	university_bathroom=[]
	university_price_per_bed=[]
	university_bedroom_number=[]
	#university realty zip code
	for n in range(12,21):
		university_zip_string=str(university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string)
	for n in range(23,25):
		university_zip_string2=str(university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string2)
	for n in range(26,31):
		university_zip_string3=str(university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string3)
	for n in range(33,36):
		university_zip_string4=str(university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string4)
	for n in range(38,73):
		university_zip_string5=str(university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string5)
	for n in range(75,82):
		university_zip_string10=float( university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string10)
	for n in range(84,109):
		university_zip_string6=str(university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string6)
	for n in range(111,113):
		university_zip_string7=str(university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string7)
	university_zip_string8=str(university_sheet.cell_value(115,0))
	university_zip.append(university_zip_string8)
	for n in range(118,123):
		university_zip_string9=str(university_sheet.cell_value(n,0))
		university_zip.append(university_zip_string9)
	print "university_zip",university_zip
	print len(university_zip)
	#--------------------
	#university address
	for n in range(12,21):
		university_address_string=str(university_sheet.cell_value(n,2))
		university_address.append(university_address_string)
	for n in range(23,25):
		university_address_string2=str(university_sheet.cell_value(n,2))
		university_address.append(university_address_string2)
	for n in range(26,31):
		university_address_string3=str(university_sheet.cell_value(n,2))
		university_address.append(university_address_string3)
	for n in range(33,36):
		university_address_string4=str(university_sheet.cell_value(n,2))
		university_address.append(university_address_string4)
	for n in range(38,73):
		university_address_string5=str(university_sheet.cell_value(n,2))
		university_address.append(university_address_string5)
	for n in range(75,82):
		university_address_string10=str( university_sheet.cell_value(n,2))
		university_address.append(university_address_string10)
	for n in range(84,109):
		university_address_string6=str(university_sheet.cell_value(n,2))
		university_address.append(university_address_string6)
	for n in range(111,113):
		university_address_string7=str(university_sheet.cell_value(n,2))
		university_address.append(university_address_string7)
	university_address_string8=str(university_sheet.cell_value(115,2))
	university_address.append(university_address_string8)
	for n in range(118,123):
		university_address_string9=str(university_sheet.cell_value(n,2))
		university_address.append(university_address_string9)
	print "university_address",university_address
	print len(university_address)
	#get university unit
	for n in range(12,21):
		university_unit_string=str(university_sheet.cell_value(n,3))
		university_unit.append(university_unit_string)
	for n in range(23,25):
		university_unit_string2=str(university_sheet.cell_value(n,3))
		university_unit.append(university_unit_string2)
	for n in range(26,31):
		university_unit_string3=str(university_sheet.cell_value(n,3))
		university_unit.append(university_unit_string3)
	for n in range(33,36):
		university_unit_string4=str(university_sheet.cell_value(n,3))
		university_unit.append(university_unit_string4)
	for n in range(38,73):
		university_unit_string5=str(university_sheet.cell_value(n,3))
		university_unit.append(university_unit_string5)
	for n in range(75,82):
			university_unit_string10=str( university_sheet.cell_value(n,3))
			university_unit.append(university_unit_string10)
	for n in range(84,109):
		university_unit_string6=str(university_sheet.cell_value(n,3))
		university_unit.append(university_unit_string6)
	for n in range(111,113):
		university_unit_string7=str(university_sheet.cell_value(n,3))
		university_unit.append(university_unit_string7)
	university_unit_string8=str(university_sheet.cell_value(115,3))
	university_unit.append(university_unit_string8)
	for n in range(118,123):
		university_unit_string9=str(university_sheet.cell_value(n,3))
		university_unit.append(university_unit_string9)
	print "university_unit",university_unit
	print len(university_unit)
	#get university rent
	for n in range(12,21):
		university_rent_string=float("%0.15g" % university_sheet.cell_value(n,4))
		university_rent.append(university_rent_string)
	for n in range(23,25):
		university_rent_string2=float(university_sheet.cell_value(n,4))
		university_rent.append(university_rent_string2)
	for n in range(26,31):
		university_rent_string3=float(university_sheet.cell_value(n,4))
		university_rent.append(university_rent_string3)
	for n in range(33,36):
		university_rent_string4=university_sheet.cell_value(n,4)
		university_rent.append(university_rent_string4)
	for n in range(38,73):
		university_rent_string5=float( university_sheet.cell_value(n,4))
		university_rent.append(university_rent_string5)
	for n in range(75,82):
		university_rent_string10=float( university_sheet.cell_value(n,4))
		university_rent.append(university_rent_string10)
	for n in range(84,109):
		university_rent_string6=float(university_sheet.cell_value(n,4))
		university_rent.append(university_rent_string6)
	for n in range(111,113):
		university_rent_string7=float(university_sheet.cell_value(n,4))
		university_rent.append(university_rent_string7)
	university_rent_string8=float(university_sheet.cell_value(115,4))
	university_rent.append(university_rent_string8)
	for n in range(118,123):
		university_rent_string9=float(university_sheet.cell_value(n,4))
		university_rent.append(university_rent_string9)
	print "university_rent",university_rent
	print len(university_rent)
	# get university phone
	for n in range(12,21):
		university_phone_string=str(university_sheet.cell_value(n,6))
		university_phone.append(university_phone_string)
	for n in range(23,25):
		university_phone_string2=str(university_sheet.cell_value(n,6))
		university_phone.append(university_phone_string2)
	for n in range(26,31):
		university_phone_string3=str(university_sheet.cell_value(n,6))
		university_phone.append(university_phone_string3)
	for n in range(33,36):
		university_phone_string4=str(university_sheet.cell_value(n,6))
		university_phone.append(university_phone_string4)
	for n in range(38,73):
		university_phone_string5=str(university_sheet.cell_value(n,6))
		university_phone.append(university_phone_string5)
	for n in range(75,82):
			university_phone_string10=str( university_sheet.cell_value(n,6))
			university_phone.append(university_phone_string10)
	for n in range(84,109):
		university_phone_string6=str(university_sheet.cell_value(n,6))
		university_phone.append(university_phone_string6)
	for n in range(111,113):
		university_phone_string7=str(university_sheet.cell_value(n,6))
		university_phone.append(university_phone_string7)
	university_phone_string8=str(university_sheet.cell_value(115,6))
	university_phone.append(university_phone_string8)
	for n in range(118,123):
		university_phone_string9=str(university_sheet.cell_value(n,6))
		university_phone.append(university_phone_string9)
	print "university_phone",university_phone
	print len(university_phone)
	#university description
	for n in range(12,21):
		university_description_string=str(university_sheet.cell_value(n,9))
		university_description.append(university_description_string)
	for n in range(23,25):
		university_description_string2=str(university_sheet.cell_value(n,9))
		university_description.append(university_description_string2)
	for n in range(26,31):
		university_description_string3=str(university_sheet.cell_value(n,9))
		university_description.append(university_description_string3)
	for n in range(33,36):
		university_description_string4=str(university_sheet.cell_value(n,9))
		university_description.append(university_description_string4)
	for n in range(38,73):
		university_description_string5=str(university_sheet.cell_value(n,9))
		university_description.append(university_description_string5)
	for n in range(75,82):
			university_description_string10=str( university_sheet.cell_value(n,9))
			university_description.append(university_description_string10)
	for n in range(84,109):
		university_description_string6=str(university_sheet.cell_value(n,9))
		university_description.append(university_description_string6)
	for n in range(111,113):
		university_description_string7=str(university_sheet.cell_value(n,9))
		university_description.append(university_description_string7)
	university_description_string8=str(university_sheet.cell_value(115,9))
	university_description.append(university_description_string8)
	for n in range(118,123):
		university_description_string9=str(university_sheet.cell_value(n,9))
		university_description.append(university_description_string9)
	print "university_description",university_description
	print len(university_description)
	#university available
	for n in range(12,21):
		university_available_string=str(datetime.datetime(*xlrd.xldate_as_tuple(university_sheet.cell_value(n,7),book_university.datemode)))[:10]
		university_available.append(university_available_string)
	for n in range(23,25):
		university_available_string2=str(datetime.datetime(*xlrd.xldate_as_tuple(university_sheet.cell_value(n,7),book_university.datemode)))[:10]
		university_available.append(university_available_string2)
	for n in range(26,31):
		university_available_string3=str(datetime.datetime(*xlrd.xldate_as_tuple(university_sheet.cell_value(n,7),book_university.datemode)))[:10]
		university_available.append(university_available_string3)
	for n in range(33,36):
		university_available_string4=str(datetime.datetime(*xlrd.xldate_as_tuple(university_sheet.cell_value(n,7),book_university.datemode)))[:10]
		university_available.append(university_available_string4)
	for n in range(38,73):
		university_available_string5=str(university_sheet.cell_value(n,7))
		university_available.append(university_available_string5)
	for n in range(75,82):
		university_available_string10=str(university_sheet.cell_value(n,7))
		university_available.append(university_available_string10)
	for n in range(84,109):
		university_available_string6=str(datetime.datetime(*xlrd.xldate_as_tuple(university_sheet.cell_value(n,7),book_university.datemode)))[:10]
		university_available.append(university_available_string6)
	for n in range(111,113):
		university_available_string7=str(datetime.datetime(*xlrd.xldate_as_tuple(university_sheet.cell_value(n,7),book_university.datemode)))[:10]
		university_available.append(university_available_string7)
	university_available_string8=str(datetime.datetime(*xlrd.xldate_as_tuple(university_sheet.cell_value(n,7),book_university.datemode)))[:10]
	university_available.append(university_available_string8)
	for n in range(118,123):
		university_available_string9=str(datetime.datetime(*xlrd.xldate_as_tuple(university_sheet.cell_value(n,7),book_university.datemode)))[:10]
		university_available.append(university_available_string9)
	print "university_available",university_available
	print len(university_available)
	#get university property
	for n in range(12,21):
		university_property_string=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string)
	for n in range(23,25):
		university_property_string2=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string2)
	for n in range(26,31):
		university_property_string3=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string3)
	for n in range(33,36):
		university_property_string4=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string4)
	for n in range(38,73):
		university_property_string5=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string5)
	for n in range(75,82):
		university_property_string10=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string10)
	for n in range(84,109):
		university_property_string6=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string6)
	for n in range(111,113):
		university_property_string7=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string7)
	university_property_string8=str(university_sheet.cell_value(115,1))
	university_property.append(university_property_string8)
	for n in range(118,123):
		university_property_string9=str(university_sheet.cell_value(n,1))
		university_property.append(university_property_string9)
	print "university_property",university_property
	print len(university_property)
	#get university size
	for n in range(12,21):
		university_size_string=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string)
	for n in range(23,25):
		university_size_string2=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string2)
	for n in range(26,31):
		university_size_string3=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string3)
	for n in range(33,36):
		university_size_string4=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string4)
	for n in range(38,73):
		university_size_string5=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string5)
	for n in range(75,82):
		university_size_string10=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string10)
	for n in range(84,109):
		university_size_string6=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string6)
	for n in range(111,113):
		university_size_string7=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string7)
	university_size_string8=str(university_sheet.cell_value(115,5))
	university_size.append(university_size_string8)
	for n in range(118,123):
		university_size_string9=str(university_sheet.cell_value(n,5))
		university_size.append(university_size_string9)
	print "university_size",university_size
	print len(university_size)
	#get university bedroom
	for x in university_size:
		if x=="Room" or x=="eff" or x=="Eff":
			x=0
		else:
			x=x[:1]
		university_bedroom.append(x)
	print "university bedroom",university_bedroom
	print len(university_bedroom)
	#get university bathroom
	for x in university_size:
		if x=="Room" or x=="eff" or x=="Eff":
			x=1
		else:
			x=x[2:]
		university_bathroom.append(x)
	print "university bathroom",university_bathroom
	print len(university_bathroom)
	# get univer price per bedroom
	
	for x in university_bedroom:
		if x=="1" or x==0:
			x=int(1)
		elif x=="2":
			x=int(2)
		elif x=="3":
			x=int(3)
		elif x=="4":
			x=int(4)
		elif x=="5":
			x=int(5)
		university_bedroom_number.append(x)
	print "university_bedroom_number",university_bedroom_number
	len(university_bedroom_number)
	for x,y in zip(university_rent,university_bedroom_number):
		monthly_rent_value=x/y
		university_price_per_bed.append(monthly_rent_value)
	print "university price per bed",university_price_per_bed
	print len(university_price_per_bed)




	#get university commission
	for n in range(1,95):
		university_commission_string="40%"
		university_commission.append(university_commission_string)
	print "university_commission",university_commission
	print len(university_commission)
	#get university title
	for x , z in zip(university_property,university_unit):
		university_title_string  =  x + " " + z
		university_title.append(university_title_string)
	print "university_title",university_title
	print len(university_title)
	# university individual identifier
	for x , z in zip(university_address,university_unit):
		university_individual_identifier_string  =  x + " " + z
		university_individual_identifier.append(university_individual_identifier_string)
	print "university_individual_identifier",university_individual_identifier
	print len(university_individual_identifier)
	#univeristy master identifier
	for y, x , z in zip(university_company,university_address,university_unit):
		university_master_identifier_string  =  y + " " + x + " " + z
		university_master_identifier.append(university_master_identifier_string)
	print "university_master_identifier",university_master_identifier
	print len(university_master_identifier)
	#get university status
	"""
	university_status=[]
	for x in range(1,95):
		status_string="Active"
		university_status.append(status_string)
	#mark leased
	status_indexes=[0,1,8,12,16,22,30,35,46,48,71,91,95,96]
	replacements=["Active","Active","Active","Active","Active","Active","Active","Active","Active","Active","Active","Active","Active","Active","Active"]
	for index in status_indexes:
		university_status[status_indexes[index]] = replacements[index]
	print "university_status",university_status
	print len(university_status)
"""




#append university realty to output stream
	status.extend(university_blank_cells)
	company.extend(university_company)
	individual_identifier.extend(university_individual_identifier)
	master_identifier.extend(university_master_identifier)
	m.extend(university_blank_cells)
	title.extend(university_title)
	print "length of title ",len(title)
	address.extend(university_address)
	print "the length of address",len(address)
	unit_list.extend(university_unit)
	city.extend(university_city)
	print "length of city at university",len(city)
	state.extend(university_state)
	print "length of state at university",len(state)
	zip_code.extend(university_zip)
	square_feet.extend(university_blank_cells)
	forms.extend(university_forms)
	parking_space.extend(university_blank_cells)
	area.extend(university_blank_cells)
	property_type.extend(university_property)
	print "the length ofproperty_type",len(property_type)
	bedroom.extend(university_bedroom)
	bathroom.extend(university_bathroom)
	monthly_rent.extend(university_rent)
	price_per_bedroom.extend(university_price_per_bed)
	available.extend(university_available)
	paid_utilities.extend(university_blank_cells)
	pets.extend(university_blank_cells)
	phone.extend(university_phone)
	print "the length ofphone",len(phone)
	description.extend(university_description)
	gate_code.extend(university_blank_cells)
	key_number.extend(university_blank_cells)
	email.extend(university_blank_cells)
	bonus.extend(university_blank_cells)
	commission.extend(university_commission)
	depo_and_first_month_rent.extend(university_first_month_rent)
	#start 900 WEST 23rd
	west_unit=[]
	west_rent=[]
	west_bedroom=[]
	west_phone=[]
	west_available=[]
	west_address=[]
	west_identifier_master=[]
	west_parking_space=[]
	west_area=[]
	west_type=[]
	west_blank_cells=[]
	west_city=[]
	west_state=[]
	west_company=[]
	west_commission=[]
	west_bonus=[]
	west_identifier_individual=[]
	west_first_month_rent=[]
	west_email=[]
	west_gate_code=[]
	west_key_number=[]
	west_paid_utilities=[]
	west_price_per_bedroom=[]
	west_forms=[]
	west_bathroom=[]
	west_pets=[]
	west_zip=[]
	west_square_feet=[]
	west_title=[]
	west_city=[]
	west_state=[]
	west_forms=[]
	
	
	#get unit
	for n in range(9,135):
		west_23rd_unit_string=str(west_23rd_sheet.cell_value(n,0))
		west_unit.append(west_23rd_unit_string)
	print "west_unit",west_unit
	print len(west_unit)
	#get rent
	for n in range(9,135):
		west_23rd_rent_string=str(west_23rd_sheet.cell_value(n,1))
		west_rent.append(west_23rd_rent_string)
	print "west_rent",west_rent
	print(west_rent)
	print len(west_rent)
	#west bedroom
	for x in range(9,135):
		west_23rd_bedroom_string=str(west_23rd_sheet.cell_value(x,0))
		west_23rd_bedroom_string_split=west_23rd_bedroom_string[6:8]
		west_23rd_bedroom_string_strip=west_23rd_bedroom_string_split[:1]
		west_bedroom.append(west_23rd_bedroom_string_strip)
	print "west_bedroom",west_bedroom
	print len(west_bedroom)
	#west phone
	for n in range(9,135):
		west_23rd_phone_string=str(west_23rd_sheet.cell_value(n,4))
		west_phone.append(west_23rd_phone_string)
	print "west_phone",west_phone
	print len(west_phone)
	#west available
	for n in range(1,127):
		west_available_string="8/19/2014"
		west_available.append(west_available_string)
	print ("west_available"),west_available
	print len(west_available)
	#get west address
	for n in range(1,127):
		west_address_string="900 W 23rd"
		west_address.append(west_address_string)
	print "west_address",west_address
	print len(west_address)
	# get west identifier from master list
	for x,y in zip(west_address,west_unit):
		west_identifier_master_string= x +y
		if west_identifier_master_string=='900 W 23rd':
			west_identifier_master_string=" "
		west_identifier_master.append(west_identifier_master_string)
	print "west_identifier_master",west_identifier_master
	print len(west_identifier_master)
	#get west 900 23rd parking space
	for x in west_bedroom:
		if x=="2":
			parking_space_string="2 RSVD"
			west_parking_space.append(parking_space_string)
		elif x=="3":
			parking_space_string="2 RSVD 1 Unssigned"
			west_parking_space.append(parking_space_string)
		elif x=='':
			parking_space_string=" "
			west_parking_space.append(parking_space_string)
	print "west_parking_space",west_parking_space
	print len(west_parking_space)
	#get west 900 23rd type
	for x in xrange(1,127):
		west_type_string="Condo"
		west_type.append(west_type_string)
	print "west_type",west_type
	print len(west_type)
	#get west 900 23rd Area
	for x in range(1,127):
		west_area_string="WC"
		west_area.append(west_area_string)
	print "west area",west_area
	print len(west_area)
	# west 900 23rd blank cells
	for x in range(1,127):
		west_blank_cells_string=' '
		west_blank_cells.append(west_blank_cells_string)
	print "west_blank_cells",west_blank_cells
	print len(west_blank_cells)
	#get west bathroom
	for x in xrange(1,127):
		bathroom_number=2
		west_bathroom.append(bathroom_number)
	print "west_bathroom",west_bathroom
	print len(west_bathroom)
	#get west_commission
	for x in xrange(1,127):
		west_commission_string="50%"
		west_commission.append(west_commission_string)
	print "west commission",west_commission
	print len(west_commission)
	#get west gete code
	for x in xrange(1,127):
		west_gate_code_string="1275"
		west_gate_code.append(west_gate_code_string)
	print "west gate_code",west_gate_code
	print len(west_gate_code)
	#get west key number
	for x in xrange(1,127):
		west_key_number_string="MLS"
		west_key_number.append(west_gate_code_string)
	print "west key_number",west_key_number
	print len(west_key_number)
	#get west 900 23rd pets
	for x in xrange(1,127):
		west_pets_string="NO"
		west_pets.append(west_pets_string)
	print "west pets",west_pets
	print len(west_pets)
	#get west 900 2rd zip
	for x in xrange(1,127):
		west_zip_string="78705"
		west_zip.append(west_zip_string)
	print "west_zip",west_zip
	print len(west_zip)
	#get west 900 23rd paid utilities
	for x in xrange(1,127):
		west_paid_utilities_string="Trash and Pets"
		west_paid_utilities.append(west_paid_utilities_string)
	print "west_paid_utilities",west_paid_utilities
	print len(west_paid_utilities)
	for x in xrange(1,127):
		west_first_month_rent_string="Austin Investments | $50 App Fee to Austin Investments | Deposit=1 Month's Rent to White/Coffee LTD."
		west_first_month_rent.append(west_first_month_rent_string)
	print "west_first_month_rent",west_first_month_rent
	print len(west_first_month_rent)
	#get west 900 23rd square feet
	for x in range(9,135):
		west_23rd_square_feet_string=str(west_23rd_sheet.cell_value(x,0))[10:]
		west_square_feet.append(west_23rd_square_feet_string)
	print "west_square_feet",west_square_feet
	print len(west_square_feet)
	#west identifier indivdual
	west_identifier_individual.extend(west_unit)
	print "west_identifier_individual",west_identifier_individual
	print len(west_identifier_individual)
	#get west_company
	for x in xrange(1,127):
		west_company_string="900 West 23rd"
		west_company.append(west_company_string)
	print "west_company",west_company
	print len(west_company)
	# get west title
	for x,y in zip(west_address,west_unit):
		west_title_string= x + y
		if west_title_string=='900 W 23rd':
			west_title_string=" "
		west_title.append(west_title_string)
	print " west title",west_title
	print len(west_title)
	for x in xrange(1,127):
		west_city_string="Austin"
		west_city.append(west_city_string)
	print "west_city",west_city
	print len(west_city)
	for x in xrange(1,127):
		west_state_string="TX"
		west_state.append(west_state_string)
	print "west_state",west_state
	print len(west_state)
	#get west 900 23rd forms
	for x in range(1,127):
		west_forms_string="TAA"
		west_forms.append(west_forms_string)
	print "west forms",west_forms
	print len(west_forms)


	#append west 900 23rd to main output stream
	status.extend(west_blank_cells)
	print len(status)
	company.extend(west_company)
	print len(company)
	individual_identifier.extend(west_identifier_individual)
	print len(individual_identifier)
	master_identifier.extend(west_identifier_master)
	print len(master_identifier)
	m.extend(west_blank_cells)
	print len(m)
	title.extend(west_title)
	print len(title)
	address.extend(west_address)
	print len(address)
	unit_list.extend(west_unit)
	print len(unit_list)
	city.extend(west_city)
	print len(city)
	state.extend(west_state)
	print len(state)
	zip_code.extend(west_zip)
	print len(zip_code)
	square_feet.extend(west_square_feet)
	print len(square_feet)
	forms.extend(west_forms)
	print len(forms)
	parking_space.extend(west_parking_space)
	print len(parking_space)
	area.extend(west_area)
	print len(area)
	property_type.extend(west_type)
	print len(property_type)
	bedroom.extend(west_bedroom)
	print len(bedroom)
	bathroom.extend(west_bathroom)
	print len(bathroom)
	monthly_rent.extend(west_rent)
	print len(monthly_rent)
	price_per_bedroom.extend(west_blank_cells)
	print len(price_per_bedroom)
	available.extend(west_blank_cells)
	print len(available)
	paid_utilities.extend(west_paid_utilities)
	print len(paid_utilities)
	pets.extend(west_pets)
	print len(pets)
	phone.extend(west_phone)
	print len(phone)
	description.extend(west_blank_cells)
	print len(description)
	gate_code.extend(west_gate_code)
	print len(gate_code)
	key_number.extend(west_key_number)
	print len(key_number)
	email.extend(west_blank_cells)
	print len(email)
	bonus.extend(west_blank_cells)
	print len(bonus)
	commission.extend(west_commission)
	print len(commission)
	depo_and_first_month_rent.extend(west_first_month_rent)
	print len(depo_and_first_month_rent)
	

	






	

		










	






	#------------------------------------------------------------------------------------
	# call output object and pass it parameters
	dumpDatatoMasterFile(status,company,individual_identifier,master_identifier,m,title,address,
	unit_list,city,state,zip_code,square_feet,
	forms,parking_space,area,
	property_type,bedroom,bathroom,monthly_rent,
	price_per_bedroom,available,paid_utilities,pets,
	phone,description,gate_code,key_number,
	email,commission,bonus,depo_and_first_month_rent)
def dumpDatatoMasterFile(status,company,individual_identifier,master_identifier,m,title,address,
		unit_list,city,state,zip_code,square_feet,
		forms,parking_space,area,
		property_type,bedroom,bathroom,monthly_rent,
		price_per_bedroom,available,paid_utilities,pets,
		phone,description,gate_code,key_number,
		email,commission,bonus,depo_and_first_month_rent):

	with open('Master_List.csv', 'wb') as f:
		writer = csv.writer(f)
		writer.writerows(izip(status,company,individual_identifier,master_identifier,m,title,address,
		unit_list,city,state,zip_code,square_feet,
		forms,parking_space,area,
		property_type,bedroom,bathroom,monthly_rent,
		price_per_bedroom,available,paid_utilities,pets,
		phone,gate_code,key_number,
		email,commission,bonus,depo_and_first_month_rent,description,))
	csv.Error()
getFormatChayslistdata()