#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
find the most similar item


'''

__author__     = "Mou Hao"

import numpy as np
from distanceMeasure import cosineSimilarity
import sys
from runCifarLsh import *
import pylab
import cPickle

resultPath = sys.argv[1]
path = sys.argv[2]

f = open( resultPath, 'rb')
result = cPickle.load(f)
f.close()



rows = []
distance = []
candidateSize = []

data, testdata = readCifarData(path, 6000, 1)
small, sdis, l, maxdis= runNaive(data, testdata)

for row in result.iterkeys():
	temp = np.array(result[row])
	rows.append(row)
	distance.append( np.average(temp[:,1] - sdis) )
	candidateSize.append( np.average(temp[:,2]) )
	
print distance, candidateSize
