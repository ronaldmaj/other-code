# Attempt at unicode_escape Python Morsel


import argparse
import html

parser = argparse.ArgumentParser()
parser.add_argument("input_file")

args = parser.parse_args()

in_file = args.input_file

with open(in_file) as f:
	read_data = f.read()
	last_two = []
	for i,let in enumerate(read_data):
		if i == 0:
			last_two.append(let)
		elif i == 1:
			last_two.append(let)
		else:
			if last_two == ['&','#'] and let == 'x':
				