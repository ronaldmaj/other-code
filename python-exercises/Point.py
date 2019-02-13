# Attempt at Python Morsels exercise 'Point'
# create Point class:

# Attempt at base exercise - passed tests
class Point:
	
	def __init__(self, x, y, z):
		self.x = x 
		self.y = y
		self.z = z
	
	def __repr__(self):
		return f'Point({self.x}, {self.y}, {self.z})'
		
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z
		
	def __ne__(self, other):
		return self.x != other.x or self.y != other.y or self.z != other.z	
	
	# Attempt at bonus 1 - passed
	def __add__(self, other):
		return Point(self.x+other.x, self.y+other.y, self.z+other.z)
		
	def __sub__(self, other):
		return Point(self.x-other.x, self.y-other.y, self.z-other.z)
	
	# Attempt at bonus 2 - passed
	def __mul__(self, other):
		return Point(self.x * other, self.y * other, self.z * other)
 
	def __rmul__(self, other):
		return Point(self.x * other, self.y * other, self.z * other)
