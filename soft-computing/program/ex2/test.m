% ----------------------------
% This is a test file for Genetic Algorithm of TIES451
%
% Author: Mou Hao
% ----------------------------

clear;clc;
tic;

% define variables

population    = 20;
genomeLength  = 10;
variableNums = 2;

crossOverProbability = 0.8;
mutationProbability  = 0.05;
maxGenerations       = 100;


% generate initial generation
initialGeneration = f_variablesGeneration(variableNums, population, genomeLength);

% start GA algorithm
[bestFitnesses, solution] = f_GA(initialGeneration, @f_fitnessFunction, crossOverProbability, mutationProbability, maxGenerations);

solution

% plot the result
figure
plot(1:maxGenerations, bestFitnesses)

title('GA play result')
xlabel('generation')
ylabel('best fitnesses value of every generation')





toc;