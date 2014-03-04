import lineSearch

def objectiveFunction(x) :
	return (x-2)**2



print lineSearch.bisection([0,10], 0.1, objectiveFunction, 0.005)