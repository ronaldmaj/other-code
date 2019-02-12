# Attempt at answering Python Morsels exercise - multimax (2019-02-12)

def add_key(item, max_list, key):
	if key(item) > key(max_list[0]):
		max_list = [item]
	elif key(item) == key(max_list[0]):
		max_list.append(item)
	return max_list

def multimax(iter, key = lambda x: x):
	max_list = []
	if iter:
		# If there is no key, will just check max val:
		for item in iter:
			# If max_list has no items, add
			if not max_list: 
				max_list.append(item)
			# Otherwise check and add based on key :
			else:	
				max_list = add_key(item, max_list, key)
					
	return max_list
	
# Passed all tests