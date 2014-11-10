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

dataFile = sys.argv[1]

fo = open(dataFile, 'rb')
dict = cPickle.load(fo)
fo.close()

data = dict['data'][0:1000]
numOfAttribute = data.shape[1]

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