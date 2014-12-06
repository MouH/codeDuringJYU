#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Different methods to split text
'''
from PorterStemmer import PorterStemmer

def stemAndRemoveFrequence(text):
	p = PorterStemmer()
	words = []
	for word in text:
		words.append( p.stem(word, 0, len(word)-1) )
	return set(words)

def bagOfWords(text):
	pass

def twoGrams(text):
	pass

def shingles(text):
	pass
