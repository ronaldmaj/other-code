# Revision script for the tail and group_by functions on 2019-02-06

# tail
def tail(seq, n):
	tail = []
	for i,el in enumerate(seq):
		tail.append(el)
		if i > (n-1):
			tail.pop(0)
	return tail

# group_by - passed tests
from collections import Counter, defaultdict

def group_by(iter, key_func=None):
	if key_func == None:
		key_func = lambda x: x
	groups = defaultdict(list)
	for val in iter:
		groups[key_func(val)].append(val)
	return dict(sorted(groups.items()))
	