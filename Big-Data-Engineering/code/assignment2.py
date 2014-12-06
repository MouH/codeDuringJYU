#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Assignment 2 for ties438 - Big Data Engineering
'''

from lib.textProcess import *
from lsh.distanceMeasure import jaccardSimilarity, compareSignature
import sys
from lsh.minHashing import *
import random
import math
import pylab

def isPrime(num):
	for j in range(2, int(math.sqrt(num))):
		if (num % j) == 0:
			return False
	return True

def findPrime(num):
	prime = num
	while True:
		if isPrime(prime):
			return prime
		else:
			prime += 1

def readData(path):
	data = []
	allterm = set()
	with open(path, "rb") as f:
		for line in f:
			# can be changed to other methods
			temp = stemAndRemoveFrequence(line.split())
			
			data.append(temp)
			allterm = allterm.union(temp)

	return data, allterm

def main(dataPath):
	# set parameters
	hashSize = [5, 10, 20, 40, 80]
	# hashSize = [5]
	seed = 1
	rawData, allterm = readData(dataPath)
	print 'read data done'
	module = findPrime( len(allterm) )
	print module

	error = []
	for size in hashSize:
		print size
		err = 0
		for i in range(100):
			d1, d2 = random.sample(rawData, 2)
			trueDistance = jaccardSimilarity([d1], d2)[0]
			# print trueDistance

			mhash = minHashing(size)
			mhash.createHash(random.randint(0,100))

			s1 = mhash.hash(d1, module)
			s2 = mhash.hash(d2, module)
			approximate = compareSignature(s1, s2)
			# print 'app   ', approximate

			err += abs(trueDistance - approximate )
		print err/100.0
		error.append( err / 100.0 )

	plotResult(hashSize, error)

def plotResult(hashSize, error):
	pylab.plot(hashSize, error)
	pylab.show()


if __name__ == '__main__':
	main(sys.argv[1])
