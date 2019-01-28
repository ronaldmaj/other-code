# Attempt at Python Morsel exercise - group_by

def group_by(iterable, func=None):
	final = dict()
	def def_func(n):
		return n 
	if func == None:
		for item in iterable:
			if def_func(item) not in final: 
				final[def_func(item)] = []
			final[def_func(item)].append(item)
	else:
		for item in iterable:
			if func(item) not in final: 
				final[func(item)] = []
			final[func(item)].append(item)
	return final	