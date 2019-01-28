# Attempt at Python Morsel exercise - group_by

def group_by(iterable, func):
	final = dict()
	def def_func(n):
		return n 
	if func == None:
		func = def_func
	for item in iterable:
		if func(item) not in final: 
			final[func(item)] = []
		final[func(item)].append(item)
	return final	