#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TIES451 - programming assignment final
Multi-Objective Optimization - NSGA2

Author: Mou Hao
'''

__author__     = "Mou Hao"

from GAhelper import *
from objectiveFunction import *

class Node:
    '''
    Class Node, design for a store the indiviudal in the evolutionary programming of NSGA-2

    '''

    def __init__(self, attribute):
        self.__attribute = attribute # attribute of this node

        self.__dominationCounter = 0 # numbers nodes dominates this node
        self.__dominateSet = [] # list of nodes dominated by this node
        self.__rank = 0 # the rank of each node, inital to be 0
        self.__crowdingDistance = 0 # set the crowdingDistance
        
        # set objective value
        self.__x = objectiveFunction(self.__attribute) 

    def getAttribute(self):
        return self.__attribute

    def getDominationCounter(self):
        return self.__dominationCounter

    def setDominationCounter(self, counter):
    	self.__dominationCounter = counter

    def increaseDominationCounter(self):
        self.__dominationCounter += 1

    def decreaseDominationCounter(self):
        self.__dominationCounter -= 1

    def getDominateSet(self):
        return self.__dominateSet
    
    def setDominateSet(self, donimateSet):
        self.__dominateSet = donimateSet

    def addDominateSet(self, node):
        self.__dominateSet.append(node)

    def getX(self):
    	return self.__x

    def getRank(self):
    	return self.__rank

    def setRank(self, rank):
    	self.__rank = rank
    
    def getCrowdingDistance(self):
    	return self.__crowdingDistance

    def setCrowdingDistance(self, crowdingDistance):
    	self.__crowdingDistance = crowdingDistance

    def __lt__(self, node):
        return self.__rank > node.getRank()
        # if self.__rank > node.getRank():
        #     return True
        # else:
        #     return 

class NSGA2:
    '''
    '''

    def __init__(self, initialPopulation):
        '''
        objective function = []
        population = []
        '''
        self.__population = initialPopulation

    def getPopulation():
        return self.__population

    def nsga2(self, iteration):
        '''
        implementation of the NSGA-2 algorithm

        takes a maxIteration time as an input
        output the population
        '''
        maxIteration = iteration
        
        while maxIteration > 0:
            # combine parents and offspring population
            tempPopulation = [ i for i in 
                            set(generateOffspring(self.__population) + self.__population)]
            
            # sort and get the first n
            self.__population = __sort(tempPopulation)



    def __getNextPopulation(self, nodes):
        '''
        sort population with 
        - __nonDominatedSort
        - __crowdingDistanceCompute

        return the a population of sorted first population length nodes
        '''

        size = len( self.__population ) # the population size
        returnSet = [] # return set

        # implement the non dominate sort
        nodesSortByDominate = self.__nonDominatedSort(nodes)
        
        # find the rank should be sort by crowdingDistance
        i = 0

        while True:
            if ( len(returnSet) + len(nodesSortByDominate[i]) ) > size:
                nodesSortByCrowding = self.__crowdingDistanceCompute(nodesSortByDominate[i])
                returnSet = returnSet + nodesSortByCrowding[0:(size-len(returnSet))]
                return returnSet
            elif ( len(returnSet) + len(nodesSortByDominate[i]) ) == size:
                returnSet = returnSet + nodesSortByDominate[i]
                return returnSet
            else:
                returnSet = returnSet + nodesSortByDominate[i]
                i += 1
    
    def __nonDominatedSort(self, nodes):
    	'''
    	input is a set
    	compute the non donimate number for given nodes

        return a list of list(with same rank)
    	'''

        sortedNodes = [] # to be returned

        # compare each pair and compute their dominate counter and dominated set
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                temp = self.__dominate(nodes[i], nodes[j])
                # print 1
                if temp == -1:
                    # print 2
                    nodes[i].increaseDominationCounter()
                    nodes[j].addDominateSet(nodes[i])
                if temp == 1:
                    # print 3
                    nodes[i].addDominateSet(nodes[j])
                    nodes[j].increaseDominationCounter()

        # find the first rank
        ranklist = []
        for node in nodes:
            if node.getDominationCounter() == 0:
                node.setRank(1)
                ranklist.append(node)

        rank = 2
        # find the rest frontier
        while len(ranklist) > 0:
            sortedNodes.append(ranklist)
            nextFront = []

            for nodep in ranklist:
                for nodeq in nodep.getDominateSet():
                    nodeq.decreaseDominationCounter()
                    
                    if nodeq.getDominationCounter() == 0:
                        nodeq.setRank(rank)
                        nextFront.append(nodeq)

            ranklist = nextFront
            rank += 1

        return sortedNodes
  	
    def __dominate(self, node1, node2):
        '''
        compute the dominate relation of two nodes
        
        if node1 > node2: return 1
        else if node1 = node2 return 0
        else return -1
        '''
        x1 = node1.getX()
        x2 = node2.getX()

        trueOrFalse = [ x1[i] > x2[i] for i in range(len(x1)) ]

        if trueOrFalse.count(True) == len(x1):
            return 1
        elif trueOrFalse.count(False) == len(x1) :
            return -1
        else:
            return 0

    def __crowdingDistanceCompute(self, nodes):
    	'''
    	input a given nodes, compute crowding distance
    	
        return a sorted nodes list according to the crowd distance
        '''

    	numOfObjectiveFunction = len(nodes[0].getX())
        
        # iterate n times, n = the number of objective funtions
        for i in range(numOfObjectiveFunction):
            # create a tuple list of the i'th objective value and node
            # list - [  ( i'th value, node )   .......]
            valueTuple = [ ( (node.getX())[i], node ) for node in nodes ]
            valueTuple.sort() # sort this list with the first value of each tuple

            maxValue = valueTuple[-1][0]
            minValue = valueTuple[0][0]
            infinite = float('inf')

            # set the boundary value to be infinite
            valueTuple[0][1].setCrowdingDistance(-infinite)
            valueTuple[-1][1].setCrowdingDistance(infinite)

            for i in range(1, len(valueTuple)-1):
                if valueTuple[i][1].getCrowdingDistance() != infinite:
                    valueTuple[i][1].setCrowdingDistance( valueTuple[i][1].getCrowdingDistance() +
                                    ( valueTuple[i+1][0] + valueTuple[i-1][0] ) / ( maxValue - minValue ) )


            # create the return list nodes
            distanceTuple = [ (node.getCrowdingDistance(), node) for node in nodes ]
            distanceTuple.sort()
            return [ tu[1] for tu in distanceTuple ]
