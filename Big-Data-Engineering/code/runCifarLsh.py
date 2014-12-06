#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
test lsh with cifar10 batch 1
'''

from lsh.lsh import lsh 
import cPickle
import sys
import numpy as np
from numpy import random
from lsh.distanceMeasure import cosineSimilarity
import time
from loadImg import loadImg

def runNaive(data, testData):
	# compute the naive algotirhm
	#t=time.time()
	dis = cosineSimilarity(data, testData)
	k = np.argmin(dis)
	m = np.argmax(dis)
	# print 'naive compute all time used: ', time.time()-t
	return k, dis[k], m, dis[m]

def readCifarData(dataPath, dataSize, testDataSize):
	fo = open(dataPath, 'rb')
	dict = cPickle.load(fo)
	fo.close()
	rawdata = dict['data'].astype(float)

	if dataSize > len(rawdata):
		raise RuntimeError('request data size should be less than total size')
	if testDataSize+dataSize > len(rawdata):
		raise RuntimeError('set the test data size smaller')

	data = rawdata[0:dataSize, :]
	testdata = rawdata[dataSize:(testDataSize+dataSize), :]
	return data, testdata

def main(dataPath, savePath):
	# set parameters
	dataSize = 6000
	testDataSize = 1
	bands = 1
	# rows = [1, 2, 4, 8, 16, 32, 60]
	rows = [20]
	distanceMeasure = 'cosine'

	
	# get data
	data, testData = readCifarData(dataPath, dataSize, testDataSize)

	# naive
	small, sdis, large, ldis = runNaive(data, testData[0])

	# initial lsh
	result = {}
	for row in rows:
		res = []
		for j in range(1):
			print j
			testlsh = lsh(data.shape[1], bands, int(row), distanceMeasure)
			seed = 123
			testlsh.createHash(seed)
			testlsh.insertDataset(data)
			i, distance, candidateSize = testlsh.search(testData[0])
			res.append([i, distance, candidateSize])

			# loadImg( data[i] )
			# loadImg( testData[0] )

		result[row] = res

	print result
	# f = open( savePath, 'wb')
	# cPickle.dump(result, f)
	# f.close()

if __name__=='__main__':
	main(sys.argv[1], sys.argv[2])
