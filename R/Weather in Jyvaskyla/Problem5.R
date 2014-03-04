source("InitiationFunction.R")

state <- c(1,2,3)
currentP <- c(0.1,0.8,0.1)
tMatrix <- matrix(0,3,3)
tMatrix[1,] <- c(0.5,0.4,0.1)
tMatrix[2,] <- c(0.2,0.6,0.2)
tMatrix[3,] <- c(0.1,0.6,0.3)
currentWeather <- InitiationFunction(runif(1),currentP,state)

ifelse(currentWeather==1,mu0 <- c(1,0,0),ifelse(currentWeather==2,mu0 <- c(0,1,0),mu0 <- c(0,0,1)))
mu <- matrix(0,1000,3)

for(i in 1:1000){
	if(i==1){
		mu[i,] = mu0 %*% tMatrix
	}
	else{
		mu[i,] = mu[i-1,] %*% tMatrix
	}
}


