#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
calculate distance
'''

import numpy as np

def cosineSimilarity(x, y):
	'''
	x is a matrix of n items and m attribute each
	y is a matrix of k items and m attirbute each
	''' 
	if len(y.shape) == 1:
		k = y[:, None]
	else:
		k = np.transpose(y)
		
	temp = np.sqrt(np.sum(x**2, axis=1)[:,None].
					dot( np.transpose(np.sum(k**2, axis=0))[None,:] ) )
	#print temp
	#print x.dot(k)/temp
	distance = np.arccos( x.dot(k)/temp ) / np.pi
	#print distance
	
	if len(y.shape) == 1:
		return distance.reshape(x.shape[0])
	else:
		return distance

def jaccardSimilarity(nodeList, item):
	'''
	nodeList is list of set
	item is a set

	return a list
	'''
	similarityList = []
	for node in nodeList:
		similarityList.append( float( len(node.intersection(item)) ) / len(node.union(item)) )
	return similarityList


def compareSignature(s1, s2):
	num = 0
	for i in range(len(s1)):
		if s1[i] == s2[i]:
			num += 1
	return 1 - float(num) / len(s1)

def test():
	x = np.array([[1,2,3,4,5],[3,3,0,5,10]])
	y = np.array([1,2,3,4,5])
	print cosineSimilarity(x,y)
	print cosineSimilarity(x,x)


if __name__=='__main__':
	test()
