source("InitiationFunction.R")
source("UpdateFunction.R")
source("OccupancyRatios.R")

initiationStateProbo <- c(0.25,0.25,0.25,0.25)
pageState <- c(1,2,3,4)
initiationState <- InitiationFunction(runif(1),initiationStateProbo,pageState)

tMatrix <- matrix(0,4,4)
tMatrix[1,] <- c(0.25,0.25,0.25,0.25)
tMatrix[2,] <- c(1,0,0,0)
tMatrix[3,] <- c(1,0,0,0)
tMatrix[4,] <- c(1,0,0,0)

samplePath <- 1:1000
currentMatrix <- matrix(0,4,4)

for(i in 1:1000){
	if(i==1)
		currentMatrix = currentMatrix + tMatrix
	else
		currentMatrix = currentMatrix %*% tMatrix	

	samplePath[i] <- UpdateFunction(initiationState,runif(1),currentMatrix)
}

#hist(samplePath)
ratios <- OccupancyRatios(samplePath,length(pageState))
time <- 1:1000
plot(time,ratios[1,],col="red",ylim=c(0,1),main="Figure 4 Occupancy Ratio of Graph G")
points(time,ratios[2,],col="green")
points(time,ratios[3,],col="blue")
points(time,ratios[4,],col="yellow")
legend("topright",legend=c("vertex1","vertex2","vertex3","vertex4"),
       col = c("red","green","blue","yellow"),
	   lty=1,lwd=2)


