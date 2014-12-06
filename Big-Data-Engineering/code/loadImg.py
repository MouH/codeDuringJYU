#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
load img from cifar data
'''

import Image
import numpy as np

def loadImg(pixel):
	length = len(pixel) / 3
	imageSize = int(np.sqrt(length))

	R = pixel[0 : length].reshape(imageSize, imageSize).astype(int)
	G = pixel[length : length*2].reshape(imageSize, imageSize).astype(int)
	B = pixel[length*2 : ].reshape(imageSize, imageSize).astype(int)

	img = Image.new( 'RGB', ( imageSize, imageSize ), "black") # create a new black image
	pixels = img.load() # create the pixel map
	 
	for i in range(img.size[0]):    # for every pixel:
		for j in range(img.size[1]):
			pixels[i,j] = (R[i,j], G[i,j], B[i,j]) # set the colour accordingly

	img.show()


def test(path):
	import cPickle
	fo = open(path, 'rb')
	dict = cPickle.load(fo)
	fo.close()
	rawdata = dict['data']

	loadImg( rawdata[0] )

if __name__=='__main__':
	import sys
	test(sys.argv[1])

