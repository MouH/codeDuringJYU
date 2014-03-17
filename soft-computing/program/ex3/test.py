from nsga2 import *
import random
from GAhelper import *
from objectiveFunction1 import objectiveFunction
import matplotlib.pyplot as plt


def main():

    # ZDT1
    initialNodes = []
    for j in range(20): # 20 nodes
        attribute = []
        for i in range(30): # 30 variable
            attribute.append(random.random()+1)
        node = Node(attribute)
        initialNodes.append(node)

    front = []
    for i in range(20):
        zdt1 = NSGA2(initialNodes)
        zdt1.nsga2(500)
        result = zdt1.getPopulation()
        front += [ result[1].getX() ]
        # print objectiveFunction( result[1].getAttribute() )
    print front

    f1 = [ x[0] for x in front ]
    f2 = [ x[1] for x in front ]
    plt.plot(f1,f2, 'bo')
    plt.xlabel('f1')
    plt.ylabel('f2')
    plt.show()
    # ZDT2


    # ZDT3    

    

if __name__ == '__main__':
    main()