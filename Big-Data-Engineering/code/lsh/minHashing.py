#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
An implementation of min-hashing
'''
import numpy as np
from numpy import random
from hashing import rabinHashing

class minHashing:
	def __init__(self, numOfHashing):
		self.hexes = []
		self.numOfHashing = numOfHashing

	def createHash(self, seed=1):
		'''
		create the hash parameter
		'''
		random.seed(seed)
		self.hexes = range(0, self.numOfHashing)
		random.shuffle(self.hexes)

	def hash(self, wordSet, module):
		'''
		return the hash value of the input item
		'''
		singnature = []

		for i in range(0, self.numOfHashing):
			sig = module + 1
			for word in wordSet:
				rh = rabinHashing(word, self.hexes[i], module)
				if rh < sig:
					sig = rh
			singnature.append(sig)
		return singnature

	def hashAll(itemList):
		pass
