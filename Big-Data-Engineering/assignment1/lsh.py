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
	def __init__(self, numOfAttribute, bands, rows, distanceMeasure):
		'''
		data is numpy array or list of lists

		'''
		self.numOfAttribute = numOfAttribute
		self.distanceMeasure = distanceMeasure
		self.bands = bands
		self.rows  = rows
		self.hashFunctions = None
		self.tries = [ lshTrie() for i in range(bands) ]
		self.data = []

	def insertDataset(self, data):
		'''
		Insert Dataset into tries
		data: numpy.ndarray with numOfAttribute
		'''
		self.data = list(data)

		if data.shape[1] != self.numOfAttribute:
			raise RuntimeError('The data have wrong number of attribute.')

		for index, item in enumerate(data):

			self.data.append(item)
			itemHashValue = self.__hash(item)
			#print itemHashValue
			for i, trie in enumerate(self.tries):
				#print itemHashValue[i*self.bands : (i+1)*self.bands]
				trie.insert( itemHashValue[i*self.rows : (i+1)*self.rows], index )
			#print 'insert: ', item


	def insertAndFind(self, item):
		if len(item) != self.numOfAttribute:
			raise RuntimeError('The data have wrong number of attribute.')
		candidate = []
		currentDataSize = len(self.data)
		for i, trie in enumerate(self.tries):
			a = trie.insert( itemHashValue[i*self.bands : (i+1)*self.bands], index+indexNow )
			candidate += a

		temp = pdist(np.array(candidate))
		k = temp.argmin()
		# print 'k',k
		com = list(combinations(range(currentDataSize),2))
		return candidate[com[k][0]], candidate[com[k][1]], temp[k]

	def findMostSimilar(self):
		'''
		find the most similar item
		return 0,0,0 meaning not find one, should set a smaller
		band and row

		It's a 'AND' and 'OR' implementation of LSH.
		'''

		possibleList = []
		for trie in self.tries:
			bucket = trie.getBucket()
			print 'butket', bucket
			if len(bucket)==0:
				continue
			else:
				possibleList.append(bucket)
		print len(possibleList)
		candidate = []
		# print possibleList
		if len(possibleList) == 0:
			return 0,0,0
		for i in possibleList:
			#print i
			temp = pdist( np.array([ self.data[item] for item in i ]) )
			k = temp.argmin()
			# print 'k',k
			com = list(combinations(range(len(i)),2))
			# print com
			candidate.append( ( temp[k], i[com[k][0]], i[com[k][1]] ) )
		# print candidate
		mostSimilar = sorted(candidate)[0]
		# print mostSimilar
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
		self.hashFunctions = random.randint( -1, 1.1, ( self.numOfAttribute, self.bands*self.rows ) )
		self.hashFunctions[self.hashFunctions==0] = 1
		
	def __hash(self, itemVertor):
		'''
		get hash value for a itemVertor
		'''
		hashValue = itemVertor.dot(self.hashFunctions)
		# set 0 to random at -1 or 1
		a = np.where(hashValue==0)
		for i in range(len(a)):
			hashValue[a[i]] = 1 if random.rand()>0.5 else -1

		hashValue[ hashValue > 0 ] = 1
		hashValue[ hashValue < 0 ] = -1
		#print hashValue
		return hashValue


def test():
	seed = 0
	random.seed(seed)	
	numOfData = 1000
	numOfAttribute = 1000
	data = random.randn(numOfData, numOfAttribute)
	bands = 10
	rows = 20
	distanceMeasure = 'cosine'

	testseed=12341234123

	testlsh = lsh(numOfAttribute, bands, rows, distanceMeasure)

	import time
	t=time.time()
	testlsh.createHash(testseed)
	testlsh.insertDataset(data)
	print '\ninsert data used: ', time.time()-t

	t=time.time()
	# print data
	dis = pdist(data)
	k = np.argmin(dis)
	m = np.argmax(dis)
	print 'naive compute all time used: ', time.time()-t
	
	t=time.time()
	i,j,distance = testlsh.findMostSimilar()
	print 'lsh used: ', time.time()-t

	com = list(combinations(range(len(data)),2))
	print '\nthe most similar is: ', i, j, distance
	print 'true minimal: ', com[k][0], com[k][1], dis[k]
	print 'true maximal: ', com[m][0], com[m][1], dis[m]

	

if __name__ == '__main__':
	test()