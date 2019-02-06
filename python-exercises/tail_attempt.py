# Attempt at solving Python Morsels problem: tail

# Return the last 'n' items from a sequence 'seq'
def tail(seq, n):
	tail = []
	if n < 0:
		return tail
	else:
		for idx,val in enumerate(seq):
			tail.append(val)
			if idx >= n:
				tail.pop(0)
		return tail