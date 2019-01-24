# 2019-01-24
# Revision of Python Morsels exercises by Trey Hunner

# Get the earliest date from a list of dates in a month-day-year format:
def get_earliest(*dates):
	def date_convert(date):
		m,d,y = date.split('/')
		return y,m,d
	return min(dates, key=date_convert)

from collections import Counter
import re

# Count the number of words in a given list. 
def count_words(words):
	list_of_words = re.findall(r'[\w\'-]+', words.lower())
	return Counter(list_of_words)
	
# Remove adjacent numbers in an iterable
def compact(numbers):
	prior = object()
	for num in numbers:
		if num != prior:
			yield num
		prior = num

# Add matrices
def add_2(mat1, mat2):
	end_mat = []
	for row1,row2 in zip(mat1,mat2):
		end_row = []
		for el_1,el_2 in zip(row1,row2):
			end_row.append(el_1+el_2)
		end_mat.append(end_row)
	return end_mat
	
def add(*mats):
	for mat in mats:
		if len(mat) != len(mats[0]):
			raise ValueError("Given matrices are not the same size.")
		for row in mat:
			if len(row) != len(mats[0][0]):
				raise ValueError("Given matrices are not the same size.")
	end_mat = []
	for rows in zip(*mats):
		end_row = []
		for els in zip(*rows):
			end_row.append(sum(els))
		end_mat.append(end_row)
	return end_mat
	
import math

# Create a Circle class
class Circle:
	
	def __init__(self, radius=1):
		self.radius = radius
	
	def __repr__(self):
		return 'Circle({})'.format(self.radius)
	
	@property
	def radius(self):
		return self._radius
	
	@property
	def diameter(self):
		return self.radius*2
	
	@property
	def area(self):
		return math.pi*self.radius**2

	@diameter.setter
	def diameter(self,diameter):
		self.radius = diameter/2
	
	@radius.setter
	def radius(self,rad):
		if rad < 0:
			raise ValueError("Radius cannot be negative")
		else:
			self._radius = rad
