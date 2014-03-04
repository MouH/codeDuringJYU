% ------------------------------
% This is the GA algorithm
%
% Author: Mou Hao
% ------------------------------
function [bestFitnesses, solution] = f_GA (initialGeneration, f_fitnessFunction, crossOverProbability, mutationProbability, maxGenerations)

populationSize = size(initialGeneration);   % populationSize of each generation

% initialise  
intermediatePopulation = ones(populationSize);
matingPool = ones(populationSize);
fitnessValue = zeros(populationSize(1),1);
bestFitnesses = zeros(maxGenerations,1);
generation = initialGeneration;
binarySolution = zeros(1,populationSize(2));

% evolution starts
for i = 1 : maxGenerations

    % compute fitness value for every individual in current generation
    fitnessValue = f_fitnessFunction(generation);
	[bestFitnesses(i), index] = max(fitnessValue);
	binarySolution = generation(index,:);
	
	expectedCount = fitnessValue / mean(fitnessValue);            % A in the book
	probabilityOfSelection = expectedCount / populationSize(1);   % B in the book
	cumulativeOfSelection = zeros(populationSize(1),1);           % C in the book
	for j = 1 : populationSize(1)
		cumulativeOfSelection(j) = sum(probabilityOfSelection(1:j));
	end
	
	% generate mating individuals
	for j = 1 : populationSize(1)
		temp = find(cumulativeOfSelection >= rand());
		matingPool(j,:) = generation(temp(1),:);
	end
	
	% cross over of mating pool
	for j = 1 : ( populationSize(1) / 2 )
		if ( rand() > ( 1 - crossOverProbability ) )
			crossOverBit = round(rand(5)*18) + 1;
			intermediatePopulation(j,:)    = [ matingPool(j, 1:crossOverBit), matingPool(j+10, crossOverBit+1 : end)];
			intermediatePopulation(j+10,:) = [ matingPool(j+10, 1:crossOverBit), matingPool(j, crossOverBit+1 : end)];
		else
		    intermediatePopulation(j,:) = matingPool(j,:);
		    intermediatePopulation(j+10,:) = matingPool(j+10,:);
		end
	end

	% mutation and generate next generation
	generation = abs(intermediatePopulation - (rand(populationSize) < mutationProbability)); 
	
end

binaryToDecimalMultiplier = 2 .^ [ 9 : -1 : 0 ]';
solution = [ binarySolution(1:10)*binaryToDecimalMultiplier*( 6 / ( 2^10 - 1 )),binarySolution(11:20)*binaryToDecimalMultiplier*( 6 / ( 2^10 - 1 ))];

end