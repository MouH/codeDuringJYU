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
		if len(array) == 0:
			self.element.append(label)
		else:
			key = array[0]
			if key not in self.edges:
				self.edges[key] = lshTrie()
			self.edges[key].insert(array[1:], label)

	def getBucket(self):
		'''
		From trie gets the element in the same leaf
		list of lists
		'''
		returnList = []
		if len(self.edges) == 0:
			# at leaf
			if len(self.element) == 1:
				return []
			else:
				return self.element
		else:
			# not at leaf
			for i in self.edges.iterkeys():
				temp = self.edges[i].getBucket()
				if len(temp) == 0:
					continue
				else:
					returnList += temp
		# print returnList
		return returnList



def testTrie():
	# intiial empty trie
	trie = lshTrie()
	import numpy as np
	data1 = np.array([1,0,1,0,1,0])
	data2 = np.array([1,1,0,0,0,0])
	data3 = np.array([1,1,0,0,0,0])

	trie.insert(data1, 0)
	trie.insert(data2, 1)
	trie.insert(data3, 2)
	#print trie.edges[1].edges.keys()
	a = trie.getBucket()
	assert a == [1,2]

	print 'test success'


def main():
	testTrie()


if __name__ == '__main__':
    main()