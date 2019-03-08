# Attempt at unicode_escape Python Morsel after looking at solutions


if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("input_file", type=argparse.FileType('rt'))

	args = parser.parse_args()

	in_file = args.input_file

with open(in_file, mode='rt', encoding='utf-8') as f:
	data = f.read()
	escape_str = []
	for c in data:
		code = hex(ord(c))[2:]
		if ord(c) > 127:
			if len(code) <= 4:
				escape_str.append(rf"\u{code:0>4}")
			else:
				escape_str.append(rf"\U{code:0>8}")
		else:
			escape_str.append(c)
	print(''.join(escape_str), end='')
