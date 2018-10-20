# Script for determining the electron density or temperature around the      
# globe using the IRI2012 model. 
# Inputs: stepsize, datetime, 
# temperature is checkbox 21 (temperature in Kelvin)
# density is checkbox 17 (density in m^-3)
# 3-h ap is checkbox 58
# Profiles (see results over these profiles from start to stop, ranges are 
# in square brackets)
# 1 - Height,km [ 60. - 2000.]
# 2 - Latitude, deg.[-90. - 90.]
# 3 - Longitude, deg.[0. - 360.]
# 4 - Year [1958-2019]
# 5 - Month [1-12]
# 6 - Day of month[1-31]
# 7 - Day of Year[1-365]
# 8 - Hour profile[0.-24.]

# Parameters for 300 km altitude, 1st Jan 2000 at 1200 UT. Profile over the
# longitudes of Earth starting from 0 to 360
height = 300
datetime = [2000, 1, 1, 12, 0, 0]
stepsize = 10

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import numpy as np

profile = 3
start = 0
stop = 360

lat_ran = range(-90,90+stepsize,stepsize)
lon_ran = range(start,stop+stepsize,stepsize)

N_e = np.zeros((len(lat_ran),len(lon_ran)))

stepsize = float(stepsize)
stop = float(stop)
start = float(start)
hour = datetime[3] + datetime[4]/60 + datetime[5]/3600

# URL for the cgi page that contains the data for extraction
url = 'https://omniweb.sci.gsfc.nasa.gov/cgi/vitmo/vitmo_model.cgi'

vars = [17, 21] # Output variables from the  17 - electron density, 21 - electron temperature

# List to hold density and temperature data at the end
den_temp_data = []

for var in vars:
	# List to hold the output data from the scraping
	ls_data = []
	for lat in lat_ran:
		# Values that are submitted to the servers with the POST request. This data
		# needs to be sent so that the correct html page is presented, ie the one we 
		# are interested in
		values = {'model':'iri_2012',
			'year':datetime[0],
			'month':datetime[1],
			'day':datetime[2],
			'time_flag':0,
			'hour':hour,
			'geo_flag':'0.',
			'latitude':lat,
			'longitude':start,
			'height':height,
			'profile':profile,
			'start':start,
			'stop':stop,
			'step':stepsize,
			'sun_n':'',
			'ion_n':'',
			'radio_f':'',
			'radio_f81':'',
			'htec_max':'',
			'ne_top':'0.',
			'imap':'0.',
			'ffof2':'0.',
			'ib0':2.,
			'probab':'0.',
			'ffoE':'0.',
			'dreg':'0.',
			'tset':'0.',
			'icomp':'0.',
			'nmf2':'0.',
			'hmf2':'0.',
			'user_nme':'0.',
			'user_hme':'0.',
			'format':0,
			'vars':var,
			'linestyle':'solid',
			'charsize':'',
			'symbol':2,
			'symsize':'',
			'yscale':'Linear',
			'xscale':'Linear',
			'imagex':640,
			'imagey':480}

		# Turning the values dict into a format that the cgi will understand
		POST_data = urllib.parse.urlencode(values)

		# Convert the format into ascii 
		POST_data = POST_data.encode('ascii')

		# Create a Request object that will be passed to create urlopen object
		req_post = urllib.request.Request(url,POST_data)

		# Send the POST request to the website and extract the html data
		with urllib.request.urlopen(req_post) as response:
			html_page = response.read()

		# Use BeautifulSoup to create a BeautifulSoup object out of the html data
		# obtained from the POST request
		soup_tree= BeautifulSoup(html_page, 'html.parser')
		# Extract only the data from the html page
		data_html = soup_tree.find('pre')
		# Turn the html data into a string
		raw_data_str = str(data_html.string)
		# Split the string up into a list of elements
		splt_data_str1 = raw_data_str.split('\n')[4:-1]

		# Turn the string data into float format 
		data_list = []
		for el in splt_data_str1:
			data_list.append(float(el))
		
		ls_data.append(data_list)
		data_list = None
	
	#Convert data to array
	ar_data = np.array(ls_data)
	den_temp_data.append(ar_data)
	
	
np.savetxt("N_e_data.csv",den_temp_data[0],delimiter=',')
np.savetxt("T_e_data.csv",den_temp_data[1],delimiter=',')