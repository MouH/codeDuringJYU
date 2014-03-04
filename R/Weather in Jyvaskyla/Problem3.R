source("InitiationFunction.R")
source("UpdateFunction.R")

state <- c(1,2,3)
tMatrix <- matrix(0,3,3)
tMatrix[1,] <- c(0.5,0.4,0.1)
tMatrix[2,] <- c(0.2,0.6,0.2)
tMatrix[3,] <- c(0.1,0.6,0.3)
currentWeatherPro <- c(0.1,0.8,0.1)
weatherChain <- c(1:10)
currentMatrix <- matrix(0,3,3)

startWeather <- InitiationFunction(runif(1),currentWeatherPro,state)

for(i in 1:10){
	if(i==1)
		currentMatrix = currentMatrix + tMatrix
	else
		currentMatrix = currentMatrix %*% tMatrix	

	weatherChain[i] <- UpdateFunction(startWeather,runif(1),currentMatrix)
}

plot(c(0:10),c(startWeather,weatherChain),type="s",xlab="time",ylab="weather state",main="Figure 2  10-day Sample Path")