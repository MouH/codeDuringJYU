#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TIES451 - programming assignment final
Multi-Objective Optimization - NSGA2

Author: Mou Hao
'''

__author__     = "Mou Hao"

from GAhelper import *

class Node:
    '''
    Class Node, design for a store the indiviudal in the evolutionary programming

    '''

    def __init__(self, x):
        self.__x = x # attribute of this node
        self.__dominationCounter = 0 # numbers nodes dominates this node
        self.__dominateSet = [] # list of nodes dominated by this node
        self.__rank = 0 # the rank of each node, inital to be 0
        self.__crowdingDistance = 0 # set the crowdingDistance

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

    def getPopulation():
        return self.__population

    def nsga2(self, iteration):
        '''
        implementation of the NSGA-2 algorithm

        takes a maxIteration time as an input
        output the population
        '''
        # maxIteration = iteration
        
        # while maxIteration > 0:
        #     # combine parents and offspring population
        #     tempPopulation = [ i for i in 
        #                     set(generateOffspring(self.__population) + self.__population)]
            
        #     # sort and get the first n
        #     self.__population = __sort(tempPopulation)



    def __sort(nodes):
        '''
        sort population with 
        - __nonDominatedSort
        - __crowdingDistanceCompute

        return the a population of sorted first population length
        '''
        pass




    def nonDominatedSort(self, nodes):
    	'''
    	input is a set
    	compute the non donimate number for given nodes

        return a list of list(with same rank)
    	'''

        sortedNodes = [] # to be returned

        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                temp = self.__dominate(nodes[i], nodes[j])
                # print 1
                if temp == -1:
                    # print 2
                    # nodes[i].setDominationCounter( nodes[i].getDominationCounter + 1 )
                    nodes[i].increaseDominationCounter()
                    nodes[j].addDominateSet(nodes[i])
                if temp == 1:
                    # print 3
                    nodes[i].addDominateSet(nodes[j])
                    nodes[j].increaseDominationCounter()

        ranklist = [ node for node in nodes if node.getDominationCounter() == 0 ]
        # print ranklist
        while len(ranklist) > 0:
            sortedNodes.append(ranklist)
            nextFront = []

            for nodep in ranklist:
                for nodeq in nodep.getDominateSet():
                    nodeq.decreaseDominationCounter()
                    if nodeq.getDominationCounter() == 0:
                        nextFront.append(nodeq)
            ranklist = nextFront

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


    def crowdingDistanceCompute(nodes):
    	'''
    	input a given nodes, compute crowding distance
    	
        return a sorted nodes list according to the crowd distance
        '''
    	pass



def main():
    # node = Node(1)
    # print node.getRank()
    x = Node([1,2])
    y = Node([2,1])
    z = Node([5,6])
    pop = [x,y,z]
    nsga2 = NSGA2(pop)

    for list in nsga2.nonDominatedSort(pop):
        # print 1
        for node in list:
            print node.getX()

if __name__ == '__main__':
    main()