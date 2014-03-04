

InitiationFunction <- function (u,p,a) {
  n <- length(p)
  F <- cumsum(p)

  k <- 1
  while (k < n && u >= F[k]) {
    k <- k+1
  }
  return(a[k])
}