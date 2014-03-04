source("InitiationFunction.R")
source("UpdateFunction.R")
source("OccupancyRatios.R")

state <- c(1,2,3)
tMatrix <- matrix(0,3,3)
tMatrix[1,] <- c(0.5,0.4,0.1)
tMatrix[2,] <- c(0.2,0.6,0.2)
tMatrix[3,] <- c(0.1,0.6,0.3)
currentWeatherPro <- c(0.1,0.8,0.1)
weatherChain <- c(1:1000)
currentMatrix <- matrix(0,3,3)

startWeather <- InitiationFunction(runif(1),currentWeatherPro,state)

for(i in 1:1000){
	if(i==1)
		currentMatrix = currentMatrix + tMatrix
	else
		currentMatrix = currentMatrix %*% tMatrix	

	weatherChain[i] <- UpdateFunction(startWeather,runif(1),currentMatrix)
}

ratio <- OccupancyRatios(weatherChain,length(state))

plot( c(1:1000),ratio[1,],type="s",
      xlab="time",ylab="weather state",
	  ylim=c(0,1),col="blue",
	  main = "Figure 3 Occupancy Ratio"
	  )

points(c(1:1000),ratio[2,],type="s",col="red")
points(c(1:1000),ratio[3,],type="s",col="green")
legend("topright",legend=c("Sunny","Cloudy","Rainy"),
       col = c("blue","red","green"),
	   lty=1,lwd=2)
	   
	   
	   
	   
	   
	   
	   
	   
	   
	   