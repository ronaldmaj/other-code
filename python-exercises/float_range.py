# Attempt at float_range Python morsels exercise

# Take in the start, end and increment (incr) and produce a range-like
# generator as output

def float_range(*args):
	if len(args) == 3:
        start, end, incr = args
    elif len(args) == 2:
        start, end = args
        incr = 1
    elif len(args) == 1:
        end, = args  #Need the comma here.  Could write `stop = args[0]` instead ...
        incr = 1
	    start = 0.0
    else:
        raise TypeError("Wrong number of arguments!")
	
	num = start
	if incr > 0:
		while num < end:
			yield num
			num = num + incr
	else:
		while num > end:
			yield num
			num = num + incr