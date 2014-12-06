#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Hashing funciton
'''

def rabinHashing(word, seed, module):
	'''
	seed is the hex
	rabinHashing(abc)   = a*seed^2 + b*seed^1 + c*seed^0 
						= ((a*seed + b) * seed) + c
	'''
	hashValue = 0

	for i in word:
		hashValue = seed * hashValue + ord(i)
	return hashValue % module