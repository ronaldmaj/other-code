''' 
Revision 2019-02-19
Exercises:
- fix_csv
- anagram
- multimax
- Point 
''' 


# Attempt at fix_csv - passed tests

if __name__ == '__main__':
	# Import packages
	import csv
	import argparse

	# Parse the input arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('in_file')
	parser.add_argument('out_file')
	parser.add_argument('--in-delimiter', default = None)
	parser.add_argument('--in-quote', default = None)
	args = parser.parse_args()
	
	# Run through the input file and write to output file:
	
	with open(args.in_file, newline = '') as in_csv:
		
		# If one or the other is not defined:
		if args.in_delimiter == None or args.in_quote == None:
			# Sniff out the dialect
			dialect = csv.Sniffer().sniff(in_csv.read(1024))
			in_csv.seek(0)
			# If delimiter is defined, then set the quotechar from dialect:
			if args.in_delimiter:
				qchar = dialect.quotechar
				delim = args.in_delimiter
			# If the quote character is defined, then set delimiter from dialect
			elif args.in_quote:
				qchar = args.in_quote
				delim = dialect.delimiter
			# Else if both are undefined, use dialect for both: 
			else:
				qchar = dialect.quotechar
				delim = dialect.delimiter
		# If both are defined then we can use those:
		else:
			qchar = args.in_quote
			delim = args.in_delimiter
		# Now we can read the data:	
		read_data = csv.reader(in_csv, 
									delimiter = delim, 
									quotechar = qchar
									)
		
		with open(args.out_file, mode = 'w', newline = '') as out_csv:
			write_data = csv.writer(out_csv, delimiter = ",")
			write_data.writerows(read_data)

			
# Attempt at anagram - Passed Tests
def is_anagram(str1, str2):
	import unicodedata as ud
	# Normalize string - lower case, remove accents and check if in alphabet 
	def norm_str(string):
		result = ud.normalize('NFKD',string.lower())
		result = sorted([letter for letter in result if letter.isalpha()]) 
		return result
	# Apply normalization to strings 1 and 2 and compare
	str1 = norm_str(str1)
	str2 = norm_str(str2)
	return str1 == str2

# Attempt at multimax - Passed tests
def multimax(iter, key = lambda x: x):
	max_list = []
	for el in iter:
		if max_list:
			if key(el) > key(max_list[0]):
				max_list = [el]
			elif key(el) == key(max_list[0]):
				max_list.append(el)
		else:
			max_list.append(el)
	return max_list		

# Attempt at Point - passed tests

class Point:
	
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z
	
	def __repr__(self):
		return f'Point({self.x}, {self.y}, {self.z})'
		
	def __eq__(self, other):
		sx = self.x 
		sy = self.y
		sz = self.z
		return (sx, sy, sz) == (other.x, other.y, other.z)
		
	def __add__(self, other):
		nx, ny, nz = self.x + other.x, self.y + other.y, self.z + other.z
		return Point(nx, ny, nz)
	
	def __sub__(self, other):
		nx, ny, nz = self.x - other.x, self.y - other.y, self.z - other.z
		return Point(nx, ny, nz)
		
	def __mul__(self, num):
		nx, ny, nz = self.x * num, self.y * num, self.z * num
		return Point(nx, ny, nz)
		
	def __rmul__(self, num):
		return self.__mul__(num)
		
	def __iter__(self):
		return iter((self.x, self.y, self.z))
		




