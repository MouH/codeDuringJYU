#
# InitiationFunction.R
#
# Simulate a random variable X on {a[1],a[2],...,a[n]} with probabilities
# p[1],p[2],...,p[n] using a uniformly distributed input variable on [0,1],
# as desribed in Levin, Peres, Wilmer (2008, Eq B.10).
# See also  (2002, p 19).
#
# Lasse Leskelä 2012-11-05
#
# Input:
# u (real number in [0,1]) argument of the initiation function
# p (n-vector) probability mass function: p[i] = Pr(X=a[i])
# a (n-vector) states of X: a[i] is the i-th state of X
#
# Output:
# x (number in {a[1],...,a[n]) is the value x=phi(u)
#

InitiationFunction <- function (u,p,a) {
  n <- length(p)
  F <- cumsum(p)

  k <- 1
  while (k < n && u >= F[k]) {
    k <- k+1
  }
  return(a[k])
}