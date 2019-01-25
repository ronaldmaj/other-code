# Attempt at solving Python Morsels problem: tail

def tail(seq, n):
	tail = []
	for idx,val in enumerate(seq):
		tail.append(val)
		if idx >= n:
			tail.pop(0)
	return tail