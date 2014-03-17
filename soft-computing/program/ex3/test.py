# from nsga2 import *
import random
# from GAhelper import *
# from objectiveFunction import objectiveFunction
import matplotlib.pyplot as plt
from moeaD import *

def main():


    # TEST for NSGA2

    # ======================================================
    # front = []
    # # for i in range(20):
    # #     # ZDT1
    # initialNodes = []
    # for j in range(20): # 20 nodes
    #     attribute = []
    #     for m in range(30): # 30 variable
    #         attribute.append(random.random()+1)
    #     node = Node(attribute)
    #     initialNodes.append(node)

        


    # zdt1 = NSGA2(initialNodes)
    # zdt1.nsga2(100)
    # front = zdt1.getPopulation()
    # #     result = zdt1.getPopulation()
    # #     front += [ result[1].getX() ]
    # #     # print objectiveFunction( result[1].getAttribute() )
    # # print front

    # f1 = [ x.getX()[0] for x in front ]
    # f2 = [ x.getX()[1] for x in front ]
    # plt.plot(f1,f2, 'bo')
    # plt.xlabel('f1')
    # plt.ylabel('f2')
    # plt.show()
 
    # ======================================================


    # TEST for MOEA/D
    # ======================================================
    initialNodes = []
    for j in range(20): # 20 nodes
        attribute = []
        for m in range(30): # 30 variable
            attribute.append(random.random())
        node = Node(attribute)
        initialNodes.append(node)

    test = MoeaD(initialNodes)

    front = test.moeaD(100)
    print len(front)
    f1 = [ node.getX()[0] for node in front ]
    f2 = [ node.getX()[1] for node in front ]
    print f1
    print f2
    plt.plot(f1,f2, 'bo')
    plt.xlabel('f1')
    plt.ylabel('f2')
    plt.show()
 



    # ======================================================



    

if __name__ == '__main__':
    main()