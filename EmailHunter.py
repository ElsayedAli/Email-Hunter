# coding: utf-8

import requests
from   bs4 import BeautifulSoup
import re
class EmailHunter:
	"""docstring for EmailHunter"""
	def __init__(self):
		self.Auther  		= "Sayed A. Omar"
		self.version 		= "V0.1"
		self.emails_file	= open('emails.csv','a+')
		self.links_file     = open('links.csv','a+')
		self.links          = []
		self.emails         = []

	def load_links_file(self,file):
		return open(file,'r').read().split('\n')
		
	def get_page_content(self,url):
		return requests.get(url).text

	def get_links_from_page(self,url):
		self.links.append(url)
		for link in self.links:
			data 				= requests.get(link).text
			soup 				= BeautifulSoup(data,'html5lib')
			for a in soup.findAll('a'):
				new_link        = a.get('href')
				if new_link and new_link.startswith('http'):
					if new_link not in self.links:
						new_link = new_link.encode('utf-8').strip()
						print new_link
						self.links.append(new_link)
						self.links_file.write(new_link+'\n')
		return links

	def get_emails(self,text):
		regex  = re.compile(("([a-z0-9!#$%&'*+\/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+\/=?^_`"
		                "{|}~-]+)*(@|\sat\s)(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?(\.|"
		                "\sdot\s))+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"))
		emails = re.findall(regex, text)
		for email in emails:
			if email not in self.emails:
				self.emails_file.write(email[0]+'\n')
		    	self.emails.append(email[0])
if __name__ == '__main__':
	hunter = EmailHunter()
	#text   = hunter.get_page_content("https://elsayedali.github.io/")
	#text   = hunter.get_links_from_page("https://elsayedali.github.io/")
	#hunter.get_emails(text)
	#print hunter.load_links_file('links.csv')


