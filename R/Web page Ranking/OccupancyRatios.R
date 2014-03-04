
# OccupancyRatios
# Lasse  2012-11-05
#
# Input:
# X (T-vector) sample path of a random sequence with values in {1,2,...,n}
#              X[s+1] is the value of X at time s, for s in {0,1,...,T-1}
# n (integer) number of states 
#
# Output:
# Y (n x T matrix) Y[i,t] is the fraction of time indices s in {0,...,t-1} for which X at time s equals i.
#

OccupancyRatios <- function (X,n) {
  T <- length(X)
  Y <- matrix(0,n,T)
  for (i in 1:n) {
    Y[i,] <- cumsum(X==i)/(1:T)
  }
  return(Y)
}
