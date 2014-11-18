#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
test lsh with cifar10 batch 1
'''

from lsh import lsh 
import cPickle
import sys
from scipy.spatial.distance import pdist, squareform
import numpy as np
from itertools import combinations
from distanceMeasure import cosineSimilarity


dataFile = sys.argv[1]

fo = open(dataFile, 'rb')
dict = cPickle.load(fo)
fo.close()

rawdata = dict['data']

data = rawdata[0:1000,:]
testdata = rawdata[1001:1100, :]

numOfAttribute = data.shape[1]

bands = 10
rows = 20
distanceMeasure = 'cosine'

testseed=12341

testlsh = lsh(numOfAttribute, bands, rows, distanceMeasure)

import time
t=time.time()
testlsh.createHash(testseed)
testlsh.insertDataset(data)
print '\ninsert data used: ', time.time()-t

t=time.time()
# print data
dis = cosineSimilarity(data, testdata[0,:])
k = np.argmin(dis)
m = np.argmax(dis)
print 'naive compute all time used: ', time.time()-t

t=time.time()
# i,j,distance = testlsh.findMostSimilar()
i,distance = testlsh.insertAndFind()
print 'lsh used: ', time.time()-t

print '\nthe most similar is: ', i, distance
print 'true minimal: ', k, dis[k]
print 'true maximal: ', m, dis[m]