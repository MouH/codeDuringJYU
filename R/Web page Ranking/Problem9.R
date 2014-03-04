source("InitiationFunction.R")
source("UpdateFunction.R")
source("OccupancyRatios.R")

initiationStateProbo <- c(0.2,0.2,0.2,0.2,0.2)
pageState <- c(1,2,3,4,5)
initiationState <- InitiationFunction(runif(1),initiationStateProbo,pageState)

tMatrix <- matrix(0,5,5)
tMatrix[1,] <- c(0,0,0,0,1)
tMatrix[2,] <- c(1,0,0,0,0)
tMatrix[3,] <- c(1,0,0,0,0)
tMatrix[4,] <- c(1,0,0,0,0)
tMatrix[5,] <- c(1,0,0,0,0)


samplePath <- 1:1000
currentMatrix <- matrix(0,5,5)

for(i in 1:1000){
	if(i==1)
		currentMatrix = currentMatrix + tMatrix
	else
		currentMatrix = currentMatrix %*% tMatrix	

	samplePath[i] <- UpdateFunction(initiationState,runif(1),currentMatrix)
}


ratios <- OccupancyRatios(samplePath,length(pageState))
time <- 1:1000
plot(time,ratios[1,],col="green",ylim=c(0,1),main="Figure 5 Occupancy Ratios of Graph G'")
points(time,ratios[2,],col="red")
points(time,ratios[3,],col="blue")
points(time,ratios[4,],col="yellow")
points(time,ratios[5,],col="gray")
legend("topright",legend=c("vertex1","vertex2","vertex3","vertex4","vertex5"),
       col = c("green","red","blue","yellow","gray"),
	   lty=1,lwd=2)


