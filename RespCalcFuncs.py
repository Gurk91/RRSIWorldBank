from RRSIFuncs import non_dac_aid, country_prefs, Data, data_loader


country = None
year = 0
result = []

#General Comparisons: These are used in all 3 versions of the RRSI

nation = data_loader(country, year)

def UnemVsPerCap(nation):
	unem = nation.Unemployment()[1]
	return unem

print(country_prefs)
brazil = data_loader('Brazil', 2017)

