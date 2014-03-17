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
'''

__author__     = "Mou Hao"

import random
import nsga2

def realCodeMutation(node):
    '''
    implement mutation on a node

    None return, set the new attribute
    '''

    attribute = node.getAttribute()
    changeIndex = int(round(random.random()*(len(attribute)-1)))
    a = random.sample([-1,1],1)
    direction = a[0]
    rangeToChange = 0.5
    domain = attribute[changeIndex]
    precision = 2 ** ( - random.random() * 16 )

    attribute[changeIndex] = attribute[changeIndex] + direction * rangeToChange * domain * precision
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
        a = random.uniform(-0.25, 1.25)
        newAttribute = newAttribute + [ attribute1[i] * a + ( 1 - a ) * attribute2[i] ]

    node = nsga2.Node(newAttribute)
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
        if random.random() < 1:
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