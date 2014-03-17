import math

def objectiveFunction(attributeX):
    '''
    input the attribute list X
    return objective value list

    ZDT1 problem
    '''
    # x1 = attributeX[0]

    f1 = attributeX[0]

    gf = 1 + 9 / (30 - 1) * sum(attributeX[1:])

    f2 = 1 - math.sqrt( f1 / gf )

    return [ f1, f2 ] # a test