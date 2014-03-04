source("InitiationFunction.R")
source("OccupancyRatios.R")

state <- c(1,2,3)
currentP <- c(0.1,0.8,0.1)
currentWeather <- c(1:100)
for(i in 1:100){
	u <- runif(1)
	currentWeather[i] = InitiationFunction(u,currentP,state)
}

a <- table(currentWeather)
hist(currentWeather,main="Figure 1   Histogram of Current Weather")