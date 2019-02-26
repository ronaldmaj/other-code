# Attempt at is_perfect_square - passed all tests

from decimal import *
import cmath

def is_perfect_square(num, *, complex=False):
	
	if complex:
		root = cmath.sqrt(num)
		R = root.real - int(root.real)
		I = root.imag - int(root.imag)
		return R - I == 0
	else:
		getcontext().prec = 64
		if num < 0:
			return False
		else:
			return Decimal(num).sqrt() - int(Decimal(num).sqrt()) == Decimal(0)