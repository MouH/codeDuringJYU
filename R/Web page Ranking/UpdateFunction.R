#
# UpdateFunction.R
#
# Random mapping presentation of a Markov chain on {1,2,....,n} with transition matrix P
# in terms of a uniform random variable on [0,1].
# See Levin, Peres, Wilmer (2008, Sec 1.2) or Häggström (2002, p 19).
#
# Lasse Leskel? 2012-11-05
#
# Input:
# i (integer in [1,n]) current state of the Markov chain
# z (real number in [0,1]) auxiliary argument of the update function
# P (n x n matrix) transition matrix of the Markov chain: P[i,j] = Pr(X_1=j | X_0=i)
#
# Output:
# j (integer in [1,n]) the update function of matrix P evaluated at (i,z)
#

source('InitiationFunction.R')

UpdateFunction <- function (i,z,P) {
  n <- dim(P)[1]
  j <- InitiationFunction(z,P[i,],1:n)
  return(j)
}