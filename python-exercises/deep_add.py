# Attempt at deep_add Python Morsels exercise

# While the type of the element is (list) continue going down

# Passed all tests

from decimal import Decimal
from collections.abc import Iterable

def sum_el_list(nest):
	try:
		return sum(nest)
	except TypeError:
		if isinstance(nest, Iterable):
			return sum(sum_el_list(el) for el in nest)
		else:
			return nest

# Take in nested list of numbers and add all of them together
def deep_add(nest, start=0):
	total = start
	for el in nest:
		total += sum_el_list(el)
	return total