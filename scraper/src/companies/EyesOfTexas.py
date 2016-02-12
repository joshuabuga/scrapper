from BaseCompanyScrapper import BaseCompanyScrapper
from ..properties.EyesOfTexasProperty import  EyesOfTexasProperty
from ..lib.helpers import *
import urllib2, httplib, urllib
from bs4 import BeautifulSoup
class EyesOfTexas(BaseCompanyScrapper):
	name ='Eyes Of Texas'
	city ='Austin'
	state ='TX'

	
	def request_props(self):
		url = self.get_file_path(True, True)
		url = collection_to_str(url,'')

		self.current_response = urllib.urlopen(url)
		content = self.current_response.read()
		beautyContent = self.new_soup(content)
		src = beautyContent.find('iframe')['src']
		self.current_content = urllib.urlopen(src).read()
		return self.current_content


	def parse_soup(self, soup ):
		props_soup =  self.find_all_properties(soup)
		count = 1
		for prop_soup in props_soup:
			print '####################Property#####################\n'
			print self.parse_property(prop_soup)
			print '#################### End Property#####################\n\n\n'
	
		return []

	def parse_property(self, soup):
		rent_avail = soup.find('table', class_='InfoBox')
		rent = self.tag_value(rent_avail.find('td', { 'align' : 'left' }).find('span', class_='fielddisplay'))
		available = self.tag_value(rent_avail.find('td', { 'align' : 'right' }).find('span', class_='fielddisplay'))
		parent_td = rent_avail.parent
		rent_avail.string = ''
		count = 1
		address = ''
		unit = ''
		bedroom = ''
		for node in parent_td.find_all('span', class_='fielddisplay'):
			if count == 1:
				address = self.tag_value(node)
			elif count == 2:
				unit = self.tag_value(node)
			elif count == 3:
				bedroom = self.tag_value(node)
			count +=1

		return [rent, available, address, unit, bedroom]
	
	def tag_value(self, tag):
		return tag.get_text() if tag != None else ''

	def find_all_properties(self, soup):
		return soup.find_all('table', class_='SearchHomesList_Results')

	def new_soup(self, html = None):
		return BeautifulSoup(open('MACHO_Texas.html'))
	def new_property(self, property_data):
		prop = EyesOfTexasProperty(property_data, self)	
		return prop