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
from distanceMeasure import cosineSimilarity, jaccardSimilarity

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
		currentSize = len(self.data)

		if data.shape[1] != self.numOfAttribute:
			raise RuntimeError('The data have wrong number of attribute.')

		for index, item in enumerate(data):
			self.data.append(item)
			itemHashValue = self.__hash(item)
	
			# have to be changed to a faster way
			for i, trie in enumerate(self.tries):
				trie.insert( itemHashValue[i*self.rows : (i+1)*self.rows], index+currentSize )


	def search(self, item):
		'''
		insert item,
		return index, distance, candidate size
		'''
		if len(item) != self.numOfAttribute:
			raise RuntimeError('The data have wrong number of attribute.')
		candidate = []

		itemHashValue = self.__hash(item)

		for i, trie in enumerate(self.tries):
			a = trie.search( itemHashValue[i*self.rows : (i+1)*self.rows] )
			candidate += a

		# print candidate
		if len(candidate) == 0:
			return -1,0,0
		
		distance = self.__distance(np.array(self.data)[candidate], item)
		index = np.argmin(distance)

		return candidate[index], distance[index], len(candidate)

	def __distance(self, nodeList, item):
		if self.distanceMeasure == 'cosine':
			cosineSimilarity(nodeList, item)
		elif self.distanceMeasure == 'jaccard':
			jaccardSimilarity(nodeList, item)
		else:
			raise RuntimeError('wrong distance measure, only support jaccard and minhashing')		

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
		'''
		write the min hashing functions
		'''
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
		if self.distanceMeasure == 'jaccard':
			pass
		elif self.distanceMeasure == 'cosine':
			hashValue = itemVertor.dot(self.hashFunctions)
			# set 0 to random at -1 or 1
			a = np.where(hashValue==0)
			for i in range(len(a)):
				hashValue[a[i]] = 1 if random.rand()>0.5 else -1

			hashValue[ hashValue > 0 ] = 1
			hashValue[ hashValue < 0 ] = -1
			#print hashValue
			return hashValue
		else:
			pass
