#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

__author__     = "Mou Hao"

class lshTrie:
	'''
	Trie designed for lsh.
	Trie has edges if not buttom
	Trie has element if in buttom
	'''
	def __init__(self):
		self.edges = {}
		self.element = []

	def insert(self, array, label):
		'''
		Insert the a hash value vertor in. And return the element in the leaf
		'''
		if len(array) == 0:
			temp = self.element[:]
			self.element.append(label)
			# return temp
		else:
			key = array[0]
			if key not in self.edges:
				self.edges[key] = lshTrie()
			self.edges[key].insert(array[1:], label)

	def search(self, array):
		if len(array) == 0:
			temp = self.element[:]
			return temp
		else:
			key = array[0]
			if key not in self.edges:
				return []
			else:
				return self.edges[key].search(array[1:])
