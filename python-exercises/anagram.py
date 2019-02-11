# Attempt at 'is_anagram' exercise from Trey Hunner's Python Morsels

# Way 1: - passed tests
from collections import Counter

def is_anagram1(ex1, ex2):
	return Counter(ex1.lower()) == Counter(ex2.lower())
	
# Way 2: - passed tests

def is_anagram2(ex1, ex2):
	def count_letters(ex):
		dictionary = {}
		for letter in ex:
			if letter in dictionary:
				dictionary[letter] += 1
			else:
				dictionary[letter] = 1
		return dictionary
	ex1_count = count_letters(ex1.lower())
	ex2_count = count_letters(ex2.lower())
	return ex1_count == ex2_count

# Way 3: - passed tests

def is_anagram3(ex1, ex2):
	return sorted(ex1.lower()) == sorted(ex2.lower())

	
# Bonus (1) attempt (ignore spaces) - passed tests

def is_anagram_b1(ex1, ex2):
	def rmv_space(ex):
		ex_sort = sorted(ex.lower())
		space_count = 0
		for letter in ex_sort:
			if letter == ' ':
				space_count += 1
		return ex_sort[space_count:]	
	return rmv_space(ex1.lower()) == rmv_space(ex2.lower())
	
	
# Bonus (2) attempt (ignore punctuation) - passed tests

def is_anagram_b2(ex1, ex2):
	def rmv_punc(ex):
		ex_sort = sorted(ex.lower())
		letter_start = 0
		for i,letter in enumerate(ex_sort):
			if letter in 'abcdefghijklmnopqrstuvwxyz':
				letter_start = i
				break
		return ex_sort[letter_start:]	
	return rmv_punc(ex1.lower()) == rmv_punc(ex2.lower())
	
	
# Bonus (3) attempt (convert accented characters) - passed tests

import unicodedata as ucd

def is_anagram(ex1, ex2):
	def rmv_acc(ex):
		ex_norm = ucd.normalize('NFKD',ex)
		ex_sort = sorted(ex_norm.lower())
		ex_noacc = []
		for letter in (ex_sort):
			if letter in 'abcdefghijklmnopqrstuvwxyz':
				ex_noacc.append(letter)
		return ex_noacc	
	return rmv_acc(ex1.lower()) == rmv_acc(ex2.lower())