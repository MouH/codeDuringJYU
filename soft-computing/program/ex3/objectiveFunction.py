def objectiveFunction(attributeX):
    '''
    input the attribute list X
    return objective value list
    '''
    # x1 = attributeX[0]
    return [ sum(attributeX), attributeX[0]-attributeX[1] ] # a test