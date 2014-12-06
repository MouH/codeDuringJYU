#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
'''

from lsh import lshTrie

def testTrie():
	# intiial empty trie
	trie = lshTrie()
	a = trie.getBucket()

	import numpy as np
	data1 = np.array([1,0,1,0,1,0])
	data2 = np.array([1,1,0,0,0,0])
	data3 = np.array([1,1,0,0,0,0])
	data4 = np.array([1,0,1,0,1,0])
	data5 = np.array([1,0,1,0,1,0])

	print trie.insert(data1, 0)
	print trie.insert(data2, 1)
	print trie.insert(data3, 2)
	print trie.insert(data4, 3)
	print trie.insert(data5, 4)
	a = trie.getBucket()
	print a

	# trie1 = lshTrie()
	# for i in range(10):
	# 	trie1.insert(np.random.randn(10),i)
	# print trie1.getBucket()

	print 'test success'


def main():
	testTrie()


if __name__ == '__main__':
    main()