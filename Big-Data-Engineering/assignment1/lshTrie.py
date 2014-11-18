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
			return temp
		else:
			key = array[0]
			if key not in self.edges:
				self.edges[key] = lshTrie()
			return self.edges[key].insert(array[1:], label)

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
				if len(self.edges[i].edges) == 0:
					a = self.edges[i].getBucket()
					if a != []:
						returnList.append(a)
				else:
					returnList += self.edges[i].getBucket()

		#print returnList
		return returnList



def testTrie():
	# intiial empty trie
	trie = lshTrie()
	a = trie.getBucket()

	import numpy as np
	data1 = np.array([1,0,1,0,1,0])
	data2 = np.array([1,1,0,0,0,0])
	data3 = np.array([1,1,0,0,0,0])
	data4 = np.array([1,0,1,0,1,0])
	data5 = np.array([1,0,1,0,1,0])

	print trie.insert(data1, 0)
	print trie.insert(data2, 1)
	print trie.insert(data3, 2)
	print trie.insert(data4, 3)
	print trie.insert(data5, 4)
	a = trie.getBucket()
	print a

	# trie1 = lshTrie()
	# for i in range(10):
	# 	trie1.insert(np.random.randn(10),i)
	# print trie1.getBucket()

	print 'test success'


def main():
	testTrie()


if __name__ == '__main__':
    main()
