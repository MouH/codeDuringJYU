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
from distanceMeasure import cosineSimilarity

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
		itemHashValue = self.__hash(item)
		self.data.append(item)


		for i, trie in enumerate(self.tries):
			a = trie.insert( itemHashValue[i*self.rows : (i+1)*self.rows], currentDataSize )
			candidate += a
		print 'candidate size: ', len(candidate)

		if len(candidate) == 0:
			return -1,0
		print candidate
		distance = cosineSimilarity(np.array(self.data)[candidate], item)
		index = np.argmin(distance)

		return candidate[index], distance[index]

	def findApproximateSimilar(self):
		a = None
		buckets = []
		for trie in self.tries:
			bucket = trie.getBucket()
			if len(bucket)==0:
				continue
			else:
				buckets += bucket
		if buckets == []:
			return 0,0,0
		print buckets
		for bucket in buckets:
			a = np.array([ self.data[bucket[1]], self.data[bucket[0]] ])
			a = bucket[1], bucket[0], pdist(a, self.distanceMeasure)[0]
		if a!=None:
			return a
		else:
			return 0,0,0

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
			print 'butket length', len(bucket)
			if len(bucket)==0:
				continue
			else:
				possibleList.append(bucket)
		
		candidate = []
		# print possibleList
		if len(possibleList) == 0:
			return 0,0,0
		for i in possibleList:
			#print i
			temp = pdist( np.array([ self.data[item] for item in i ]), self.distanceMeasure )
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
	seed = 1
	random.seed(seed)	
	numOfData = 10000
	numOfAttribute = 1000
	data = random.randn(numOfData, numOfAttribute)
	bands = 10
	rows = 15
	distanceMeasure = 'cosine'

	testseed=12341

	testlsh = lsh(numOfAttribute, bands, rows, distanceMeasure)

	import time
	t1=time.time()
	testlsh.createHash(testseed)
	testlsh.insertDataset(data[0:-1])
	t2=time.time()
	
	# dis = pdist(data[0:-1], distanceMeasure)
	# k = np.argmin(dis)
	# m = np.argmax(dis)

	# t3=time.time()
	# i,j,distance = testlsh.findMostSimilar()
	# i,j,distance = testlsh.findApproximateSimilar()
	# t4=time.time()


	# com = list(combinations(range(len(data)-1),2))
	# print '\ninsert data used: ', t2-t1
	# print 'naive compute all time used: ', t3-t2
	# print 'lsh used: ', t4-t3
	# print '\nthe most similar is: ', i, j, distance
	# print 'true minimal: ', com[k][0], com[k][1], dis[k]
	# print 'true maximal: ', com[m][0], com[m][1], dis[m]

	
	print '\n-----------------------------------------------------------------'
	print 'testing insert similar\n'
	t5 = time.time()
	i, distance = testlsh.insertAndFind(data[-1])
	t6 = time.time()

	dis = cosineSimilarity(data[0:-1,:], data[-1,:])
	k = np.argmin(dis)
	m = np.argmax(dis)
	t7 = time.time()

	print '\ninsert data and find approximate used: ', t6-t5
	print 'naive compute all time used: ', (t7-t6)
	print '\nthe most similar is: ', i, distance
	print 'true minimal: ', k, dis[k]
	print 'true maximal: ', m, dis[m]

if __name__ == '__main__':
	test()
