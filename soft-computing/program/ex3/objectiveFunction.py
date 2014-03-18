import math

def objectiveFunction(attributeX):
    '''
    input the attribute list X
    return objective value list

    ZDT1 problem
    '''
    # TEST for MOEA/D
    # ======================================================
    #   # ZDT1
    # f1 = attributeX[0]

    # gf = 1 + 9 / (30 - 1) * sum(attributeX[1:])

    # f2 = 1 - math.sqrt( f1 / gf )

    # return [ f1, f2*gf ] # a test




    # #ZDT2
    # f1 = attributeX[0]

    # gf = 1 + 9 / (30 - 1) * sum(attributeX[1:])

    # f2 = 1 - ( f1 / gf ) ** 2

    # return [ f1, f2*gf ] # a test


    # # ZDT3

    f1 = attributeX[0]

    gf = 1 + 9 / (30 - 1) * sum(attributeX[1:])

    f2 = 1 - math.sqrt( f1 / gf ) - (f1 / gf) * math.sin( 10 * f1 * math.pi )

    return [f1, f2*gf]  
    # ======================================================
