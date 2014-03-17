#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TIES451 - programming assignment final
Multi-Objective Optimization - NSGA2
# ======================================
# This is a help function for GA 
# algorithm
# 
# ======================================
Author: Mou Hao

this file is the help file for NSGA-2 and MOEA/D algorithms
for proper useage, one should modify the import and the create node 
function in linearCrossOver function
'''

__author__ = "Mou Hao"

from objectiveFunction import *
import random

class Node:
    '''
    Class Node, design for a store the indiviudal in the evolutionary programming of NSGA-2

    '''

    def __init__(self, attribute):
        self.__attribute = attribute # attribute of this node

        # set objective value
        self.__x = objectiveFunction(self.__attribute)
        self.__weightedX = 0

    def getAttribute(self):
        return self.__attribute

    def getWeightedX(self):
        return self.__weightedX

    def setWeightedX(self, weightedX):
        self.__weightedX = weightedX

    def setAttribute(self, newAttribute):
        self.__attribute = newAttribute

    def getX(self):
    	return self.__x

    def __lt__(self, node):
        return self.__weightedX > node.getWeightedX()

class MoeaD:
    '''
    Multi-Objective Optimization using Weighted Algorithm of objective value
    '''

    def __init__(self, initialPopulation):
        '''
        set initial population
        '''

        self.__population = initialPopulation

    def getPopulation(self):
        return self.__population

    def moeaD(self, iteration):
        '''
        MOEA/D algorithm

        input a iteration time
        output a optima value for given ratio of weights

        This implementation only suitable for the two objective functions
        type problem

        after iteration the population is sorted
        '''
        
        maxIteration = iteration
        size = len( self.__population )
        
        front = []

        for i in range(0, 21):

            initialPopulation = [ node for node in self.__population ]
            for j in range(iteration):

                # set weighted objective value for each node
                a = i * 1.0 / 20
                for node in initialPopulation:
                    # this calculation is only suitable for two objective function
                    X = node.getX()
                    node.setWeightedX( X[0] * a + X[1] * ( 1 - a ) )

                # generate offspring and combine it with population
                offspring = generateOffspring(initialPopulation)

                for node in offspring:
                    X = node.getX()
                    node.setWeightedX( X[0] * a + X[1] * ( 1 - a ) )

                tempPopulation = initialPopulation + offspring

                # select the best of pool
                tempPopulation.sort()

                initialPopulation = tempPopulation[ 0 : size ]

            # append the best node to frontier of every weight
            front.append(initialPopulation[0])

        return front

def realCodeMutation(node):
    '''
    implement mutation on a node

    None return, set the new attribute
    '''

    attribute = node.getAttribute()
    changeIndex = int(round(random.random()*(len(attribute)-1)))

    # a = random.sample([-1,1],1)
    # direction = a[0]
    # rangeToChange = 0.5
    # domain = attribute[changeIndex]
    # precision = 2 ** ( - random.random() * 16 )
    if changeIndex == 0:
        if attribute[changeIndex] <= 0.1:
            attribute[changeIndex] = attribute[changeIndex] + random.uniform(0,0.1)    
        elif attribute[changeIndex] >= 0.9:
            attribute[changeIndex] = attribute[changeIndex] - random.uniform(0,0.1)
    else:
        attribute[changeIndex] = attribute[changeIndex] + random.uniform(-0.5,0.5)

    node.setAttribute(attribute)

def linearCrossOver(node1, node2):
    '''
    implement linear cross over of two parents

    return a node
    '''
    attribute1 = node1.getAttribute()
    attribute2 = node2.getAttribute()
    newAttribute = []
    for i in range(len(attribute2)):
        if i == 0:
            a = random.uniform(0, 1)
        else:
            a = random.uniform(-0.5,1.5)
        newAttribute = newAttribute + [ attribute1[i] * a + ( 1 - a ) * attribute2[i] ]
    
    # node = nsga2.Node(newAttribute)
    node = Node(newAttribute)
    return node

def generateOffspring(nodes):
    '''
    generate offspring with self.__population
    - tournament selection
    - cross over - linear cross over
    - mutation

    input a list of last generation
    out a list of new generation
    '''
    
    offspringTemp = [] # the temp list of offsprings
    # print nodes
    # size = len(nodes)
    # doing cross over
    for i in range( len(nodes) ):
         # with assumption that nodes is biger much bigger than 6
        tournament1 = random.sample(nodes, 2)
        tournament1.sort()
        parent1 = tournament1[1]

        tournament1 = random.sample(nodes, 2)
        tournament1.sort()
        parent2 = tournament1[1]
        
        # with probability 0.8 to crossover
        if random.random() < 0.8:
            offspringTemp.append(linearCrossOver(parent1, parent2)) # store the offspring of parents 1 and 2
        else:
            if parent1 < parent2:
                offspringTemp.append(parent2)
            else:
                offspringTemp.append(parent1)

    # doing mutation
    for node in offspringTemp:
        realCodeMutation(node)

    return offspringTemp