import numpy as np
from lsh.lshTrie import lshTrie
from lsh.distanceMeasure import cosineSimilarity
from numpy import random
from lsh.lsh import lsh

'''
'''

def test():
	seed = 1
	random.seed(seed)	
	numOfData = 10000
	numOfAttribute = 1000
	data = random.randn(numOfData, numOfAttribute)
	bands = 10
	rows = 5
	distanceMeasure = 'cosine'

	testseed=12341

	testlsh = lsh(numOfAttribute, bands, rows, distanceMeasure)

	import time
	t1=time.time()
	testlsh.createHash(testseed)
	testlsh.insertDataset(data[0:-1])
	t2=time.time()

	print 'testing insert similar\n'
	t5 = time.time()
	i, distance, candidateSize = testlsh.search(data[-1])
	t6 = time.time()

	dis = cosineSimilarity(data[0:-1,:], data[-1,:])
	k = np.argmin(dis)
	m = np.argmax(dis)
	t7 = time.time()

	print '\ninsert data and find approximate used: ', t6-t5
	print 'naive compute all time used: ', (t7-t6)
	print 'candidate size: ', candidateSize
	print '\nthe most similar is: ', i, distance
	print 'true minimal: ', k, dis[k]
	print 'true maximal: ', m, dis[m]

if __name__ == '__main__':
	test()
