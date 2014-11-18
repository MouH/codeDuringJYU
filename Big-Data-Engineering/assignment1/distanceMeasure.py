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
	temp = np.sqrt(np.sum(x**2, axis=1)[:,None].\
					dot(np.transpose(np.sum(k**2, axis=0))[None,:]))
	distance = 2 * np.arccos( x.dot(k)/temp ) / np.pi
	
	if len(y.shape) == 1:
		return distance.reshape(x.shape[0])
	else:
		return distance


def test():
	x = np.array([[1,2,3,4],[2,3,4,5]])
	y = np.array([1,2,3,4])
	print cosineSimilarity(x,y)
	print cosineSimilarity(x,x)


if __name__=='__main__':
	test()