from ..lib.helpers import *
from bs4 import BeautifulSoup
import urllib, httplib
from BaseCompany import BaseCompany

class BaseCompanyScrapper(BaseCompany):

	soup = None
	current_response = None
	current_content = None
	connection  = None

	def get_connection(self):
		if self.connection == None:
			host = self.get_file_path(host = True)
			
			self.connection = httplib.HTTPConnection(host)
		return self.connection

	def get_response(self, params = [], method = 'POST', headers = {  "Content-type": "application/x-www-form-urlencoded"  }, url = None):
		url = self.get_file_path(url = True) if url == None else url
		conn = self.get_connection()
		conn.request(method, url, params, headers )
		self.current_response = conn.getresponse()
		
		return self.current_response

	def get_file_path(self, host = False, url = False ):
		if host == True and url == True:
			return self.file_path
		elif host == True and url == False:
			return self.file_path[0]
		elif url == True and host == False:
			return self.file_path[1]

	def extract_data(self):
		self.properties_data = self.parse_soup(self.get_soup())
		return self.properties_data

	def parse_soup(self, soup ):
		return []
	
	def get_soup(self):
		if self.soup == None:
			self.soup = self.new_soup()
		return self.soup

	def new_soup(self, html = None):
		html = self.request_props() if html == None else html
		return BeautifulSoup(html)

	def to_list(self):
		property_list = []
		for property_ in self.company_properties:
			property_list.append(property_.to_list())

		return property_list


	def request_props(self):
		return ''
