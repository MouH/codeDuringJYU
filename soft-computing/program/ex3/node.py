#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TIES451 - programming assignment final
Multi-Objective Optimization - NSGA2

Author: Mou Hao
'''

__author__     = "Mou Hao"

class Node:
    '''
    Class Node, design for a store the indiviudal in the evolutionary programming

    '''

    def __init__(self, x):
        self.__x = x # attribute of this node
        self.__doninationCounter = 0 # numbers nodes dominates this node
        self.__rank = 0 # the rank of each node, inital to be 0
        self.__crowdingDistance = 0 # set the crowdingDistance

    def getDonimationCounter(self):
        return self.__doninationCounter

    def setDonimationCounter(self, counter):
    	self.__doninationCounter = counter

    def getX(self):
    	return self.__x

    def setX(self, x):
    	self.__x = x

    def getRank(self):
    	return self.__rank

    def setRank(self, rank):
    	self.__rank = rank
    
    def getCrowdingDistance(self):
    	return self.__crowdingDistance

    def setCrowdingDistance(self, crowdingDistance):
    	self.__crowdingDIstance = crowdingDistance

class NSGA2:
    '''
    '''

    def __init__(self, initialPopulation):
        '''
        objective function = []
        population = []
        '''
        self.__population = initialPopulation

    def nsga2(iteration):
        '''

        '''
    	pass

    def nonDominatedSort(nodes):
    	'''
    	input is a set
    	compute the non donimate number for given nodes
    	'''
    	pass

    def generateOffspring(self):
        '''
        generate offspring with self.__population
        tournament selection
        cross over - linear cross over
        mutation
        '''

    def crowdingDistanceCompute(nodes):
    	'''
    	input a given nodes, compute crowding distance
    	'''
    	pass

def main():
    # node = Node(1)
    # print node.getRank()
    pass


if __name__ == '__main__':
    main()