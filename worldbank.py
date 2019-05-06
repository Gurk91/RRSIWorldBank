from pprint import pprint

import requests
import wbdata


BrazilData = requests.get('http://api.worldbank.org/v2/country/BRA/indicator/NY.GDP.PCAP.PP.CD?format=json')
Brazilper_cap = BrazilData.json()
print(Brazilper_cap[1][1]['value']) #the second index gives the year. 0 = 2018, 1 = 2017, 2 = 2016 and so on. 

'''
To get data from the world bank API, you start with: 'http://api.worldbank.org/v2/country/[3 LETTER COUNTRY CODE]/indicator/[INDICATOR CODE]?format=json'
You can get the indicator and country codes from the url of the data, for example: https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD
:) :P

'''





### MIT Dataset - This one is only for international trade ###

India_trade_data = requests.get('http://atlas.media.mit.edu/hs92/export/2015/ind/usa/show/')
raw_data = India_trade_data.json()
