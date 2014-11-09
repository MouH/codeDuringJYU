#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
find the most similar item


'''

__author__     = "Mou Hao"

import numpy as np
from numpy import random
from scipy.spatial.distance import pdist, squareform
from lshTrie import lshTrie
from itertools import combinations

class lsh:
	def __init__(self, data, bands, rows, distanceMeasure):
		'''
		data is numpy array or list of lists

		'''
		self.data = np.array(data) # n * m
		self.distanceMeasure = distanceMeasure
		self.bands = bands
		self.rows  = rows
		self.hashValueMatrix = None
		self.tries = [ lshTrie() for i in range(bands) ]

	def findMostSimilar(self):
		'''
		find the most similar item
		return 0,0,0 meaning not find one, should set a smaller
		band and row
		'''

		for index, item in enumerate(self.hashValueMatrix):
			for i, trie in enumerate(self.tries):
				trie.insert( item[i*self.bands : (i+1)*self.bands], index )

		possibleList = []
		for trie in self.tries:
			bucket = trie.getBucket()
			if len(bucket)==0:
				continue
			else:
				possibleList.append(trie.getBucket())

		candidate = []
		# print possibleList
		if len(possibleList) == 0:
			return 0,0,0
		for i in possibleList:
			print i
			temp = pdist(self.data[i])
			k = temp.argmin()
			# print 'k',k
			com = list(combinations(range(len(i)),2))
			# print com
			candidate.append( ( temp[k], com[k][0], com[k][1] ) )
		# print candidate
		mostSimilar = sorted(candidate)[0]
		return mostSimilar[1], mostSimilar[2], mostSimilar[0]

	def createHash(self, seed):
		'''
		create number of ( bands * rows ) hash funtions based on the
		distanceMeasure, meaning for different distance measure create
		different hash family
		'''

		if self.distanceMeasure == 'cosine':
			self.__randomHyperplanes(seed)
		elif self.distanceMeasure == 'jaccard':
			self.__minHashing(seed)
		else:
			raise RuntimeError('wrong distance measure, only support jaccard and minhashing')

	def __minHashing(self, seed):
		pass

	def __randomHyperplanes(self, seed):
		'''
		set hashfunctions to be ( m * (b*r) )
		'''
		# create hash functions
		random.seed(seed)
		hashFunctions = random.randint( -1, 1.1, ( self.data.shape[1], self.bands*self.rows ) )
		hashFunctions[hashFunctions==0] = 1
		
		# set hash value matrix
		self.hashValueMatrix = self.data.dot(hashFunctions)
		# set 0 to random at -1 or 1
		a,b = np.where(self.hashValueMatrix==0)
		for i in range(len(a)):
			self.hashValueMatrix[a[i], b[i]] = 1 if random.rand()>0.5 else -1

		self.hashValueMatrix[ self.hashValueMatrix > 0 ] = 1
		self.hashValueMatrix[ self.hashValueMatrix < 0 ] = -1


def test():
	seed = 6
	random.seed(seed)	
	data = random.randn(10,10)
	bands = 5
	rows = 5
	distanceMeasure = 'cosine'

	testseed=12341234123

	testlsh = lsh(data, bands, rows, distanceMeasure)
	testlsh.createHash(testseed)

	# print data
	# print '\ntrue minimal\n--------------------------------\n'
	# dis = pdist(data)
	# k = np.argmin(dis)
	# com = list(combinations(range(len(data)),2))
	# # print com
	# print com[k][0], com[k][1], dis[k]

	# print '\ndistance matrix\n----------------------------------\n'
	# print squareform(dis)

	i,j,distance = testlsh.findMostSimilar()
	print '\nthe most similar is: ', i, j, distance

if __name__ == '__main__':
	test()