from pprint import pprint
import requests
import wbdata

class Data:
	"""docstring for Data"""
	def __init__(self, country, year_index):
		self.country = country
		self.year_index = year_index


	def GDPPerCapPPP(self):
		data = requests.get('http://api.worldbank.org/v2/country/{}/indicator/NY.GDP.PCAP.PP.CD?format=json'.format(self.country))
		ret_val = data.json()
		return ret_val[1][self.year_index]['value']

	def Unemployment(self):
		data = requests.get('http://api.worldbank.org/v2/country/{}/indicator/SL.UEM.TOTL.ZS?format=json'.format(self.country))
		ret_val = data.json()
		return ret_val[1][self.year_index]['value']

	def GDPGrowthRate(self):
		data = requests.get('http://api.worldbank.org/v2/country/{}/indicator/NY.GDP.MKTP.KD.ZG?format=json'.format(self.country))
		ret_val = data.json()
		return ret_val[1][self.year_index['value']]

	def PovertyRate(self):
		data = requests.get('http://api.worldbank.org/v2/country/{}/indicator/SI.POV.DDAY?format=json'.format(self.country))
		ret_val = data.json()
		return ret_val[1][self.year_index]['value']

#Need to include method for case where no data is available... preferably to output last available data

brazil = Data('USA', 1)
#print(brazil.PovertyRate())

data = requests.get('http://api.worldbank.org/v2/country/IND/indicator/SI.POV.DDAY?format=json')
ret_val = data.json()
print(ret_val[1][7])

print("Hello")

