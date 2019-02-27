# Attempt at Python morsel exercise - parse_range - passed tests

# Take the string and parse it
def parse_ranges(string):
	
	# Split list based on commas:
	ranges = string.split(',')
	
	# Create pairs of start/end numbers in string format:
	str_pairs = [
			[num_str for num_str in r.split('-')] 
			for r in ranges
			]
	
	# Convert string pairs to integer pairs, filtering for non-numeric vals:
	pairs = []
	for str_pair in str_pairs:
		pair = []
		for str_num in str_pair:
			try:
				pair.append(int(str_num))
			except ValueError:
				pass
		pairs.append(pair)
	
	# Create list of numbers based on the range pairs
	numbers = []
	for pair in pairs:
		# If a single number, yield just that number:
		if len(pair) == 1:
			yield pair[0]
		# Otherwise create a range of numbers based on pair:
		else:
			for num in range(pair[0], pair[1]+1):
				yield num
	

	#Find position of all commas:
	#coms = []
	#for i,let in enumerate(string):
	#	if let == ",":
	#		coms.append(i)
	
	#ranges = []
	#for i in range(len(coms)+1):
	#	if i == 0:
	#		ranges.append(string[:coms[0]])
	#	elif i == len(coms):
	#		ranges.append(string[coms[i-1]+1:])
	#	else:
	#		ranges.append(string[coms[i-1]+1:coms[i]])
	
	#for r in ranges:
	#	nums = []
	#	for i,el in enumerate(r):
	#		if el.isnumeric():			