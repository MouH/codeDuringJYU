from nsga2 import *
import random
from GAhelper import *


def main():
    # node = Node(1)
    # print node.getRank()
    pop = []
    for i in range(20):
        node = Node([random.random()*20, random.random()*20])
        pop.append(node) 
    hoho = NSGA2(pop)
    hoho.nsga2(20)
    for i in hoho.getPopulation():
        print i.getAttribute()

    

    

if __name__ == '__main__':
    main()