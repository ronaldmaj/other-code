# Attempt at Python Morsels exercise - meetup_date
# Passed all tests

import datetime		

# Define days class to eliminate need for magic numbers in weedays
class days():

	def __init__(self):
		self.MONDAY = 0
		self.TUESDAY = 1
		self.WEDNESDAY = 2
		self.THURSDAY = 3
		self.FRIDAY = 4
		self.SATURDAY = 5
		self.SUNDAY = 6
		
		self.Monday = 0
		self.Tuesday = 1
		self.Wednesday = 2
		self.Thursday = 3
		self.Friday = 4
		self.Saturday = 5
		self.Sunday = 6

# Create Weekday object:
Weekday = days()
		
def meetup_date(year, month, nth=4, weekday=3):
	# Take the year and month variables and figure out what is the datetime
	# of the 4th Thursday of that month.
	# Mon - 0, Tues - 1, Wed - 2, Thurs - 3, Fri - 4, Sat - 5, Sun - 6 

	
	# Create list of days of the given month:
	day_list = []
	for day in range(1,32):
		try:
			day_list.append(datetime.date(year,month,day).day)
		except ValueError:
			break
	# If last or second last day requested, reverse list and count
	# from the back
	if nth < 0:
		day_list.reverse()
		nth = nth*-1

	# Start with the first day of the month
	dom = datetime.date(year,month,1)
	# Initialize counter
	day_count = 0
		
	# Run through days of the month until the requested day of the week,
	# add to counter and break when required number is reached
	for d in day_list:
		dom = dom.replace(day=d)
		dow = dom.weekday()
		# Add to counter if correct day of the week
		if dow == weekday:
			day_count += 1
		# If the number of days reached, return the date
		if day_count == nth:
			req_date = dom
			break 
		
	return req_date